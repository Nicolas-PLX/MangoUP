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
        
        for t in data["mangas"]:
             t_obj = Title(t['title'],t['site'],t['url'],t['last_chapter'],
                           t['last_update'])
             list_t.append(t_obj)
        
        print(f"Load {len(list_t)} title(s)...")
        print("Loading complete.")
        return list_t


def save_json(file_path,data):
        try:
            with open(file_path,"w") as f:
                 json_data = {"mangas":[i.to_dict() if isinstance(i,Title) else i for i in data]}
                 json.dump(json_data,f,ensure_ascii=False,indent=4)
                 print(f"Save complete in file \"{file_path}\".")
        except FileNotFoundError:
             print(f"Error : file '{file_path} not found.")
        except json.JSONDecodeError as e:
             print(f"Error writing json file : {e}")
             return None
        

def test():
     print("popo")