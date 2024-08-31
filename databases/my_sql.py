# Some comment about the application

from mysql import connector
from mysql.connector import errorcode
import time
import os
import sys
import sys
sys.path.append("/Users/ayoub/PycharmProjects/HBO-ICT/")
from worldnames.databases.sqlsharing import SqlShared
from tabulate import tabulate

operating_system = "unix"
clear = "clear" if operating_system == "unix" else "cls"


class MySQL(SqlShared):
    """

        c_ = custom methods for overridden methods in SqlShared

    """
    def __init__(self):
        self.connected = False
        self.users = None
        self.databases = None
        self.validators = {
            'user_name': False,
            'password': False,
            'host': False,
            'port': False
        }
        self.connection_attempt = False
        while True:
            os.system(clear)
            print("Om een verbinding te kunnen maken met jouw MySQL database. Dien je de volgende informatie in te vullen: \n")
            if True in self.validators.values():
                print(self)
            if not self.validators['user_name']:
                self.user_name = input("Gebruikersnaam: ").strip()
                self.validators['user_name'] = True
            if not self.validators['password']:
                self.password = input("Wachtwoord: ").strip()
                self.validators['password'] = True
            if not self.validators['host']:
                self.host = input("Host: ").strip()
                self.validators['host'] = True
            if not self.validators['port']:
                self.port = input("Poort: ").strip()
                self.validators['port'] = True
            try:
                print("\nVerbinding maken met MySQL...")
                self.cnx = self.connect()
            except connector.Error as error:
                if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Password or username is invalid!")
                    self.validators['user_name'] = False
                    self.validators['password'] = False
                    time.sleep(2)
                    continue
                elif error.errno == errorcode.CR_UNKNOWN_HOST or errorcode.ER_BAD_HOST_ERROR:
                    print(f"Host {self.host} is invalid!")
                    self.validators['host'] = False
                    time.sleep(2)
                    continue
                elif error.errno == errorcode.CR_CONN_HOST_ERROR or error.errno == -1:
                    print(f"Host {self.host} or port {self.port} is invalid!")
                    self.validators['port'] = False
                    self.validators['host'] = False
                    time.sleep(2)
                    continue
                else:
                    print("Something went wrong, create a ISSUE on: https://github.com/ayoub-abdessadak/worldnames/issues")
                    print(f"ERROR: {error.errno}, {error.msg}, {error}, {error.sqlstate}")
                    sys.exit()
            else:
                print("Verbinding successvol")
                self.connection_attempt = True
                self.disconnect()
                return

    def connect(self):
        self.connected = True
        return connector.connect(user=self.user_name, password=self.password, host=self.host, port=self.port)

    def disconnect(self):
        self.connected = False
        self.cnx.close()

    def get_cursor(self):
        if not self.connected:
            self.cnx = self.connect()
        return self.cnx.cursor(buffered=True)

    def get_databases(self):
        if self.databases:
            return self.databases
        else:
            cursor = self.get_cursor()
            cursor.execute("SHOW DATABASES;")
            result = cursor.fetchall()
            self.databases = [database[0] for database in result]
            self.disconnect()

    def run(self):
        self.c_create_table()
        self.c_fill_table()
        self.c_view_users()
        self.c_search_user()

    def c_create_table(self, table_name: str = "Users"):
        super().create_table(self.get_cursor(), table_name, False)

    def c_add_user(self, user: tuple, table_name: str="Users"):
        super().add_user(user, self.get_cursor(), table_name)

    def c_fill_table(self, table_name: str="Users", amount_of_users: int = 20):
        super().fill_table(self.get_cursor(), self.cnx, table_name, amount_of_users)

    def c_view_users(self, table_name: str = "Users"):
        super().view_users(self.get_cursor(), table_name)

    def c_search_user(self, search_input: str = None, table_name: str = "Users"):
        while True:
            os.system("clear")
            print(self)
            _ = super().search_user(self.get_cursor(), search_input, table_name)
            if _:
                break

    def __repr__(self):
        return f"""{tabulate(self.users, headers=self.headers, tablefmt="fancy_grid")}\n"""
