"""
The scrabble_player module describes an abstract player that implements custom
logic and playing habits in its child. The abstract class is used in the implementation
of the game loop, thus not caring if a player or an AI implementation is playing.
"""

from abc import ABC, abstractmethod
from src.shared.scrabble_bag import ScrabbleBag
from src.shared.scrabble_board import ScrabbleBoard
from src.shared.scrabble_rack import ScrabbleRack


class ScrabblePlayer(ABC):
    """
    Abstract class of a player.
    """
    def __init__(self):
        self.rack = ScrabbleRack()

    @abstractmethod
    def say_hello(self) -> None:
        """
        Prints information about itself to the console.
        e.g.: print('Player [Artificial]: Basic')
        """

    @abstractmethod
    def suggest_move(self, board: ScrabbleBoard):
        """
        Given the current board, the method returns the move
        that the player would make. The logic behind it
        depends on the implementation and could be human made.
        :return: The move, the player wants to make.
        """

    def fill_rack(self, bag: ScrabbleBag) -> None:
        """
        Takes the bag and fills the own rack back up.
        """
        missing_count = self.rack.count_missing()
        self.rack.add(bag.draw_tiles(missing_count))
