from entities.Pizza import Pizza
from entities.Desert import Desert
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
cursor = cnx.cursor()

# required methods

def get_all_pizzas():
    query = ("SELECT pizza_name, pizza_price_euros, pizza_price_cents FROM Pizza;")  # need to add join for toppings
    cursor.execute(query)
    AllPizzas = []
    for (pizza_name, pizza_price_euros, pizza_price_cents) in cursor:
        AllPizzas.append(Pizza(pizza_name, pizza_price_euros, pizza_price_cents, []))  # add toppings
    return AllPizzas

def get_all_desserts():
    query = ("SELECT dessert_name, dessert_price_euros, dessert_price_cents FROM Dessert;")  # need to add join for toppings
    cursor.execute(query)
    AllDesserts = []
    for (dessert_name, dessert_price_euros, dessert_price_cents) in cursor:
        AllDesserts.append(Drink(dessert_name, dessert_price_euros, dessert_price_cents))  # add toppings
    return AllDesserts

def get_all_drinks():
    query = ("SELECT drink_name, drink_price_euros, drink_price_cents FROM Drink;")  # need to add join for toppings
    cursor.execute(query)
    AllDrinks = []
    for (drink_name, drink_price_euros, drink_price_cents) in cursor:
        AllDrinks.append(Drink(drink_name, drink_price_euros, drink_price_cents))  # add toppings
    return AllDrinks

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

# Main function to test query methods
if __name__ == '__main__':
    for pizza in get_all_pizzas():
        print(pizza.name)

    print("---")

    for drink in get_all_drinks():
        print(drink.name)

    print("---")

    for dessert in get_all_desserts():
        print(dessert.name)


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
