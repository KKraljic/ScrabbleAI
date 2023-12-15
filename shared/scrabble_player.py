from abc import ABC, abstractmethod

from shared.scrabble_bag import ScrabbleBag
from shared.scrabble_board import ScrabbleBoard
from shared.scrabble_rack import ScrabbleRack


class ScrabblePlayer(ABC):
    def __init__(self):
        self.rack = ScrabbleRack()

    @abstractmethod
    def say_hello(self):
        pass

    @abstractmethod
    def suggest_move(self, board: ScrabbleBoard):
        pass

    def fill_rack(self, bag: ScrabbleBag):
        missing_count = self.rack.count_missing()
        self.rack.add(bag.draw_tiles(missing_count))


