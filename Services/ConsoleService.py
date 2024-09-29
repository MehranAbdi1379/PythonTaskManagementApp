class ConsoleService:
    def __init__(self) -> None:
        pass

    def print_task_options(self):
        print("*** Task options ***")
        print("1. Show all tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Remove all tasks")

    def print_category_options(self):
        print("*** Category options ***")
        print("5. Select a category")
        print("6. Show all categories")
        print("7. Add a category")
        print("8. Remove a category (Also removes all of the tasks in the category)")

    def print_options(self):
        print()
        print("Options of the application:")
        print()
        self.print_task_options()
        print()
        self.print_category_options()
        print()
        print("9. Quit")
        print()

    def run_selected_option(self, task_service, category_service, selected_option):
        if selected_option == "1":
            task_service.show_all_tasks()
        elif selected_option == "2":
            task_name = input("Please enter the name of task: ")
            task_service.add_task(task_name, category_service.selected_category_id)
        elif selected_option == "3":
            task_id_string = input("Please enter the Id of task: ")
            try:
                task_id = int(task_id_string)
                task_service.remove_task(task_id)
            except ValueError:
                print("Please enter a valid value!!!")
        elif selected_option == "4":
            are_you_sure = input("Are You SURE (yes/no)?")
            if are_you_sure.lower() == "yes":
                task_service.remove_all_tasks()
                print("All tasks are removed!!!")
        elif selected_option == "5":
            category_id_string = input("Please enter the Id of category: ")
            try:
                category_id = int(category_id_string)
                category_service.select_category(category_id)
            except ValueError:
                print("Please enter a valid value!!!")
        elif selected_option == "6":
            category_service.show_all_categories()
        elif selected_option == "7":
            category_name = input("Please enter the name of category: ")
            category_service.add_category(category_name)
        elif selected_option == "8":
            category_id_string = input("Please enter the Id of category: ")
            try:
                category_id = int(category_id_string)
                category_service.remove_category(category_id)
            except ValueError:
                print("please enter a valid value!!!")
        elif selected_option == "9":
            return False
        else:
            print("Please enter a valid option!!!")
        return True
