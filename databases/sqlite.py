from datetime import datetime
import sqlite3
import sys
sys.path.append("/Users/ayoub/PycharmProjects/HBO-ICT/")
import worldnames
import os
import time
from tabulate import tabulate
from worldnames.databases.sqlsharing import SqlShared

class Sqlite(SqlShared):

    def __init__(self, simulation: bool=True):
        self.tables = None
        self.table_name = None
        self.users = None
        if simulation:
            self.database_name = f"SIMDATABASE-{datetime.now().isoformat()}"
            file = open(self.database_name, "w")
            file.close()
        else:
            self.database_name = input("Geef de sqlite.db file op met het volledige pad naar het bestand: ")
        try:
            self.con = sqlite3.connect(self.database_name)
            self.cursor = self.con.cursor()
        except Exception as error:
            print(f"Create a issue for error {error} on github")
            sys.exit()

    def run(self):
        self.c_create_table()
        self.c_fill_table()
        self.c_view_users()
        self.c_search_user()

    def c_create_table(self, table_name: str = "Users"):
        super().create_table(self.cursor, table_name, True)

    def c_add_user(self, user: tuple, table_name: str="Users"):
        super().add_user(user, self.cursor, table_name)

    def c_fill_table(self, table_name: str="Users", amount_of_users: int = 20):
        super().fill_table(self.cursor, self.con, table_name, amount_of_users)

    def c_view_users(self, table_name: str = "Users"):
        super().view_users(self.cursor, table_name)

    def c_search_user(self, search_input: str = None, table_name: str = "Users"):
        while True:
            os.system("clear")
            print(self)
            _ = super().search_user(self.cursor, search_input, table_name)
            if _:
                break

    def __repr__(self):
        return f"""{tabulate(self.users,headers=self.headers,tablefmt="fancy_grid")}\n"""

