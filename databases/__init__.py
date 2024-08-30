from enum import Enum
from .my_sql import MySQL

class Databases(Enum):
    sqlite = None
    mysql = MySQL