from flask import Flask
import PizzaService

app = Flask(__name__)


if __name__ == '__main__':
    PizzaService.run(Debug=True)
