"""
The module holds the logic for a human player.
It implements the logic and UI for playing.
"""

from src.shared.scrabble_board import ScrabbleBoard
from src.shared.scrabble_player import ScrabblePlayer


class HumanPlayer(ScrabblePlayer):
    """
    Representation of a real player, that can be controlled by the user.
    """
    def suggest_move(self, board: ScrabbleBoard):
        """
        Gives the user the current board. The user has to decide which move to make.
        :param board: Current board
        :return: Suggested move, can be invalid.
        """

    def say_hello(self) -> None:
        """
        Prints information about the player to the console.
        """
        print('Player [Human]')
