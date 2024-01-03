"""
Module that holds the representation of the bag, that holds all the tiles.
"""

import json
import random
from dataclasses import dataclass
from src.shared.config_reader import Config


class ScrabbleBag:
    """
    Class for representing the bag, that holds all tiles.
    Can be used to draw new tiles.
    """
    def __init__(self, seed=0):
        if seed != 0:
            random.seed(seed)
        self._fill_bag()

    def _fill_bag(self) -> None:
        """
        Initializes the scrabble bag.
        """
        with open(Config.bag_config_path(), 'r', encoding='utf-8') as file:
            content = json.loads(file.read())

        self.bag: dict[str, TileInfo] = {element['letter']: TileInfo(
                element['letter'], element['count'], element['value']
            ) for element in content}

        self.tile_string = self._create_tile_string()

    def _create_tile_string(self) -> list[str]:
        """
        Creates the content of the back and sets a random order in which the tiles will be drawn.
        :return: A list of the tiles in the back.
        """
        tile_string = ''.join([tile.letter * tile.count for tile in self.bag.values()])
        tile_string_list = list(tile_string)
        random.shuffle(tile_string_list)
        return tile_string_list

    def count(self) -> int:
        """
        Counts the tiles that are left in the bag.
        :return: Number of tiles in the bag.
        """
        return sum((element.count for element in self.bag.values()))

    def remaining_points(self) -> int:
        """
        Sums up the points pf the tiles, that are left in the bag.
        :return: Number of points.
        """
        return sum((element.value * element.count for element in self.bag.values()))

    def draw_tile(self) -> str:
        """
        Draws a random tile from the bag.
        :return: The drawn tile.
        """
        draw = self.tile_string.pop()
        self.bag[draw].count -= 1
        return draw

    def draw_tiles(self, count: int) -> list[str]:
        """
        Draws multiple tiles from the bag.
        :param count: Number of tiles that should be drawn.
        :return: List of the drawn tiles.
        """
        return [self.draw_tile() for _ in range(count)]

    def tile_score(self, tile: str) -> int:
        """
        Retrieve the score of a tile.
        :param tile: The tile.
        :return: The score of the tile.
        """


@dataclass
class TileInfo:
    """
    Class for representing information about a tile.
    """
    letter: str
    count: int
    value: int
