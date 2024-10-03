from __future__ import annotations
from Models.BaseEntity import BaseEntity


class Task(BaseEntity):
    def __init__(self, name: str, category_id: int):
        self.name: str = name
        self.category_id: int = category_id
        self.is_done: bool = False
        super().__init__()

    def make_printable_task(self, category_repository):
        category_name = category_repository.get_by_id(self.category_id).name
        done = ""
        if self.is_done:
            done = "Yes"
        else:
            done = "No"
        return f"Task(ID: {self.id}, Name: '{self.name}', Category: {category_name}, Done: {done})"
