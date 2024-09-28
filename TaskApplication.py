from Services.TaskService import TaskService
from Services.CategoryService import CategoryService
from Services.ConsoleService import ConsoleService

category_service = CategoryService()
task_service = TaskService(category_service)
console_service = ConsoleService()

continue_application = True
option_counter = 5

while continue_application:
    if option_counter % 5 == 0:
        console_service.print_options()

    selected_option = input("Please enter the number of your choice: ")

    continue_application = console_service.run_selected_option(
        task_service, category_service, selected_option
    )

    option_counter += 1

print("Hope you enjoyed using the application")
