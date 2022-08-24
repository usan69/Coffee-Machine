class MenuItem:

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:

    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.7),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.6),
            MenuItem(name="cappuccino", water=240, milk=51, coffee=27, cost=3.1),
        ]

    def get_items(self):

        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):

        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")