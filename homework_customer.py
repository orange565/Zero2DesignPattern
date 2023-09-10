from datetime import datetime
import re
import os

class Customer:
  def __init__(self, name, surname, email, phone):
    self.name = name
    self.surname = surname
    self.email = email
    self.phone = phone

class Order:
  def __init__(self, customer, product, amount, date):
    self.customer = customer
    self.product = product
    self.amount = amount
    self.date = date


def clear_console():
    clear = lambda: os.system('clear')
    clear()


# Define a function for
# for validating an Email
def check_email(email):
    # Make a regular expression
    # for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        return True
 
    else:
        return False

def is_customer(customer_list, email_address):
    for customer in customer_list:
      if(customer.email == email_address):
        return customer
    return False

def check_quit(input):
   return(True if input == 'q' else False)

def get_customer_orders(orders,email):
   order_list = []
   for order in orders:
      if order.customer.email == email:
         order_list.append(order)
   return order_list

def print_orders(orders):
   clear_console()
   print ("Your order list: ")
   for order in orders:
      print(order.product + " " + str(order.amount) + " " + str(order.date))

def create_order(order_list,customer,product_name,product_amount):
    new_order = Order(customer,product_name, product_amount,datetime.now())
    order_list.append(new_order)
    print("Your order created successfully. You can see all your orders below")
    orders = get_customer_orders(order_list,customer.email)
    print_orders(orders)

def update_customer(customer_list,name,surname,phone,email):
   for customer in customer_list:
      if customer.email == email:
        customer.name = name
        customer.surname = surname
        customer.phone = phone

        clear_console()
        print("Your account updated successfully")
        print("Name = " + customer.name)
        print("Surname = " + customer.surname)
        print("Phone = " + customer.phone)
        print("E-mail = " + customer.email)


   
clear_console()
print("Please enter q to quit")
quit = ''
customer_list = []
order_list =[]
customer1 = Customer("Fatih","Subaşı","f@f.com","05336531615")
order1 = Order(customer1,"p1",5, datetime.now())
customer_list.append(customer1)
order_list.append(order1)
email = ''

while quit != 'q':
    if email == '':
        email = input("Welcome to MD Customer Services. Please enter your e-mail address: ")
        if check_quit(email): break;
    
    while not check_email(email) :
        email = input("The e-mail address you entered is wrong. Please enter your e-mail address: ")
        if check_quit(email): break;
    
    current_customer = is_customer(customer_list,email)
    if current_customer:
        print("Welcome "+ current_customer.name +" " +current_customer.surname + " " + current_customer.phone)
        print("What do you want to do today?")
        print("Press 1 to see your orders")
        print("Press 2 to create a new order")
        print("Press 3 to edit your account")
        print("Press 4 to use different account")
        choise = input()
        if choise == '1':
           print("Your ourders")
           orders = get_customer_orders(order_list,email)
           print_orders(orders)
        elif choise == '2':
            print("New order")
            product_name = input("Please enter product name")
            product_amount = input("Please enter product name")
            create_order(order_list,current_customer,product_name,product_amount)
        elif choise == '3':
            name = input("Please enter your name:")
            if check_quit(name): break;

            surname = input("Please enter your surname:")
            if check_quit(surname): break;

            phone = input("Please enter your phone:")
            if check_quit(phone): break;
            update_customer(customer_list,name,surname,phone,email)
        elif choise == '4':
           email = ''
        else:
           print("Wrong choise")
           break;
    else:
        name = input("You are not our customer. You need to sign up first. Please enter your name:")
        if check_quit(name): break;

        surname = input("Please enter your surname:")
        if check_quit(surname): break;

        phone = input("Please enter your phone:")
        if check_quit(phone): break;

        new_customer = Customer(name,surname,email,phone)
        customer_list.append(new_customer)

        print("Your account created successfully")
    #for customer in customer_list:
    #    print("Customer = " + customer.name + " " + customer.surname + " " + customer.email + " " + customer.phone)