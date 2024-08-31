import random, string, json

letters = [letter for letter in string.ascii_lowercase]
class WorldNames:

    def __init__(self, file: str = '/Users/ayoub/PycharmProjects/HBO-ICT/worldnames/worldnames.json'):
        __file = open(file)
        names_in_json = __file.readlines()[0]
        self.names = json.loads(names_in_json)
        self.min, self.max = 0, len(self.names)-1

    def full_name(self) -> str:
        return f"{self.first_name()} {self.last_name()}"

    def first_name(self) -> str:
        random.shuffle(self.names)
        return self.names[random.randint(self.min, self.max)]

    def last_name(self) -> str:
        _max = random.randint(3, 12)
        random.shuffle(letters)
        _last_name = "".join(letters[0:_max])
        return f"{_last_name[0].upper()}{_last_name[1::].lower()}"

world_names = WorldNames()
full_name = world_names.full_name
first_name = world_names.first_name
last_name = world_names.last_name