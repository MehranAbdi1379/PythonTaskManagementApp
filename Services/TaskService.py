from __future__ import annotations
from typing import List
from Models.Task import Task
from Repositories.CategoryRepository import CategoryRepository
from Repositories.TaskRepository import TaskRepository


class TaskService:
    def __init__(self, category_repository, task_repository):
        self.category_repository: CategoryRepository = category_repository
        self.task_repository: TaskRepository = task_repository

    def show_all_tasks(self):
        if not self.task_repository.get_all():
            print("No tasks available.")
        else:
            for task in self.task_repository.get_all():
                print(task.make_printable_task(self.category_repository))
        print()

    def show_all_done_tasks(self):
        if not self.task_repository.get_all_done_tasks():
            print("No done tasks available.")
        else:
            for task in self.task_repository.get_all_done_tasks():
                print(task.make_printable_task(self.category_repository))
        print()

    def show_all_undone_tasks(self):
        if not self.task_repository.get_all_undone_tasks():
            print("No undone tasks available.")
        else:
            for task in self.task_repository.get_all_undone_tasks():
                print(task.make_printable_task(self.category_repository))
        print()

    def remove_all_tasks(self):
        try:
            for task in self.task_repository.get_all():
                self.task_repository.delete(task.id)
        except Exception as e:
            print(e)

    def remove_all_done_tasks(self):
        try:
            for task in self.task_repository.get_all():
                if task.is_done == True:
                    self.task_repository.delete(task.id)
        except Exception as e:
            print(e)

    def remove_all_undone_tasks(self):
        try:
            for task in self.task_repository.get_all():
                if task.is_done == False:
                    self.task_repository.delete(task.id)
        except Exception as e:
            print(e)

    def get_task_by_id(self, task_id: int) -> Task:
        try:
            task = self.task_repository.get_by_id(task_id)
            return task
        except Exception as e:
            print(e)

    def make_task_done(self, task_id: int):
        try:
            task = self.task_repository.get_by_id(task_id)
            task.is_done = True
            self.task_repository.update(task.id, task)
            task = self.get_task_by_id(task_id)
            print(f"Task '{task.name}' with the Id of '{task.id}' is done")
        except Exception as e:
            print(e)

    def show_tasks_by_category_id(self, category_id: int):
        try:
            for task in self.get_tasks_by_category_id(category_id):
                print(task.make_printable_task(self.category_repository))
        except Exception as e:
            print(e)

    def get_tasks_by_category_id(self, category_id: int) -> List[Task]:
        return self.task_repository.get_by_category_id(category_id)

    def add_task(self, task_name, category_id):
        try:
            task = Task(task_name, category_id)
            self.task_repository.create(task)
            category_name = self.category_repository.get_by_id(category_id).name
            print(
                f"Task '{task_name}' added successfully with ID {task.id}, to the category '{category_name}'"
            )
        except Exception as a:
            print(a)

    def get_all_tasks(self) -> List[Task]:
        return self.task_repository.get_all()

    def remove_task(self, task_id: int):
        try:
            self.task_repository.delete(task_id)
            print(f"Task with ID {task_id} removed successfully.")
        except Exception as a:
            print(a)
