import Save.configjson as cj
import WebReader.title as title
from datetime import date

class Model:
    list_title = []

    def __init__(self):
        self.saves_path = "../saves/save.json"
        
    def load(self):
        self.list_title = cj.load_json(self.saves_path)
        
    def save(self):
        cj.save_json(self.saves_path,self.list_title)

    def add(self, titre, site, url, num_chap):
        if url in self.list_title:
            return None
        last_update = date.today().strftime('%Y-%m-%d')
        nt = title.Title(titre,site,url,num_chap,last_update)
        self.list_title.append(nt)
        return nt

    def remove(self):
        pass