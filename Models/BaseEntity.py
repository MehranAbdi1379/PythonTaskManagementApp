from __future__ import annotations
from random import randint


class BaseEntity:
    def __init__(self) -> None:
        self.id = randint(1000, 9999)
