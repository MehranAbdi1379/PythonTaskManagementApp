from typing import List
from Models.Category import Category
from Models.Task import Task
from Repositories.CategoryRepository import CategoryRepository
from Services.TaskService import TaskService


class CategoryService:
    def __init__(
        self, category_repository: CategoryRepository, task_service: TaskService
    ):
        self.selected_category_id = 0
        self.category_repository = category_repository
        self.task_service = task_service

    def select_category(self, category_id):
        try:
            category = self.category_repository.get_by_id(category_id)
            self.selected_category_id = category_id
            print(f"Category '{category.name}' is selected")
        except Exception as a:
            print(a)

    def get_category_by_id(self, category_id):
        return self.category_repository.get_by_id(category_id)

    def show_all_categories(self):
        categories = self.category_repository.get_all()
        for category in categories:
            print(category)
        print()

    def add_category(self, category_name):
        try:
            category = Category(category_name)
            self.category_repository.create(category)
            self.selected_category_id = category.id
            print(
                f"Category '{category_name}' added successfully with ID {category.id}"
            )
        except Exception as e:
            print(e)

    def remove_category(self, category_id):
        try:
            tasks = self.task_service.get_tasks_by_category_id(category_id)
            for task in tasks:
                self.task_service.remove_task(task.id)
            self.category_repository.delete(category_id)
            print(f"Category with ID {category_id} removed successfully.")
        except Exception as a:
            print(a)
