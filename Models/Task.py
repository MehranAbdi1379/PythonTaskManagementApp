from random import randint


class Task:
    def __init__(self, name, category_id):
        self.name = name
        self.id = randint(1000, 9999)
        self.category_id = category_id

    def make_printable_task(self, category_repository):
        category_name = category_repository.get_by_id(self.category_id).name
        return f"Task(ID: {self.id}, Name: '{self.name}', Category: {category_name})"
