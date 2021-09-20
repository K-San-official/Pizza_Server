from flask import jsonify

class Pizza:

    name = str
    cost_euro = int
    cost_cents = int
    toppings = []

    def __init__(self, name, cost_euro, cost_cents, toppings):
        self.name = name
        self.cost_euro = cost_euro
        self.cost_cents = cost_cents
        self.toppings = toppings

    def to_JSON(self):
        return {"name":str(self.name),
                "toppings":str(self.toppings),
                "price":str(self.cost_euro + '.' + self.cost_cents)}
