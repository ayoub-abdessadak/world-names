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
        "title": "Simulatie (in dit programma wordt een simulatie uitgevoerd voor het populeren van een database)",
        "question": "Maak een keuze: ",
        "action": "call",
        "options": f"1. Simuleren via MySQL\n2. Simuleren via SqlLite",
        "enum": Databases,
        "option_values": {
            "1": "mysql",
            "2": "sqlite",
        },
        "assign": "database",
        "valid": False,
        "next": 3,
    },
    3: {
        "title": "Simulatie Hoofdmenu\n",
        "question": "Kies een database: ",
        "action": "flow",
        "options": f"1. Om opnieuw een simulatie uit te voeren\n2. Om het programma te verlaten",
        "enum": Databases,
        "option_values": {
            "1": 2,
            "2": -1,
        },
        "assign": "database",
        "valid": False,
        "next": 3,
    },
}

