from random import randint


class Category:
    def __init__(self, name):
        self.name = name
        self.id = randint(1000, 9999)

    def __repr__(self):
        return f"Category(ID: {self.id}, Name: '{self.name}')"
