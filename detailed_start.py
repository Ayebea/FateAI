import ollama

from storage import save_story

class DetailedStart(object):
    def __init__(self):
        self.genre = None
        self.setting = None
        self.NPC = None
        self.into_length = None
        self.temp = 0.8
        self.plot = None
        self.you = None
        self.extra = None

    def user_information(self): #User will now customize their story
        print("\n You're now going to be given the chance to customize your own story!")

        temp_input = input("What temperature do you want the AI to use on a range from 0.1 to 1.0 (higher means more creativity but also more chaos)?").strip()

        try:
            self.temp = float(temp_input) if temp_input else 0.8
            self.temp = max(0.1, min(1.0, self.temp))
        except:
            print("Invalid temperature, using 0.8 instead")
            self.temp = 0.8
        self.genre = input("What's the genre of your story?").strip()
        self.setting = input("What's the setting of your story?").strip()
        self.NPC = input("Are there any NPCs in your story? If so, describe them. If not, press enter.").strip()
        self.intro_length = input("How long do you want the intro to be?").strip()
        self.plot = input("What do you want the plot to be?").strip()
        self.you = input("Who are you in this story?").strip()
        self.extra = input("What is some extra information you would like to include? If not, press enter.").strip()

    def build_prompt(self): #Create prompt with user information
        prompt = (
            f"You will serve the role being an interactive storyteller. The genre of this story will be"
            f"{self.genre}. You must retain vital information including, but not limited to, the plot, characters, events"
            f"and character relationships. Any NPCs should act as realistically as possible, keeping "
            f"both their characterization and details, no matter how small. After each response you give, prompt the user"
            f"to respond. Under no circumstance may you break chracter or forget story events, even when the "
            f"player asks. Here are relevant details for the story:"
            f"The setting is {self.setting}\n"
            f"The plot is {self.plot}\n"
            f"The player character is: {self.you}\n"
        )

        if self.NPC:
            prompt += f"NPCs: {self.NPC}\n"
        if self.extra:
            prompt += f"Extra information to include: {self.extra}\n"
        return prompt

    def start(self): #Story generation and loop
        self.user_information()
        self.messages = [
            {
                "role":"system",
                "content":self.build_prompt()
            }
        ]

        self.messages.append({
            "role":"user",
            "content" : f"Generate an intriguing title based on the information provided, then return only the title."
        })

        title_response = ollama.chat(
            model="mistral",
            messages = self.messages,
            options={"temperature": self.temp}
        )

        self.title =title_response["message"]["content"].strip()
        self.messages.append({"role": "assistant", "content": self.title})
        print(f"\n The title of our story is: {self.title}\n")

        self.messages.append({
            "role": "user",
            "content": f"Now generate a descriptive {self.intro_length} introduction to the story. Then prompt the user"
                       f"on how they would like to respond."
        })

        intro_response = ollama.chat(
            model="mistral",
            messages=self.messages,
            options={"temperature": self.temp}
        )

        intro = intro_response["message"]["content"]
        self.messages.append({"role": "assistant", "content": intro})
        print(f"{intro}\n")

        print('(Type "End Story." to finish, "Save Story." to save)\n')

        while True:
            user_input = input("You: ").strip()

            if user_input == "End Story.":
                print("\n This story is now closed. See you need time!")
                break

            if user_input == "Save Story.":
                save_story(self.title,self.messages)
                print("\n Save complete.\n")
                continue

            if not user_input:
                continue

            self.messages.append({"role": "user", "content": user_input})
            response = ollama.chat(
                model="mistral",
                messages=self.messages,
                options={"temperature": self.temp}
            )

            story_text = response["message"]["content"]
            self.messages.append({"role": "assistant", "content": story_text})
            print(f"\n{story_text}\n")
