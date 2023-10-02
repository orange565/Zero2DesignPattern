import item as item
class Book(item.Item):
    #constructor
    def __init__(self,title,author,publication_year,status,genre):
        super().__init__(title,author,publication_year,status)
        self.genre = genre
    
    def display_info(self):
        super().display_info()
        print (f"* Genre = {self.genre}\n*")

