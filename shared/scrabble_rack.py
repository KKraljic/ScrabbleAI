from array import array

from config_reader import Config


class ScrabbleRack:
    def __init__(self):
        self.rack = []
        self.size = Config.rack_size()

    def count(self):
        return len(self.rack)

    def count_missing(self):
        return self.size - self.count()

    def add(self, pieces: list[str]):
        self.rack += pieces

    def print(self):
        print(''.join(self.rack))
