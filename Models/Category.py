from random import randint


class Category:
    def __init__(self, name: str):
        self.name: str = name
        self.id: int = randint(1000, 9999)

    def __repr__(self) -> str:
        return f"Category(ID: {self.id}, Name: '{self.name}')"
