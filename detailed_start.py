import ollama

class DetailedStart(object):
    def __init__(self,genre,setting,NPC,intro_length,temp,plot,you,extra):
        self.genre = genre
        self.setting = setting
        self.NPC = NPC
        self.into_length = intro_length
        self.temp = temp
        self.plot = plot
        self.you = you
        self.extra = extra
    def start(self):
        ollama.generate(
            model="mistral",
            prompt= "You're main objective is to facilitate storytelling given the users wishes,"
                    "you will be given information relating to this story but don't generate a response yet until all information is given."
                    "Instead begin thinking of a story as more information is given. All details are important so you must stay consistent.",
            options={"temperature": 0.8}
        )
        print("You're now going to be given the chance to customize your own story!")
        self.temp = input("What temperature do you want the AI to use (higher means more creativity but also more chaos)?")
        ollama.generate(
            model="mistral",
            prompt="",
            options={"temperature": self.temp}
        )
        self.genre = input("What's the genre of your story?")
        ollama.generate(
            model="mistral",
            prompt=f"Your genre will be {self.genre}",
            options={"temperature": self.temp}
        )
        self.setting = input("What's the setting of your story?")
        self.NPC = input("Are there any NPCs in your story? If so, describe them,")
        self.intro_length = input("How long do you want the intro to be?")
        self.plot = input("What do you want the plot to be?")
        self.you = input("What do you want the You to be?")