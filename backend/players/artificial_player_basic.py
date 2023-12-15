from backend.datastructures.dawg import DAWG
from shared.scrabble_bag import ScrabbleBag
from shared.scrabble_board import ScrabbleBoard
from shared.scrabble_player import ScrabblePlayer


class ArtificialPlayerBasic(ScrabblePlayer):
    def suggest_move(self, board: ScrabbleBoard):
        pass

    def __init__(self):
        super().__init__()

        self.dawg = DAWG()
        self.dawg.create('test.txt')

    def say_hello(self):
        print('Player [Artificial]: Basic')
