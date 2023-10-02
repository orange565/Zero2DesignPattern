import item as item
import dvd as dvd
import book as book
import library as library


print("\n\n***Print from item Class***\n")
my_book = item.Item("Trust","Hernan Diaz","2023", "Available")
my_book.display_info()

my_cd = item.Item("Star Wars","George Lucas","1977","not Available")
my_cd.display_info()

my_dvd = item.Item("Lord of the Rings","J.R.R. Tolkien","2001","Available")
my_dvd.display_info()

print("***Print from Dvd Class***\n")
dvd1 = dvd.Dvd("The God Father","Mario Puzo","1972","Available","Francis Ford Coppola")
dvd1.display_info()

dvd2 = dvd.Dvd("The Dark Knight","Jonathan Nolan","2008","not Available","Christopher Nolan")
dvd2.display_info()

print("***Print from Book Class***\n")

book1 = book.Book("The Housemaid ","Freida McFadden","2020","not Available","Genre")
book1.display_info()

book2 = book.Book("Killers of the Flower Moon","David Grann","2021","Available","History")
book2.display_info()

my_library = library.Library()
my_library.add_item(book2,"book")
my_library.add_item(dvd1,"dvd")
