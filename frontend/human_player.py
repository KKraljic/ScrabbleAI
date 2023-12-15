from shared.scrabble_bag import ScrabbleBag
from shared.scrabble_board import ScrabbleBoard
from shared.scrabble_player import ScrabblePlayer


class HumanPlayer(ScrabblePlayer):
    def suggest_move(self, board: ScrabbleBoard):
        pass

    def __init__(self):
        super().__init__()

    def say_hello(self):
        print('Player [Human]')
