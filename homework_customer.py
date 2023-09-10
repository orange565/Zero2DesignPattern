from datetime import datetime
import re
import os
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

class Customer:
  def __init__(self, name, surname, email, phone):
    self.name = name
    self.surname = surname
    self.email = email
    self.phone = phone

class Order:
  def __init__(self, email, product, amount, date):
    self.email = email
    self.product = product
    self.amount = amount
    self.date = date

#Define a function to clear console before write 
def clear_console():
    clear = lambda: os.system('clear')
    clear()


# Define a function to validate an Email
def check_email(email):
    # regular expression for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    # pass the regular expression and the string into the fullmatch() method
    return(True if(re.fullmatch(regex, email)) else  False)



# Define a function to validate turkish phone number
def check_phone(phone):
    # regular expression for validating turkish phone number
    regex = r'^\(?0[1-9][0-9]{2}\)?[-.\s]?\d{3}[-.\s]?\d{2}[-.\s]?\d{2}$'

    # pass the regular expression and the string into the fullmatch() method
    return(True if(re.fullmatch(regex, phone)) else  False)

# Define a function to validate name and surname
def check_name(name):
    # regular expression for validating name and surname
    regex = r'^[A-Za-zÀ-ÖØ-öø-ÿ\-\'\s]+$'

    # pass the regular expression and the string into the fullmatch() method
    return(True if(re.fullmatch(regex, name)) else  False)

#Define a function to check a customer is in the list or not
def is_customer(customer_list, email_address):
    for customer in customer_list:
      if(customer.email == email_address):
        return customer
    return False

#Define a function to check user input if q or not to quit
def check_quit(input):
   return(True if input == 'q' else False)

#Define a function to return orders for given e-mail address
def get_customer_orders(orders,email):
   order_list = []
   for order in orders:
      if order.email == email:
         order_list.append(order)
   return order_list

#Define a function to print order list
def print_orders(orders):
   i=1
   for order in orders:
      print("Order-" + str(i) + ":")
      print(f"{Fore.BLUE}\t Product Name : {Style.RESET_ALL}" + order.product)
      print(f"{Fore.BLUE}\t Product Amount : {Style.RESET_ALL}" + str(order.amount))
      print(f"{Fore.BLUE}\t Order Time : {Style.RESET_ALL}" + str(order.date))
      i+=1

#Define a function to print a customer
def print_customer(customer):
    print(f"{Fore.BLUE}\t Name = {Style.RESET_ALL}" + customer.name)
    print(f"{Fore.BLUE}\t Surname = {Style.RESET_ALL}" + customer.surname)
    print(f"{Fore.BLUE}\t Phone = {Style.RESET_ALL}" + customer.phone)
    print(f"{Fore.BLUE}\t E-mail = {Style.RESET_ALL}" + customer.email)

#Define a function to create an order to a customer
def create_order(order_list,customer,product_name,product_amount):
    new_order = Order(customer.email,product_name, product_amount,datetime.now())
    order_list.append(new_order)
    clear_console()
    print(f"{Fore.GREEN}Your order created successfully.{Style.RESET_ALL}")
    print(" You can see all your orders below")
    orders = get_customer_orders(order_list,customer.email)
    print_orders(orders)

#Define a function to update customer and write in console
def update_customer(customer_list,name,surname,phone,email):
   for customer in customer_list:
      if customer.email == email:
        customer.name = name
        customer.surname = surname
        customer.phone = phone

        clear_console()
        print(f"{Fore.GREEN}Your account updated successfully.{Style.RESET_ALL}")
        print_customer(customer)

def print_menu():
   print(f"{Fore.BLUE}\t Press 1 : {Style.RESET_ALL}to see your orders")
   print(f"{Fore.BLUE}\t Press 2 : {Style.RESET_ALL}to create a new order")
   print(f"{Fore.BLUE}\t Press 3 : {Style.RESET_ALL}to edit your account")
   print(f"{Fore.BLUE}\t Press 4 : {Style.RESET_ALL}to use different account")
   print(f"{Fore.BLUE}\t Press q : {Style.RESET_ALL}to quit")


#public variables
quit = ''
customer_list = []
order_list =[]
email = ''

#create a customer and and order
customer1 = Customer("Fatih","Subaşı","f@f.com","05336531615")
order1 = Order(customer1.email,"product-1",5, datetime.now())
customer_list.append(customer1)
order_list.append(order1)


#the program starts running from here 
clear_console()
print(f"{Fore.RED}You can always enter q to quit!{Style.RESET_ALL}" )


# Customer input loop
# The program continues to run until the user types q
while quit != 'q':

    if email == '':
        clear_console()
        email = input("Welcome to MD Customer Services. \nPlease enter your e-mail address: ")
        if check_quit(email): break;
    
    #if the given e-mail addres format is wrong ask again to customer
    while not check_email(email) :
        print(f"{Fore.RED}The e-mail address you entered is wrong. {Style.RESET_ALL}")
        email = input("Please enter your e-mail address: ")
        if check_quit(email): break;
    
    #Check e-mail address is in current customer list or not
    current_customer = is_customer(customer_list,email)

    #if customer is found in the current list => existing customer
    if current_customer:
        #Write the welcome message and the menu
        clear_console()
        print(f"{Fore.RED}WELCOME! {current_customer.name} {current_customer.surname} {Style.RESET_ALL}")
        print("What do you want to do today?")
        print_menu()

        #Get customer input and check
        choise = input()
        
        #See order list for customer
        if choise == '1':
           clear_console()
           print("You can see your orders below : ")
           orders = get_customer_orders(order_list,email)
           print_orders(orders)
           input(f"{Fore.RED}Please type to continue...{Style.RESET_ALL}")

        #Create order for customer
        elif choise == '2':
            clear_console()
            product_name = input("Please enter product name :    ")

            product_amount = input("Please enter product amount :   ")
               
            #Get product_amount in correct format
            while not product_amount.isdigit():
                print(f"{Fore.RED}This is not a number.{Style.RESET_ALL}")
                product_amount = input(" Please enter product amount : ")
                if check_quit(product_amount): break;
            
            create_order(order_list,current_customer,product_name,product_amount)
            input(f"{Fore.RED}Please type to continue...{Style.RESET_ALL}")

        #Update customer information
        elif choise == '3':
            name = input("Please enter your name :   ")
            if check_quit(name): break;

            #Get name in correct format
            while not check_name(name) :
                print(f"{Fore.RED}The name you entered is wrong.{Style.RESET_ALL}")
                name = input(" Please enter your name : ")
                if check_quit(name): break;

            surname = input("Please enter your surname :   ")
            if check_quit(surname): break;

            #Get surname in correct format
            while not check_name(surname) :
                print(f"{Fore.RED}The surname you entered is wrong.{Style.RESET_ALL}")
                surname = input(" Please enter your surname : ")
                if check_quit(surname): break;

            phone = input("Please enter your phone :   ")
            if check_quit(phone): break;

            #Get phone number in correct format
            while not check_phone(phone) :
                print(f"{Fore.RED}The phone number you entered is wrong.{Style.RESET_ALL}")
                phone = input(" Please enter your phone number : ")
                if check_quit(phone): break;

            update_customer(customer_list,name,surname,phone,email)
            input(f"{Fore.RED}Please type to continue...{Style.RESET_ALL}")
        
        #Clear email address to start again
        elif choise == '4':
           email = ''

        #Quit
        elif choise == 'q':
           print(f"{Fore.RED}Thank you for reaching us. See you next time {Style.RESET_ALL}")
           break;
        
        #Wrong input for menu
        else:
           print("Wrong choise")
    
    #if customer is not found in the current list => new customer
    else:

        clear_console()
        print("Your e-mail does not found in our customer list.")
        
        name = input("Please enter your name to sign up :   ")
        if check_quit(name): break;

         #Get name in correct format
        while not check_name(name) :
            print(f"{Fore.RED}The name you entered is wrong.{Style.RESET_ALL}")
            name = input(" Please enter your name : ")
            if check_quit(name): break;

        surname = input("Please enter your surname:   ")
        if check_quit(surname): break;

        #Get surname in correct format
        while not check_name(surname) :
            print(f"{Fore.RED}The surname you entered is wrong.{Style.RESET_ALL}")
            surname = input(" Please enter your surname : ")
            if check_quit(surname): break;

        #get phone number in correct format
        phone = input("Please enter your phone :   ")
        while not check_phone(phone) :
            print(f"{Fore.RED}The phone number you entered is wrong.{Style.RESET_ALL}")
            phone = input("Please enter your phone number : ")
            if check_quit(phone): break;

        #Create customer
        new_customer = Customer(name,surname,email,phone)
        customer_list.append(new_customer)

        #Print customer information
        clear_console()
        print(f"{Fore.GREEN}Your account created successfully.{Style.RESET_ALL}")
        print_customer(new_customer)
        
        input(f"{Fore.RED}Please type to continue...{Style.RESET_ALL}")
