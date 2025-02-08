from datetime import date

class Title:

    def __init__(self, title,site,url, last_chapter, last_update):
        self.title = title
        self.last_chapter = last_chapter
        self.last_update = last_update
        self.site = site
        self.url = url


    def update_title(self,last_chapter):
        last_update = date.today()
        update = Title(self.title,self.url,last_chapter,last_update,self.site)        

        return update
    
    def to_dict(self):
        return {
            "title":self.title,
            "site":self.site,
            "url":self.url,
            "last_chapter":self.last_chapter,
            "last_update":self.last_update
        }

    