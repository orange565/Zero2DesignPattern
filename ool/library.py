import book as Book
import dvd as Dvd
import item as Item
class Library:

    #constructor
    def __init__(self):
        self.book_list = []
        self.dvd_list = []
    
    #Define a function to add books and dvds to the library
    def create_dummy_library(self):
        self.dvd_list.append(Dvd.Dvd("The God Father","Mario Puzo","1972","Available","Francis Ford Coppola"))
        self.dvd_list.append(Dvd.Dvd("The Dark Knight","Jonathan Nolan","2008","Available","Christopher Nolan"))
        self.dvd_list.append(Dvd.Dvd("Star Wars","George Lucas","1977","Available","Unknown"))
        self.dvd_list.append(Dvd.Dvd("Lord of the Rings","J.R.R. Tolkien","2001","Available","Unknown"))
        self.book_list.append(Book.Book("The Housemaid","Freida McFadden","2020","Available","Genre"))
        self.book_list.append(Book.Book("Killers of the Flower Moon","David Grann","2021","Available","History"))

    #Define a function to add and item to library
    #item: book or dvd item(class)
    #type: book, dvd (string)
    def add_item(self,item,type):
        item.status = "Available"
        if type == "book":
            self.book_list.append(item)
        elif type == "dvd":
            self.dvd_list.append(item)
        else: 
            pass

    #Define a function to borrow and item from library
    #item: book or dvd item(class)
    #type: book, dvd (string)
    def borrow_item(self,item,type):
        if type == "book":
            if item in self.book_list:
                item.status = "unAvailable"
        elif type == "dvd":
            if item in self.dvd_list:
                item.status = "unAvailable"
        else:
            pass
    
    
    #Define a function to return and item to library
    #item: book or dvd (class)
    #type: book, dvd (string)
    def return_item(self,item,type):
        if type == "book":
            if item in self.book_list:
                item.status = "Available"
        elif type == "dvd":
            if item in self.dvd_list:
                item.status = "Available"
        else:
            pass
    

    #Define a function to find an item with given name
    #item_name: title for dvd or book
    def find_item(self, item_name):
        for book in self.book_list:
            if(book.title == item_name):
                return ("book",book)
        
        for dvd in self.dvd_list:
            if(dvd.title == item_name):
                return ("dvd",dvd)
        return ("none","")


    #Define a function to list available items
    #status: Available, unAvailable
    #check : To control list is empty or not
    def list_items(self,status):
        check = False
        for book in self.book_list:
            if book.status == status:
                book.display_info()
                check = True

        for dvd in self.dvd_list:
            if dvd.status == status:
                dvd.display_info()
                check = True     
        return check
    


