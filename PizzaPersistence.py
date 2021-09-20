import entities.Pizza
import mysql
from mysql.connector import (connection)

cnx = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database='PizzaDB')
cursor = cnx.cursor()

# required methods

def get_all_pizzas():
    query = ("SELECT pizza_name, pizza_price_euros, pizza_price_cents FROM Pizza")
    cursor.execute(query)
    for pizzaEntry in cursor:
        entities.Pizza(pizzaEntry.name, pizzaEntry.pizza_price_euro, pizzaEntry.pizza_price_cents, pizzaEntry.toppings)
    return None

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
