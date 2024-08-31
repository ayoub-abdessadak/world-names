# Something

from datetime import datetime
from mysql import connector
from mysql.connector import cursor as _cursor
import sys
sys.path.append("/Users/ayoub/PycharmProjects/HBO-ICT/")
import worldnames
import os
import time
from tabulate import tabulate
from uuid import uuid4


class SqlShared:

    headers = ["Voornaam", "Achternaam", "Gender", "Leeftijd", "Email"]
    users = None

    def create_table(self, cursor:_cursor, table_name: str="Users", lite=True):
        if not isinstance(table_name, str):
            raise BaseException("Table name should be as string")
        query = f"CREATE TABLE {table_name}(first_name CHAR(255), last_name CHAR(255), gender CHAR(255), age INT, email CHAR(255))"
        if not lite:
            print("Tijdelijke database maken...")
            db_name = uuid4().__str__()[0:10].replace("-", '')
            cursor.execute(f"CREATE DATABASE {db_name}")
            cursor.execute(f"USE {db_name};")
            print(f"Database: {db_name} aangemaakt")
        cursor.execute(query)
        if lite:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        else:
            cursor.execute("SHOW TABLES;")
        tables = [table[0] for table in cursor.fetchall()]
        if table_name in tables:
            print(f"{table_name} is successvol gemaakt")
            table_name = table_name
            return table_name
        else:
            print(f"Het is niet gelukt om de tabel {table_name} te maken.")

    def add_user(self, user: tuple, cursor:_cursor, con, table_name: str="Users"):
        if not isinstance(table_name, str):
            raise BaseException("Table name should be as string")
        print(table_name)
        query = f"INSERT INTO {table_name} (first_name, last_name, gender, age, email) VALUES {user}"
        print(query)
        cursor.execute(query)
        con.commit()

    def fill_table(self, cursor:_cursor, con, table_name: str="Users", amount_of_users: int = 20):
        for _time in range(amount_of_users):
            self.add_user(worldnames.user(), cursor, con, table_name)

    def view_users(self, cursor:_cursor, table_name: str = "Users"):
        os.system("clear")
        print(f"Users for table: {table_name}")
        query = f"SELECT * from {table_name}"
        cursor.execute(query)
        res = cursor.fetchall()
        users = res
        self.users = users
        print(tabulate(res,headers=self.headers,tablefmt="fancy_grid"))
        input("Klik op enter om verder te gaan...")

    def search_user(self, cursor:_cursor, search_input: str=None, table_name: str = "Users"):
        print("Typ exit om de zoekfunctie te verlaten\n")
        search_input = input("Zoek: ") if not search_input else search_input
        if search_input.lower().strip() == "exit":
            return "exit"
        fields = ["first_name", "last_name", "gender", "age", "email"]
        search_input = search_input.split()
        results = []
        for field in fields:
            for si in search_input:
                query = f"SELECT * FROM {table_name} WHERE {field} LIKE '%{si}%'"
                cursor.execute(query)
                result = cursor.fetchall()
                results = [*results, *result]
        results = set(results)
        os.system("clear")
        print(f"Gevonden resultaten voor zoekopdracht: {' '.join(search_input)}")
        print(tabulate(results,headers=self.headers,tablefmt="fancy_grid"))
        input("Enter om verder te gaan...")