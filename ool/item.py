class Item:
    #constructor
    def __init__(self,title,author,publication_year,status):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.status = status

    #Define a function to print item details
    def display_info(self):
        print("**********************************")
        print (f"* Title = {self.title} \n"+
               f"* Author = {self.author}\n"+
               f"* Publication year = {self.publication_year}\n"+
               f"* Status = {self.status}")

