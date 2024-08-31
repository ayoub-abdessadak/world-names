# Module Package for populating random names

import random, json
from .populatinghelpers import email_domains, letters, genders

class WorldNames:

    def __init__(self, file: str = '/Users/ayoub/PycharmProjects/HBO-ICT/worldnames/worldnames.json'):
        __file = open(file)
        names_in_json = __file.readlines()[0]
        self.names = json.loads(names_in_json)
        self.min, self.max = 0, len(self.names)-1
        self.min_gender, self.max_gender = 0, len(genders)-1
        self.min_domain, self.max_domain = 0, len(email_domains)-1

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

    def age(self) -> int:
        return random.randint(0, 120)

    def gender(self) -> str:
        random.shuffle(genders)
        return genders[random.randint(self.min_gender, self.max_gender)]

    def email(self, first_name:str=None, last_name:str=None) -> str:
        random.shuffle(email_domains)
        domain = email_domains[random.randint(self.min_domain, self.max_domain)]
        if not first_name or not last_name:
            return f"{self.first_name()}.{self.last_name()}@{domain}"
        else:
            return f"{first_name}.{last_name}@{domain}"

    def user(self) -> tuple:
        fn, ln = self.first_name(), self.last_name()
        return fn, ln, self.gender(), self.age(), self.email(fn, ln)

world_names = WorldNames()
full_name = world_names.full_name
first_name = world_names.first_name
last_name = world_names.last_name
age = world_names.age
gender = world_names.gender
email = world_names.email
user = world_names.user