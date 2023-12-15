import json
import random
from array import array
from dataclasses import dataclass
from config_reader import Config


class ScrabbleBag:
    def __init__(self, seed=0):
        if seed != 0:
            random.seed(seed)
        self._fill_bag()

    def _fill_bag(self):
        file = open(Config.bag_config_path(), 'r')
        content = json.loads(file.read())

        self.bag: dict[str, TileInfo] = {
            element['letter']: TileInfo(element['letter'], element['count'], element['value']) for element in content}

        self.tile_string = self._create_tile_string()

    def _create_tile_string(self) -> list[str]:
        tile_string = ''.join([tile.letter * tile.count for tile in self.bag.values()])
        tile_string_list = list(tile_string)
        random.shuffle(tile_string_list)
        return tile_string_list

    def count(self) -> int:
        return sum([element.count for element in self.bag.values()])

    def remaining_points(self) -> int:
        return sum([element.value * element.count for element in self.bag.values()])

    def draw_tile(self) -> str:
        draw = self.tile_string.pop()
        self.bag[draw].count -= 1
        return draw

    def draw_tiles(self, count) -> list[str]:
        return [self.draw_tile() for i in range(count)]

    def tile_score(self, tile) -> int:
        pass



@dataclass
class TileInfo:
    letter: str
    count: int
    value: int
