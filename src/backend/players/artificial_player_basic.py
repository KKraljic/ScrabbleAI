"""
The module holds the logic for an artificial player.
"""

from src.backend.datastructures.dawg import DAWG
from src.shared.scrabble_board import ScrabbleBoard
from src.shared.scrabble_player import ScrabblePlayer


class ArtificialPlayerBasic(ScrabblePlayer):
    """
    Artificial player
    - Name: Basic
    - Version: 1.0
    - Technique: DAWG
    """
    def __init__(self):
        super().__init__()

        self.dawg = DAWG()
        self.dawg.create('test.txt')

    def suggest_move(self, board: ScrabbleBoard):
        """
        Move suggestion
        """

    def say_hello(self):
        """
        Prints information about the player to the console.
        """
        print('Player [Artificial]: Basic')
