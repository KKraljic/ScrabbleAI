"""
The scrabble_game module is the topmost module.
It describes a scrabble game in its entirety, with all subcomponents.
"""
from src.backend.players.artificial_player_basic import ArtificialPlayerBasic
from src.frontend.human_player import HumanPlayer
from src.shared.scrabble_bag import ScrabbleBag
from src.shared.scrabble_board import ScrabbleBoard
from src.shared.scrabble_move import ScrabbleMove


class ScrabbleGame:
    """
    The entirety of a scrabble game with all subcomponents.
    """
    def __init__(self):
        # Game assets
        self.board = ScrabbleBoard()
        self.bag = ScrabbleBag()

        # Define players
        self.players = [
            ArtificialPlayerBasic(),
            HumanPlayer()
        ]

        self.prepare()
        self.play()

    def prepare(self) -> None:
        """
        Prepares the game for playing
        """
        # Initialize game
        for player in self.players:
            player.say_hello()
            player.fill_rack(self.bag)

    def play(self) -> None:
        """
        Start the game loop for playing
        """

    def check_move_validity(self, move: ScrabbleMove) -> bool:
        """
        Checks if the provided move is valid
        :return: Move validity
        """
