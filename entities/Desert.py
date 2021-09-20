
class Desert:

    def __init__(self, name, cost_euro, cost_cents):
        self.name = name
        self.cost_euro = cost_euro
        self.cost_cents = cost_cents

    def to_JSON(self):
        return {"name": self.name,
                "cost": str(self.cost_euro + "." + self.cost_cents)}
