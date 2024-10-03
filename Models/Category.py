from __future__ import annotations

from Models.BaseEntity import BaseEntity


class Category(BaseEntity):
    def __init__(self, name: str):
        self.name: str = name
        super().__init__()

    def __repr__(self) -> str:
        return f"Category(ID: {self.id}, Name: '{self.name}')"
