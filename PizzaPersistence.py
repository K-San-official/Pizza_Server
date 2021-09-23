from entities.Pizza import Pizza
from entities.Drink import Drink
import mysql
from mysql.connector import (connection)

import mysql.connector

config = {
  'user': 'root',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'pizzas',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

# required methods

def get_all_pizzas():
    cursor = cnx.cursor()
    query = ("SELECT pizza_name, pizza_price_euros, pizza_price_cents FROM Pizza;")  # need to add join for toppings
    cursor.execute(query)
    AllPizzas = []
    for (pizza_name, pizza_price_euros, pizza_price_cents) in cursor:
        AllPizzas.append(Pizza(pizza_name, pizza_price_euros, pizza_price_cents, []))  # add toppings
    cursor.close()
    return AllPizzas

def get_all_desserts():
    return None

def get_all_drinks():
    return None

def create_purchase(Purchase):
    return None

def create_customer(Customer):
    return None

def get_customer_address(Customer):
    return None

def get_purchase(purchase_id):
    return None

def get_delivery_driver(purchase_id):
    return None

def testGet():
    print("Test")
    cursor = cnx.cursor()
    query = ("SELECT pizza_name, pizza_price_euros, pizza_price_cents FROM Pizza;")
    cursor.execute(query)
    for (pizza_name, pizza_price_euros, pizza_price_cents) in cursor:
        print(pizza_name, pizza_price_euros, pizza_price_cents)
    cursor.close()


# Main function to test query methods
if __name__ == '__main__':
    x = get_all_pizzas()
    for pizza in x:
        print(pizza.name)



"""
- get_all_pizzas() -> Pizza[]
- get_all_desserts() -> Desert[]
- get_all_drinks() -> Drink[]
- create_purchase(Purchase) -> 200
- create_customer(Customer) -> 200
- get_customer_address(Customer) -> 200
- get_purchase(purchase_id) -> Purchase
- get_delivery_driver(purchase_id) -> DeliveryDriver

Classes:

Pizza
Dessert
Drink
Customer
Purchase
DeliveryDriver
Address



"""
