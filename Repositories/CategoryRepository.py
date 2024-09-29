from Repositories.Repository import Repository
from Repositories.ModelMappings import map_category


class CategoryRepository(Repository):
    def __init__(self, connection_string):
        super().__init__(connection_string, "Categories", map_category)
