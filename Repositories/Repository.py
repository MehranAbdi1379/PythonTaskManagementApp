from __future__ import annotations
from typing import List
import pyodbc

from Models.BaseEntity import BaseEntity


class Repository:
    def __init__(self, connection_string: str, table_name: str, map_function):
        self.connection_string = connection_string
        self.table_name = table_name
        self.map_function = map_function

    def get_connection(self):
        return pyodbc.connect(self.connection_string)

    def create(self, obj: BaseEntity):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            columns = ", ".join(obj.__dict__.keys())
            values = ", ".join(f"'{v}'" for v in obj.__dict__.values())
            query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({values})"
            cursor.execute(query)
            conn.commit()

    def get_by_id(self, obj_id: int) -> BaseEntity:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM {self.table_name} WHERE ID = ?"
            cursor.execute(query, (obj_id,))
            row = cursor.fetchone()
            return self.map_function(row) if row else None

    def update(self, obj_id: int, obj: BaseEntity):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            set_clause = ", ".join(f"{k} = '{v}'" for k, v in obj.__dict__.items())
            query = f"UPDATE {self.table_name} SET {set_clause} WHERE ID = ?"
            cursor.execute(query, (obj_id,))
            conn.commit()

    def delete(self, obj_id: int):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = f"DELETE FROM {self.table_name} WHERE ID = ?"
            cursor.execute(query, (obj_id,))
            conn.commit()

    def get_all(self) -> List[BaseEntity]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [self.map_function(row) for row in rows]
