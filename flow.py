# The program itself

from databases import Databases
from colorama import Fore

program = {
    1: {
        "title": "User Populater WorldNames - Een programma om fictieve gebruikers aan te maken",
        "question": "Klik op enter om door te gaan...",
        "action": "",
        "options": f"",
        "enum": None,
        "option_values": None,
        "next": 2,
        "color":Fore.GREEN,
    },
    2: {
        "title": "Simulatie (in dit programma wordt een simulatie uitgevoerd voor het populeren van een database)\n",
        "question": "\nMaak een keuze: ",
        "action": "call",
        "options": f"1. Simuleren via MySQL\n2. Simuleren via SqlLite",
        "enum": Databases,
        "option_values": {
            "1": "mysql",
            "2": "sqlite",
        },
        "next": 3,
        "color":Fore.GREEN,
    },
    3: {
        "title": "WorldNames Hoofdmenu\n",
        "question": "\nKies een database: ",
        "action": "flow",
        "options": f"1. Om opnieuw een simulatie uit te voeren\n2. Om het programma te verlaten",
        "enum": None,
        "option_values": {
            "1": 2,
            "2": -1,
        },
        "next": 3,
        "color":Fore.GREEN,
    },
}

