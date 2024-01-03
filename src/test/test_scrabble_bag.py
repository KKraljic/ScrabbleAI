"""
scrabble_bag.py tests
"""
import unittest
from src.shared.scrabble_bag import ScrabbleBag


class ScrabbleBagTestCase(unittest.TestCase):
    """
    scrabble_bag.py tests
    """
    def test_randomness(self):
        """
        Testing the randomization and seed usage.
        :return:
        """
        # Different seeds
        bag_a = ScrabbleBag(seed=1)
        bag_b = ScrabbleBag()
        self.assertTrue(bag_a.tile_string != bag_b.tile_string)

        # Same seeds
        bag_c = ScrabbleBag(seed=1)
        self.assertTrue(bag_a.tile_string == bag_c.tile_string)
