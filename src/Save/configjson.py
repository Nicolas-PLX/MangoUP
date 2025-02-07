import json, os
from WebReader.title import Title



def load_json(file_path):
        list_t = []
        try:
            with open(file_path,"r") as f:
                data = json.load(f)
        except FileNotFoundError:
             print(f"Error : file '{file_path} not found.")
        except json.JSONDecodeError as e:
             print(f"Error loading json file : {e}")
             return None
        
        for t in data["title"]:
             t_obj = Title(t['name'],t['site'],t['url'],t['last_chapter'],
                           t['last_update'])
             list_t.append(t_obj)
        
        print(f"Load {len(list_t)}...")
        print("Loading complete.")
        return list_t


def save_json(file_path,info):
        try:
            with open(file_path,"w") as f:
                 pass
        except FileNotFoundError:
             print(f"Error : file '{file_path} not found.")
        except json.JSONDecodeError as e:
             print(f"Error writing json file : {e}")
             return None
