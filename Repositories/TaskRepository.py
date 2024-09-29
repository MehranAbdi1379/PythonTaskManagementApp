from Repositories.Repository import Repository
from Repositories.ModelMappings import map_task


class TaskRepository(Repository):
    def __init__(self, connection_string):
        self.table_name = "Tasks"
        super().__init__(connection_string, self.table_name, map_task)

    def get_by_category_id(self, category_id):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM {self.table_name} WHERE category_id = ?"
            cursor.execute(query, (category_id,))
            rows = cursor.fetchall()
            return [self.map_function(row) for row in rows]
