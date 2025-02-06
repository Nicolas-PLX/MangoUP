from datetime import date

class Title:

    def __init__(self, title, last_chapter, last_update, site):
        self.title = title
        self.last_chapter = last_chapter
        self.last_update = last_update
        self.site = site


    def update_title(self,last_chapter):
        last_update = date.today()
        update = Title(self.title,last_chapter,last_update,self.site)        

        return update