# Some comment about this module

class InvalidDataType(Exception):

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        if self.message:
            return self.message

class OperatorNotSupported(Exception):

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        if self.message:
            return self.message


