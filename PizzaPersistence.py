import mysql
from mysql.connector import (connection)

cnx = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database='PizzaDB')
cnx.close()

# required methods

def get_all_pizzas():
    query = ("SELECT pizza_name FROM Pizza ")
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
