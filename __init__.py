import random, string, json

class WorldNames:

    def __init__(self, file: str = '/Users/ayoub/PycharmProjects/HBO-ICT/worldnames/worldnames.json'):
        __file = open(file)
        names_in_json = __file.readlines()[0]
        self.names = json.loads(names_in_json)
        self.min, self.max = 0, len(self.names)-1

    def first_name(self):
        random.shuffle(self.names)
        return self.names[random.randint(self.min, self.max)]

    def last_name(self):
        pass

world_names = WorldNames()
first_name = world_names.first_name
last_name = world_names.last_name