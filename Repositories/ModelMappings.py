from Models.Category import Category
from Models.Task import Task


def map_category(row):
    category = Category(name=row.name)
    category.id = row.id
    return category


def map_task(row):
    task = Task(name=row.name, category_id=row.category_id)
    task.id = row.id
    return task
