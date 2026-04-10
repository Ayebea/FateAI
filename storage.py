import json
import os
from datetime import datetime

SAVES = "saves"
def create_save_dir(): #Creates a save directory if none are found
        if not os.path.exists(SAVES):
                os.makedirs(SAVES)



def save_story(title,messages): #Save conversation history to JSON file
        create_save_dir()

        clean_title = ("".join(i for i in title if i.isalnum() or i
                              in (" ", "-", "_")).strip()).replace(" ","_")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{SAVES}/{clean_title}_{timestamp}.json"

        data = {"title":title,"save_time":datetime.now().isoformat(),"messages":messages}

        with open(filename,"w") as f:
                json.dump(data,f,indent=2)

        print(f"\n {clean_title}_{timestamp} saved")
        return filename

def load_story(filename): #Load story from json file
        path = f"{SAVES}/{filename}" if not filename.startswith(SAVES) else filename

        if not os.path.exists(path):
                print(f"Path {path} not found")
                return None, None

        with open(path, "r") as f:
                save_data = json.load(f)

        print(f"\nLoaded: {save_data['title']}")
        print(f"Last saved at: {save_data['save_time']}\n")
        return save_data["title"], save_data["messages"]

def display_saves(): #Displays current saves
        create_save_dir()

        saves = [i for i in os.listdir(SAVES) if i.endswith(".json")]

        if not saves:
                print("No stories found")
                return []

        print("\n Your saves:")

        for i, v in enumerate(saves,1):
                path = f"{SAVES}/{v}"
                with open(path, "r") as f:
                        save_data = json.load(f)
                print(f"  {i}. {save_data['title']} — saved {save_data['save_time'][:10]}")


        return saves

def delete_save(filename): #Deletes a save
        path = f"{SAVES}/{filename}" if not filename.startswith(SAVES) else filename
        if os.path.exists(path):
                os.remove(path)
                print(f"Deleted: {filename}")
        else:
                print(f"File not found: {filename}")


