# Some comment about this program

import time
from databases import Databases
import os
from flow import program
import sys
from rich.console import Console
from content import logo, icon

console = Console()

class PopulateDatabase:

    def __init__(self) -> None:
        self.database = None
        self.showed_icon = False

    def run_program(self, program_flow) -> None:
        _next = 1
        while True:
            if _next == -1:
                print("Doei :)")
                sys.exit()

            flow = program_flow[_next]
            os.system("clear")
            console.print(self.__logo())
            print(flow["color"] + f'''\n{flow["title"]}\n{flow["options"]}''')
            choice = input(flow["question"])

            if flow["action"] == "call":
                try:
                    output = flow['enum'][flow['option_values'][choice.strip()]].value()
                    output.run()
                    _next = flow["next"]
                    continue
                except KeyError:
                    print("De opgegeven keuze is ongeldig.")
                    time.sleep(2)
                    continue
                except Exception as error:
                    print(f"Something went wrong, make a issue on GIT, for {error}")
                    sys.exit()

            if flow["action"] == "flow":
                try:
                    _next = flow["option_values"][choice.strip()]
                    continue
                except KeyError:
                    print("De opgegeven keuze is ongeldig.")
                    time.sleep(2)
                    continue
                except Exception as error:
                    print(f"Something went wrong, make a issue on GIT, for {error}")
                    sys.exit()

            if not flow["action"]:
                _next = flow["next"]
                continue

    def __logo(self) -> None:
        if not self.showed_icon:
            self.showed_icon = True
            return logo + icon
        else:
            return logo


if __name__ == "__main__":
    pd = PopulateDatabase()
    pd.run_program(program)
