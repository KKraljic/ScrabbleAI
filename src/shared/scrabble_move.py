"""
Module with classes, represneting moves, a player can make.
"""

from dataclasses import dataclass
from enum import Enum


class MoveDirection(Enum):
    """
    Enum for the direction of the move.
    """
    ACROSS = 1
    DOWN = 2


@dataclass
class ScrabbleMove:
    """
    Class for representing the move, performed by a player
    """
    postion: (int, int)
    direction: MoveDirection
    word: str
    tiles_used: list[str]  # Needed to determine, if jokers were used.
