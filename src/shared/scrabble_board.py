"""
The module holds the class for representing the board (over time)
"""

from src.shared.config_reader import Config
from src.shared.scrabble_move import ScrabbleMove


class ScrabbleBoard:
    """
    A Class for representing the current board and all board states over time.
    """
    def __init__(self):
        board_size = Config.board_size()
        init_state = [["#" for _ in range(board_size)] for _ in range(board_size)]
        self.board_states = [init_state]

    def get(self, age: int = 0) -> list[list[str]]:
        """
        Get the board state.
        :param age: Age of the board (0: current state, 1: state before, ...)
        :return: A single board state
        """
        saved_states_count = len(self.board_states)
        if saved_states_count > age:
            return self.board_states[saved_states_count - age - 1]
        raise ValueError("A board state this old does not exist.")

    def perform_move(self, move: ScrabbleMove) -> int:
        """
        Performs the actual move on the board
        :return: Number of points gained
        """

    def print(self, age: int = 0) -> None:
        """
        Prints one board state to the console.
        :param age: Age of the board
        """
        board = self.get(age)

        print("   | ", end="")
        for i, row in enumerate(board):
            print(f"{i + 1:02}", end=" ")
        print("\n----------------------------------------------------")

        for i, row in enumerate(board):
            print(f"{i + 1:02}", end=" | ")
            for _, col in enumerate(row):
                print(col, end="  ")
            print(" |")
