# Some comment about this program

import time
from databases import Databases
import os
from flow import program

class PopulateDatabase:

    def __init__(self):
        self.database = None

    def run_program(self, program_flow):
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
    pd.run_program(program)
