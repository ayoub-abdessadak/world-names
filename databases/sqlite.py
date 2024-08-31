from datetime import datetime
import sqlite3
import sys
sys.path.append("/Users/ayoub/PycharmProjects/HBO-ICT/")
import worldnames
import os
import time
from tabulate import tabulate

class Sqlite:

    def __init__(self, simulation: bool=True):
        self.tables = None
        self.table_name = None
        self.users = None
        self.headers = ["Voornaam", "Achternaam", "Gender", "Leeftijd", "Email"]
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

    def create_table(self, table_name: str="Users"):
        if not isinstance(table_name, str):
            raise BaseException("Table name should be as string")
        query = f"CREATE TABLE {table_name}(first_name, last_name, gender, age, email)"
        self.cursor.execute(query)
        response = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        self.tables = [table[0] for table in response.fetchall()]
        if table_name in self.tables:
            print(f"{table_name} is successvol gemaakt")
            self.table_name = table_name
            return table_name
        else:
            print(f"Het is niet gelukt om de tabel {table_name} te maken.")

    def add_user(self, user: tuple, table_name: str="Users"):
        if not isinstance(table_name, str):
            raise BaseException("Table name should be as string")
        query = f"INSERT INTO {table_name} VALUES {user}"
        self.cursor.execute(query)
        self.con.commit()

    def fill_table(self, table_name: str, amount_of_users: int = 20):
        for _time in range(amount_of_users):
            self.add_user(worldnames.user(), table_name)

    def view_users(self, table_name: str = "Users"):
        os.system("clear")
        print(f"Users for table: {table_name}")
        query = f"SELECT * from {table_name}"
        self.cursor.execute(query)
        res = self.cursor.fetchall()
        self.users = res
        print(tabulate(res,headers=self.headers,tablefmt="fancy_grid"))
        input("Klik op enter om verder te gaan...")

    def search_user(self, search_input: str=None, table_name: str = "Users"):
        os.system("clear")
        print(self)
        search_input = input("Zoek: ") if not search_input else search_input
        fields = ["first_name", "last_name", "gender", "age", "email"]
        search_input = search_input.split()
        results = []
        for field in fields:
            for si in search_input:
                query = f"SELECT * FROM {table_name} WHERE {field} LIKE '%{si}%'"
                self.cursor.execute(query)
                result = self.cursor.fetchall()
                results = [*results, *result]
        print(tabulate(results,headers=self.headers,tablefmt="fancy_grid"))

    def __repr__(self):
        return f"""{tabulate(self.users,headers=self.headers,tablefmt="fancy_grid")}\n"""


