import sqlite3
import os

class DarkoobSQLIT:
    def __init__(self, db_name='name.db', folder_path='databases'):
        db_path = os.path.join(folder_path, db_name)
        os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.folder_path = os.path.abspath(folder_path)

    def create_table(self, table_name='default_table', **columns):
        columns_str = ', '.join([f'{key} {value}' for key, value in columns.items()])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def insert(self, table_name, **data):
        columns_str = ', '.join(data.keys())
        values_str = ', '.join([f'"{value}"' for value in data.values()])
        insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"
        self.cursor.execute(insert_query)
        self.conn.commit()

    def select(self, table_name, **condition):
        condition_str = ' AND '.join([f'{key}="{value}"' for key, value in condition.items()])
        select_query = f"SELECT * FROM {table_name} WHERE {condition_str}"
        self.cursor.execute(select_query)
        return self.cursor.fetchall()

    def update(self, table_name, data, **condition):
        set_str = ', '.join([f'{key}="{value}"' for key, value in data.items()])
        condition_str = ' AND '.join([f'{key}="{value}"' for key, value in condition.items()])
        update_query = f"UPDATE {table_name} SET {set_str} WHERE {condition_str}"
        self.cursor.execute(update_query)
        self.conn.commit()

    def delete(self, table_name, **condition):
        condition_str = ' AND '.join([f'{key}="{value}"' for key, value in condition.items()])
        delete_query = f"DELETE FROM {table_name} WHERE {condition_str}"
        self.cursor.execute(delete_query)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()


