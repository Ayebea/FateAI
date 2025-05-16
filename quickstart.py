import random
import ollama
class quickstart(object):
    def __init__(self,genres=None):
        self.genres = genres or ["Fantasy","Horror", "Adventure", "Sci-Fi","Historical","Romance",
                      "Comedy","Mystery","Thriller","Drama","Fantasy","Slice of Life"]


    def quick(self):
        genre = random.choice(self.genres)
        prompt_title = f"Auto-generate a name for a random story in the {genre} genre. Return only the title"
        response1 = ollama.generate(
            model="mistral",
            prompt=prompt_title,
            options={"temperature": 0.8}
        )
        print(f"The title of our story is: {response1['response']}")
        prompt2 = ("Now offer a descriptive introduction to this story. At the end, ask the user"
                   " what they would like to do next to interacted with the story. ")
        intro = ollama.generate(
            model="mistral",
            prompt=prompt2,
            options={"temperature": 0.8}
        )
        print(f"{intro['response']}")
        while True:
            user_input = input()

            if user_input == "End Story.":
                break
            story = ollama.generate(
                model="mistral",
                prompt=user_input,
                options={"temperature": 0.8}
            )

            print(f"\n{story['response']}\n")




