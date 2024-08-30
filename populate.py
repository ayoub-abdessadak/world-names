# Some comment about this program

import time
from databases import Databases
import os

program_flow = {
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


class PopulateDatabase:

    def __init__(self):
        self.database = None

    def run_program(self):
        _next = 1
        while True:
            os.system("clear")
            print(self)
            flow = program_flow[_next]
            if flow["valid"]:
                _next = flow["next"]
                continue
            print(flow["title"])
            print(flow["options"])
            choice = input(flow["question"])
            if flow["action"] == "call":
                output = flow['enum'][flow['option_values'][choice.strip()]].value()
                setattr(self, flow['assign'], output)
                flow["valid"] = True
                _next = flow["next"]
            else:
                _next = flow["next"]
                continue

    def __repr__(self):
        return f"""Database: Nothing"""


if __name__ == "__main__":
    pd = PopulateDatabase()
    pd.run_program()
