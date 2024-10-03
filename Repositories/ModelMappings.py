from __future__ import annotations
from Models.Category import Category
from Models.Task import Task


def map_category(row) -> Category:
    category = Category(name=row.name)
    category.id = row.id
    return category


def map_task(row) -> Task:
    task = Task(name=row.name, category_id=row.category_id)
    task.id = row.id
    task.is_done = row.is_done
    return task
