# Python imports
from datetime import datetime
import sqlite3, os, sys
sys.path.append("/Users/ayoub/PycharmProjects/HBO-ICT/")
# 3th party imports
from tabulate import tabulate
from worldnames.databases.sqlsharing import SqlShared
from rich.console import Console
from content import logo
from content import custom_print

operating_system = "unix"
clear = "clear" if operating_system == "unix" else "cls"
console = Console()
console.print(logo)

class Sqlite(SqlShared):

    def __init__(self, simulation: bool=True) -> None:
        self.tables = None
        self.table_name = None
        self.users = list()
        if simulation:
            self.database_name = f"temp/SIMDATABASE-{datetime.now().isoformat()}"
            file = open(self.database_name, "w")
            file.close()
        else:
            self.database_name = input("Geef de sqlite.db file op met het volledige pad naar het bestand: ")
        try:
            self.con = sqlite3.connect(self.database_name)
            self.cursor = self.con.cursor()
        except Exception as error:
            custom_print(f"Create a issue for error {error} on github")
            sys.exit()

    def run(self) -> None:
        table_name = "Users"
        super().create_table(self.cursor, table_name, True)
        super().fill_table(self.cursor, self.con, table_name, 20)
        super().view_users(self.cursor, table_name)
        while True:
            os.system("clear")
            console.print(logo)
            custom_print(self)
            _ = super().search_user(self.cursor, None, table_name)
            if _:
                break

    def __repr__(self) -> str:
        return f"""{tabulate(self.users,headers=self.headers,tablefmt="fancy_grid")}\n"""

