# The controller acts as the API for the app, in this case it will exist as a terminal based app
# using inputs and if statements to specify what the app should do

# It will run commands from the service file, which in turn uses the DB file to 
# query and create data and will return the data back to the user

import service
import sys
menu = """
    Welcome to the QA Cafe, what would you like to do? 
    1. Create an order
    2. Read an order
    3. Read all Orders
    4. Update an order
    5. Delete an order
    6. Delete all orders
    7. Exit
    """

def startApp():
    print(menu)
    exit = False
    while not exit:
        choice = input("Pick an options from the menu: ")
        if choice == "1":
            print(createOrder())
        if choice == "2":
            print(readOrder())
        if choice == "3":
            print(readAllOrders())
        if choice == "4":
            print(orderUpdate())
        if choice == "5":
            print(orderDelete())
        if choice == "6":
            print(deleteAllOrders())
        if choice == "7":
            confirmUpdate()
            sys.exit("Order Complete :)")


def createOrder():
    customer_name, type_of_drink, size_of_drink, extra_items, price = input("Enter order: name, drink, size, extra_items and price: ").split()
    return service.enterOrder(customer_name, type_of_drink, size_of_drink, extra_items, price)

def readOrder(id):
    return service.readID(id)

def readAllOrders():
    return service.viewAllRecords()

def orderUpdate():
    order_id = input("order_id: ")
    customer_name = input("Customer name: ")
    type_of_drink = input("Drink type: ")
    size_of_drink = input("Drink size: ")
    extra_items = input("Any extra_items: ")
    price = input("Price: ")
    return service.updateOrder(order_id, customer_name, type_of_drink, size_of_drink, extra_items, price)

def orderDelete():
    order_id = input("Order to be deleted: ")
    return service.removeOrder(order_id)

def deleteAllOrders():
    decision = input("Do you want to delete all the orders? Yes or No: ")
    if decision.lower == "yes" or decision.lower == 'y':
        return service.deleteOrders()
    return "No orders deleted."


def confirmUpdate():
    return service.updateDB()

#startApp()
#print(service.viewAllRecords())
