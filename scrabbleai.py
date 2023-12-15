import argparse

from shared.scrabble_game import ScrabbleGame

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument('action')
    args = parser.parse_args()

    game = ScrabbleGame()
