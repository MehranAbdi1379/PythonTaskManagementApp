from Models.Category import Category


class CategoryService:
    def __init__(self):
        category1 = Category("Work")
        category1.id = 1001
        category2 = Category("Personal")
        category2.id = 1002
        category3 = Category("Shopping")
        category3.id = 1003
        category4 = Category("Fitness")
        category4.id = 1004
        category5 = Category("Hobby")
        category5.id = 1005
        default_category = Category("Default")
        default_category.id = 0
        self.categories = [
            default_category,
            category1,
            category2,
            category3,
            category4,
            category5,
        ]
        self.selected_category_id = 0

    def select_category(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                self.selected_category_id = category_id
                print(f"Category '{category.name}' is selected")
                return
        print(f"No category found with Id {category_id}")

    def show_all_categories(self):
        for category in self.categories:
            print(category)
        print()

    def add_category(self, category_name):
        if category_name == "":
            print("Please enter a valid category name!!!")
            return
        else:
            category = Category(category_name)
            self.categories.append(category)
            self.selected_category_id = category.id
            print(
                f"Category '{category_name}' added successfully with ID {category.id}"
            )

    def remove_category(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                self.categories.remove(category)
                print(f"Task with ID {category_id} removed successfully.")
                return
        print("There is no category with this ID")
