import item as item
class Dvd(item.Item):
    #constructor
    def __init__(self,title,author,publication_year,status,director_name):
        super().__init__(title,author,publication_year,status)
        self.director_name = director_name

    def display_info(self):
        super().display_info()
        print (f"* Director Name = {self.director_name}\n*")