from Models.Task import Task


class TaskService:
    def __init__(self, category_service):
        self.tasks = []
        self.tasks.append(Task("Complete project report", 1))
        self.tasks.append(Task("Buy groceries", 3))
        self.tasks.append(Task("Morning workout", 4))
        self.tasks.append(Task("Read a book", 5))
        self.tasks.append(Task("Plan weekend trip", 2))
        self.tasks.append(Task("Team meeting", 1))
        self.tasks.append(Task("Pay bills", 3))
        self.tasks.append(Task("Evening run", 4))
        self.tasks.append(Task("Paint a picture", 5))
        self.tasks.append(Task("Client call", 1))
        self.tasks.append(Task("Clean the house", 2))
        self.tasks.append(Task("Order supplies", 3))
        self.tasks.append(Task("Yoga session", 4))
        self.tasks.append(Task("Learn guitar", 5))
        self.tasks.append(Task("Prepare presentation", 1))
        self.tasks.append(Task("Visit the dentist", 2))
        self.tasks.append(Task("Online shopping", 3))
        self.tasks.append(Task("Swim practice", 4))
        self.tasks.append(Task("Write a blog post", 5))
        self.tasks.append(Task("Schedule appointments", 1))
        self.category_service = category_service

    def show_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task.make_printable_task(self.category_service))
        print()

    def add_task(self, task_name, category_id):
        if task_name == "":
            print("The task name is not valid!!!")
        else:
            task = Task(task_name, category_id)
            self.tasks.append(task)
            category_name = ""
            for category in self.category_service.categories:
                if category.id == self.category_service.selected_category_id:
                    category_name = category.name
            print(
                f"Task '{task_name}' added successfully with ID {task.id}, to the category '{category_name}'"
            )

    def remove_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print(f"Task with ID {task_id} removed successfully.")
                return
        print(f"No task found with Id {task_id}")
