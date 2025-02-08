import Save.configjson as cj

class Model:
    list_title = []

    def __init__(self):
        self.saves_path = "../saves/save.json"
        
    def load(self):
        self.list_title = cj.load_json(self.saves_path)
        
    def save(self):
        cj.save_json(self.saves_path,self.list_title)