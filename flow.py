# The program itself

import time
from databases import Databases
import os

program = {
    1: {
        "title": "DATABASE\n",
        "question": "Kies een database: ",
        "action": "call",
        "options": f"1. MySQL",
        "enum": Databases,
        "option_values": {
            "1": "mysql"
        },
        "assign": "database",
        "valid": False,
        "next": 3,
    },
    3: {
            "title": "DATABASE\n",
            "question": "Kies een database: ",
            "action": "call",
            "options": f"1. MySQL",
            "enum": Databases,
            "option_values": {
                "1": "mysql"
            },
            "assign": "database",
            "valid": False,
            "next": 3,
    }
}

# 1. Introduction to the program, pressing enter will start it
# 2. Keuze om een simulatie te runnen (bijv geen mysql of niet technisch)
# 3. keuze om mysql of sqlite zelf te runnen in flow

## De simulatie
# 1. Creer een sqlite database
# 2. Creer een tabel
# 3. tabel vullen met fictionele gebruikers
# 4. Hoofdmenu met keuze: 1.gebruikers bekijken of 2. gebruike opzoeken obv naam

## Eigen flow (SQL)
# 1. Verbinden met mysql
# 2. Database kiezen
# 3. Tabel maken
# 4. Gebruikers aanmaken

## Eigen flow (SQL)
# 1. Verbinden met mysql
# 2. Database kiezen
# 3. Tabel maken
# 4. Gebruikers aanmaken

