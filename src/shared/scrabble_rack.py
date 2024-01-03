"""
The module hold a class that implements the scrabble racks.
"""

from src.shared.config_reader import Config


class ScrabbleRack:
    """
    Class for representing a rack from a player that holds its tiles.
    """
    def __init__(self):
        self.rack = []
        self.size = Config.rack_size()

    def count(self) -> int:
        """
        Counts how many tiles are left on the rack.
        :return: Number of tiles
        """
        return len(self.rack)

    def count_missing(self) -> int:
        """
        Counts how many tiles are missing on the rack to be full.
        :return: Number of tiles
        """
        return self.size - self.count()

    def add(self, pieces: list[str]) -> None:
        """
        Puts some tile on the rack.
        :param pieces: List of new tiles
        """
        self.rack += pieces

    def print(self):
        """
        Prints the content of the rack to the console.
        """
        print(''.join(self.rack))
