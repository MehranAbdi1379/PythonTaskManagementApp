from Repositories.Repository import Repository
from Repositories.ModelMappings import map_task


class TaskRepository(Repository):
    def __init__(self, connection_string):
        super().__init__(connection_string, "Tasks", map_task)
