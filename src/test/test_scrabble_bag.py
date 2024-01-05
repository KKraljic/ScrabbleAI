"""
scrabble_bag.py tests
"""
import unittest
from src.shared.scrabble_bag import ScrabbleBag


class ScrabbleBagTestCase(unittest.TestCase):
    """
    scrabble_bag.py tests
    """
    def test_randomness(self) -> None:
        """
        Testing the randomization and seed usage.
        """
        # Different seeds
        bag_a = ScrabbleBag(seed=1)
        bag_b = ScrabbleBag()
        self.assertTrue(bag_a.tile_string != bag_b.tile_string)

        # Same seeds
        bag_c = ScrabbleBag(seed=1)
        self.assertTrue(bag_a.tile_string == bag_c.tile_string)

    def test_measurements(self) -> None:
        """
        Testing measurements of the bag (Count and points).
        """
        bag = ScrabbleBag()
        self.assertEqual(bag.count(), 100)
        self.assertEqual(bag.remaining_points(), 187)

    def test_drawing(self) -> None:
        """
        Testing the drawing of tiles
        """
        bag = ScrabbleBag(seed=1)
        self.assertEqual(bag.tile_string[0], 'T')
        self.assertEqual(bag.draw_tile(), 'A')
        self.assertEqual(bag.draw_tiles(3), ['G', 'Z', 'E'])
