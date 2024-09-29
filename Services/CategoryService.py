from Models.Category import Category


class CategoryService:
    def __init__(self, category_repository):
        self.selected_category_id = 0
        self.category_repository = category_repository

    def select_category(self, category_id):
        try:
            category = self.category_repository.get_by_id(category_id)
            self.selected_category_id = category_id
            print(f"Category '{category.name}' is selected")
        except Exception as a:
            print("Error: " + a)

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
            print("Error: " + e)

    def remove_category(self, category_id):
        try:
            self.category_repository.delete(category_id)
            print(f"Task with ID {category_id} removed successfully.")
        except Exception as a:
            print("Error: " + a)
