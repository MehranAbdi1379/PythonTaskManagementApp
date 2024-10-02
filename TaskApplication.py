from Repositories.CategoryRepository import CategoryRepository
from Repositories.TaskRepository import TaskRepository
from Services.TaskService import TaskService
from Services.CategoryService import CategoryService
from Services.ConsoleService import ConsoleService
from DataBase import DataBase

connection_string = DataBase.get_connection_string()

category_repository = CategoryRepository(connection_string)
task_repository = TaskRepository(connection_string)

task_service = TaskService(category_repository, task_repository)
category_service = CategoryService(category_repository, task_service)
console_service = ConsoleService()

continue_application = True

while continue_application:
    console_service.print_options()

    selected_option = input("Please enter the number of your choice: ")

    continue_application = console_service.run_selected_category_of_options(
        task_service, category_service, selected_option
    )

print("Hope you enjoyed using the application")
