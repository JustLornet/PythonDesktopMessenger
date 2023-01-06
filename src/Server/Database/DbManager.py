import pyodbc
from Database.DbConfig import *
from Server.Database.DbConfig import conn_str


class DbManager:
    def __init__(self):
        self.connection = pyodbc.connect(conn_str)
        self.cursor = self.connection.cursor()

    def set_changes(self, sql_request: str):
        self.cursor.execute(sql_request)
        self.cursor.commit()

    def get_data(self, sql_request: str) -> list:
        self.cursor.execute(sql_request)
        rest_of_rows = self.cursor.fetchall()

        return rest_of_rows
