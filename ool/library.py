import book as Book
class Library:

    #constructor
    def __init__(self):
        self.book_list = []
        self.dvd_list = []

    def add_item(self,item,type):
        if type == "book":
            self.book_list.append(item)
        elif type == "dvd":
            self.dvd_list.append(item)
        else: 
            pass


    def borrow_item(self,item):
        pass

    def return_item(self,item):
        pass

    def list_available_items(self,item):
        for book in self.book_list:
            pass #book print

        for dvd in self.dvd_list:
            pass #dvd print
        pass

