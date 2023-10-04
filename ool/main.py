import item as item
import dvd as dvd
import book as book
import library as library


print("\n\n***Task-1***\n")
my_book = item.Item("Trust","Hernan Diaz","2023", "Available")
my_book.display_info()

my_cd = item.Item("Star Wars","George Lucas","1977","not Available")
my_cd.display_info()

my_dvd = item.Item("Lord of the Rings","J.R.R. Tolkien","2001","Available")
my_dvd.display_info()



print("\n\n*********Task-2**********\n")
dvd1 = dvd.Dvd("The God Father","Mario Puzo","1972","Available","Francis Ford Coppola")
dvd1.display_info()

dvd2 = dvd.Dvd("The Dark Knight","Jonathan Nolan","2008","Available","Christopher Nolan")
dvd2.display_info()


book1 = book.Book("The Housemaid ","Freida McFadden","2020","Available","Genre")
book1.display_info()

book2 = book.Book("Killers of the Flower Moon","David Grann","2021","Available","History")
book2.display_info()


print("\n\n*********Task-3**********\n")

my_library = library.Library()
my_library.add_item(book1,"book")
my_library.add_item(book2,"book")
my_library.add_item(dvd1,"dvd")
my_library.add_item(dvd2,"dvd")
print("__________3 books and 2 dvds are added________________")
my_library.list_items("Available")


my_library.borrow_item(dvd1,"dvd")
print("________________dvd1 is borrowed_____________________")
my_library.list_items("Available")



my_library.borrow_item(book1,"book")
print("________________book1 is borrowed_____________________")
my_library.list_items("Available")


my_library.return_item(dvd1,"dvd")
print("________________dvd1 is returned_____________________")
my_library.list_items("Available")

