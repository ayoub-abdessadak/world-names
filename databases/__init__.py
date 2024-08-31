from enum import Enum
from .my_sql import MySQL
from .sqlite import Sqlite

class Databases(Enum):
    sqlite = Sqlite
    mysql = MySQL