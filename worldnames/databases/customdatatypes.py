# Some comment about this module

# Python imports
import numbers

# Worldnames imports
import worldnames
from worldnames.exceptions import InvalidDataType, OperatorNotSupported

class User:

    def __init__(self, _first_name: str, _last_name: str, gender: str, age: int, email: str):
        """

        :param _first_name:
        :param _last_name:
        :param age:
        :param gender:
        :param email:
        """
        self.users = set()
        self.first_name = _first_name
        self.last_name = _last_name
        self.gender = gender
        self.age = age
        self.email = email
        self.users.add(self)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Name: {self.first_name} {self.last_name} | gender: {self.gender} | age: {self.age} | email: {self.email}"

    # Arithmetic operators
    def __add__(self, other) -> set:
        """
        Supports adding for type User

        :param other:
        :return:
        """
        if not isinstance(other, User):
            raise InvalidDataType(f"{other} should be an instance of User not {type(other)}")
        else:
            self.users.add(other)
            return self.users

    def __sub__(self, other) -> set:
        """
        Supports subtraction by User.

        :param other:
        :return:
        """
        if not isinstance(other, User):
            raise InvalidDataType(f"{other} should be an instance of User not {type(other)}")
        else:
            self.users.remove(other)
            return self.users

    def __mul__(self, other) -> list:
        """
        Supports multiplication by number or User.

        :param other:
        :return:
        """
        if not isinstance(other, User) and not isinstance(other, numbers.Real):
            raise InvalidDataType(f"{other} should be an instance of User or Number not {type(other)}")
        else:
            return list(set) * other.age if isinstance(other, User) else other

    def __truediv__(self, other) -> OperatorNotSupported:
        """
        Does not support true division

        :param other:
        :return:
        """
        raise OperatorNotSupported("Division is not supported for User")

    def __floordiv__(self, other) -> OperatorNotSupported:
        """
        Does not support floor division
        :param other:
        :return:
        """
        raise OperatorNotSupported("Floor division is not supported for User")

    def __mod__(self, other) -> OperatorNotSupported:
        """
        Does not support mod

        :param other:
        :return:
        """
        raise OperatorNotSupported("Modulus is not supported for User")

    def __pow__(self, *args, **kwargs) -> set:
        """
        Possible to pow a User object

        :param power:
        :param modulo:
        :return:
        """
        raise OperatorNotSupported("The power of User is not supported")

    # Rich comparisons
    def __eq__(self, other) -> bool:
        """
        Supports comparison for integers and user type
        :param other:
        :return: bool
        """
        if not isinstance(other, User):
            raise InvalidDataType(f"{other} should be an instance of User not {type(other)}")
        else:
            return hash(self) == hash(other)

    def __lt__(self, other) -> bool:
        """
        Supports comparison for integers and user type
        :param other:
        :return: bool
        """
        if not isinstance(other, User) and not isinstance(other, numbers.Real):
            raise InvalidDataType(f"{other} should be an instance of User or Number not {type(other)}")
        else:
            return bool(self.age < other.age if isinstance(other, User) else other)

    def __le__(self, other) -> bool:
        """
        Supports comparison for integers and user type
        :param other:
        :return: bool
        """
        if not isinstance(other, User) and not isinstance(other, numbers.Real):
            raise InvalidDataType(f"{other} should be an instance of User or Number not {type(other)}")
        else:
            return bool(self.age <= other.age if isinstance(other, User) else other)

    def __ge__(self, other) -> bool:
        """
        Supports comparison for integers and user type
        :param other:
        :return: bool
        """
        if not isinstance(other, User) and not isinstance(other, numbers.Real):
            raise InvalidDataType(f"{other} should be an instance of User or Number not {type(other)}")
        else:
            return bool(self.age >= other.age if isinstance(other, User) else other)

    def __gt__(self, other) -> bool:
        """
        Supports comparison for integers and user type
        :param other:
        :return: bool
        """
        if not isinstance(other, User) and not isinstance(other, numbers.Real):
            raise InvalidDataType(f"{other} should be an instance of User or Number not {type(other)}")
        else:
            return bool(self.age > other.age if isinstance(other, User) else other)

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.gender, self.age, self.email))