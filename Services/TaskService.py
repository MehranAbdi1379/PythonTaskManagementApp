from Models.Task import Task


class TaskService:
    def __init__(self, category_repository, task_repository):
        self.category_repository = category_repository
        self.task_repository = task_repository

    def show_all_tasks(self):
        if not self.task_repository.get_all():
            print("No tasks available.")
        else:
            for task in self.task_repository.get_all():
                print(task.make_printable_task(self.category_repository))
        print()

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

    def remove_task(self, task_id):
        try:
            self.task_repository.delete(task_id)
            print(f"Task with ID {task_id} removed successfully.")
        except Exception as a:
            print("Error: " + a)
