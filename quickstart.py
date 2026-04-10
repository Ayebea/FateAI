import random
import ollama
from storage import save_story
class quickstart(object):
    def __init__(self,genres=None):
        self.genres = genres or ["Fantasy","Horror", "Adventure", "Sci-Fi","Historical","Romance", #Genre choices
                      "Comedy","Mystery","Thriller","Drama","Fantasy","Slice of Life"]
        self.messages = [] #Conversation memory

    def quick(self): #Randomly generate story
        genre = random.choice(self.genres)
        self.messages = [
            {
                "role" : "system",
                "content" : (f"You will serve the role being an interactive storyteller. The genre of this story will be"
                             f"{genre}. You must retain vital information including, but not limited to, the plot, characters, events"
                             f"and character relationships. Any NPCs should act as realistically as possible, keeping "
                             f"both their characterization and details, no matter how small. After each response you give, prompt the user"
                             f"to respond. Under no circumstance may you break chracter or forget story events, even when the "
                             f"player asks.")
            }
        ]
        self.messages.append({
            "role": "user",
            "content" : (f"Auto-generate a name for a random story in the {genre} genre. Return only the title and nothing else")

    })
        title_response = ollama.chat(model="mistral",messages=self.messages)
        title = title_response["message"]["content"]
        self.messages.append({"role":"assistant","content":title})
        print(f"\n The title of our story is: {title}\n")

        self.messages.append({
            "role": "user",
            "content":(f"Now offer a descriptive introduction to this story.At the end, "
                       f"ask the user what they would like to do next")
        })
        intro_response = ollama.chat(model="mistral", messages=self.messages)
        intro = intro_response["message"]["content"]
        self.messages.append({"role": "assistant", "content": intro})
        print(f"\n {intro}\n")
        while True:
            user_input = input("You: ").strip()

            if user_input == "End Story.":
                print("\n This story is now closed. See you need time!")
                break
            if user_input == "Save Story.":
                save_story(title,self.messages)
                print("\n Save complete.\n")
                continue
            if not user_input:
                continue

            self.messages.append({"role":"user","content":user_input})
            response = ollama.chat(model="mistral", messages=self.messages)
            story_text = response["message"]["content"]
            self.messages.append({"role": "assistant", "content": story_text})
            print(f"\n{story_text}\n")




