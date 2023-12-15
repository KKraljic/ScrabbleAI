from backend.players.artificial_player_basic import ArtificialPlayerBasic
from frontend.human_player import HumanPlayer
from shared.scrabble_bag import ScrabbleBag
from shared.scrabble_board import ScrabbleBoard


class ScrabbleGame:
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

    def prepare(self):
        # Initialize game
        for player in self.players:
            player.say_hello()
            player.fill_rack(self.bag)

    def play(self):
        # Start Game loop
        pass
