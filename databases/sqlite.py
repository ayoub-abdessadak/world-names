from datetime import datetime
import sqlite3
import sys
import worldnames


class Sqlite:

    def __init__(self, simulation: bool=True):
        self.tables = None
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

    def create_table(self, table_name: str):
        if not isinstance(table_name, str):
            raise BaseException("Table name should be as string")
        query = f"CREATE TABLE {table_name}(first_name, last_name, gender, age, email)"
        self.cursor.execute(query)
        response = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        self.tables = [table[0] for table in response.fetchall()]
        if table_name in self.tables:
            print(f"{table_name} is successvol gemaakt")
        else:
            print(f"Het is niet gelukt om table {table_name} te maken.")

    def add_user(self, table_name: str, user: tuple):
        if not isinstance(table_name, str):
            raise BaseException("Table name should be as string")
        query = f"INSERT INTO {table_name} VALUES {user}"
        self.cursor.execute(query)
        self.con.commit()

    def fill_table(self, amount_of_users: int = 100, table_name: str):
        for time in range(amount_of_users):
            self.add_user(table_name, worldnames.user)

    def view_users(self):
        pass

    def search_user(self):
        pass

