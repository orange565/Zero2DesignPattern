import os
import library as library
import book as book
import dvd as dvd


#Define a function to clear console before write 
def clear_console():
    clear = lambda: os.system('clear')
    clear()

#Define a function to print menu after each operation
# error_message : if user enters a wrong entry
def print_menu(error_message):
    clear_console()
    if(error_message != ""):
        print(error_message)
    else:
        print("Welcome to the Library. Please choose the operation that you want")

    print("Press 1 - Borrow an item")
    print("Press 2 - Return an item")
    print("Press 3 - Display list of available items ")
    print("Press q - Quit the program")

#Add some books to library
my_library = library.Library()
my_library.create_dummy_library()

quit = ''
value = ''
wrong_entry = ''

# Customer input loop
# The program continues to run until the user types q
while quit != 'q':
    print_menu(wrong_entry)
    wrong_entry = ""
    value = input("")
    quit=value

    # 1- Borrow an item from library
    if value == "1":

        my_library.list_items("Available") #list available items

        print("Please write the title of item")
        item_name = input() #get item name from user

        item_type,item = my_library.find_item(item_name) #use title to find the item from the library
        
        if item_type == "none": # item not found
            print("item not found")

        else: #item found and borrowed
            print("The "+item_type +" \"" + item_name + "\" is borrowed to you. Please don't forget to bring back to us")
            my_library.borrow_item(item,item_type)
            
        input("Press any button to continue")


    # 2- Return back an item to library
    elif value == "2":
        check = my_library.list_items("unAvailable") #list unavailable items

        if check is False:
            print("We don't have any borrowed items.")
        else:
            print("Please write the name of item")
            item_name = input()  #get item name from user

            item_type,item = my_library.find_item(item_name)#use title to find the item from the library

            if item_type == "none":# item not found
                print("item not found")
            
            else: #item found and return back
                print("The "+item_type +" \"" + item_name + "\" is return back to library. Thank you!")
                my_library.return_item(item,item_type)
        input("Press any button to continue")


    # 3 - List available items from the library   
    elif value == "3":

        my_library.list_items("Available") #list available items
        input("Press any button to continue")

    # q - To quit
    elif value == "q":
        quit = value

    # Wrong entry
    else:
        wrong_entry = "Wrong entry, please try again"
        

