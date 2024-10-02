class ConsoleService:
    def __init__(self) -> None:
        pass

    def print_task_options(self):
        print("*** Task options ***")
        print("1. Show all tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Remove all tasks")
        print("5. Show all undone tasks")
        print("6. Show all done tasks")
        print("7. Make a task done")
        print("8. Remove all done tasks")
        print("9. Remove all undone tasks")
        print("10. Show tasks of the selected category")
        print("*. Go Back")

    def print_category_options(self):
        print("*** Category options ***")
        print("1. Select a category")
        print("2. Show all categories")
        print("3. Add a category")
        print("4. Remove a category (Also removes all of the tasks in the category)")
        print("5. Show selected category")
        print("*. Go Back")

    def print_options(self):
        print()
        print("Options of the application:")
        print()
        print("1. Task options")
        print("2. Category options")
        print()
        print("*. Quit")
        print()

    def run_selected_category_option(
        self,
        task_service,
        category_service,
        selected_option,
    ):
        if selected_option == "1":
            category_id_string = input("Please enter the Id of category: ")
            try:
                category_id = int(category_id_string)
                category_service.select_category(category_id)
            except ValueError:
                print("Please enter a valid value!!!")
        elif selected_option == "2":
            category_service.show_all_categories()
        elif selected_option == "3":
            category_name = input("Please enter the name of category: ")
            category_service.add_category(category_name)
        elif selected_option == "4":
            category_id_string = input("Please enter the Id of category: ")
            try:
                category_id = int(category_id_string)
                category_service.remove_category(category_id)
            except ValueError:
                print("please enter a valid value!!!")
        elif selected_option == "5":
            try:
                category = category_service.get_category_by_id(
                    category_service.selected_category_id
                )
                print(
                    f"Selected category is '{category.name}' with Id of '{category.id}'"
                )
            except Exception as e:
                print(e)
        elif selected_option == "*":
            return False
        else:
            print("Please enter a valid option!!!")
        return True

    def run_selected_task_option(
        self,
        task_service,
        category_service,
        selected_option,
    ):
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
        # elif selected_option == '5':
        # write code
        # elif selected_option == '6':
        # write code
        # elif selected_option == '7':
        # write code
        # elif selected_option == '8':
        # write code
        # elif selected_option == '9':
        # write code
        # elif selected_option == '10':
        # write code
        elif selected_option == "*":
            return False
        else:
            print("Please enter a valid option!!!")
        return True

    def run_selected_category_of_options(
        self, task_service, category_service, selected_option
    ):
        continue_with_options = True
        if selected_option == "1":
            while continue_with_options:
                self.print_task_options()
                second_selected_option = input(
                    "Please enter the number of your choice: "
                )
                continue_with_options = self.run_selected_task_option(
                    task_service, category_service, second_selected_option
                )
        elif selected_option == "2":
            while continue_with_options:
                self.print_category_options()
                second_selected_option = input(
                    "Please enter the number of your choice: "
                )
                continue_with_options = self.run_selected_category_option(
                    task_service,
                    category_service,
                    second_selected_option,
                )
        elif selected_option == "*":
            return False
        else:
            print("Please enter a valid option!!!")
        return True
