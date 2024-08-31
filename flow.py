# The program itself

import time
from databases import Databases
import os

program = {

    1: {
        "title": "Programma: User Populater WorldNames - Een programma om fictionele gebruikers aan te maken\n",
        "question": "Klik op enter om door te gaan...",
        "action": "",
        "options": f"",
        "enum": None,
        "option_values": {
            "1": "mysql"
        },
        "assign": None,
        "valid": False,
        "next": 2,
    },
    2: {
        "title": "Simulatie of Database\n",
        "question": "Wil je een simulatie runnen of een echte database populeren: ",
        "action": "flow",
        "options": f"1. Simulatie (niks voor nodig)\n2. Database (MySQL DB of Sqlite bestand nodig)",
        "enum": None,
        "option_values": {
            "1":3,
            "2":4
        },
        "assign": None,
        "valid": False,
        "next": 2,
    },
    3: {
        "title": "Simulatie\n",
        "question": "Klik op enter om de simulatie te starten...",
        "action": "call",
        "options": f"",
        "enum": Databases,
        "option_values": {
            "1": "sqlite"
        },
        "assign": "database",
        "valid": False,
        "next": 3,
    },
    4: {
        "title": "Simulatie of Database\n",
        "question": "Klik op enter om door te gaan...",
        "action": "flow",
        "options": f"1. Simulatie (niks voor nodig)\n2. Database (MySQL DB of Sqlite bestand nodig)",
        "enum": Databases,
        "option_values": {
            "1":3,
            "2":4
        },
        "assign": None,
        "valid": False,
        "next": 2,
    },
    10: {
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
    11: {
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

