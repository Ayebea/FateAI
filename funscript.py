import sys
import ollama
from quickstart import quickstart
from detailed_start import DetailedStart
from storage import display_saves, load_story
from storage import save_story

def new_story(): #Make a new story
    new = input(""""
     1. Quick Start (Auto-Generate Story)
     2. Detailed Start
     """).strip()

    if new == "1":
        quickstart().quick()
    elif new == "2":
        DetailedStart().start()
def story_exists():
    saves = display_saves()
    if not saves:
        return

    choice = input("\n Enter your story number:").strip()

    try:
        i = int(choice) - 1
        if 0 <= i < len(saves):
            filename = saves[i]
            title,messages = load_story(filename)
            if messages:
                print(f"Continuing: {title}\n")

                while True:
                    response = input("You: ").strip()

                    if response == "Save Story.":
                        save_story(title, messages)
                        continue

                    if response == "End Story.":
                        print("\nThis story is now closed. See you next time!")
                        break

                    if not response:
                        continue

                    messages.append({"role": "user", "content": response})
                    user_input = ollama.chat(model = "mistral", messages = messages)
                    story_text = user_input["message"]["content"]
                    messages.append({"role": "assistant", "content": story_text})
                    print(f"\n{story_text}\n")

        else:
            print("Invalid")

    except ValueError:
        print("Enter a valid number")

def start_menu():
        print("Welcome to Fate AI,let's get you started")
        start = input("""
        1. New Story
        2. Continue story
        3. What is this?
        4. Exit
        """).strip()
        if start == "1":
            new_story()
        elif start == "2":
            story_exists()
        elif start == "3":
            print("See you in the next story!")
            sys.exit()

start_menu()