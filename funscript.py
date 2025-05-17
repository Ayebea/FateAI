import sys
from quickstart import quickstart

def new_story(): #Make a new story
    new = input(""""
     1. Quick Start (Auto-Generate Story)
     2. Detailed Start
     """).strip()
    if new == "1":
        quickstart().quick()

def story_exists(): #Access existing story
    find = input("What's the name of your story?").strip()

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
            print("Coming soon")
        elif start == "4":
            print("See you in the next story!")
            sys.exit()

start_menu()