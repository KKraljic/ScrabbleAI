"""
backend/datastructures/dawg.py tests
"""
import unittest

from src.backend.datastructures.dawg import DAWG


class ScrabbleBagTestCase(unittest.TestCase):
    """
    backend/datastructures/dawg.py tests
    """
    def test_unique_pairs(self) -> None:
        """
        Testing the creation of the unique pairs
        """
        # Small list
        small_list = ['a', 'b', 'c', 'd']
        pairs_small_list = DAWG._list_to_pairs(small_list)
        self.assertEqual(pairs_small_list, [
            ['a', 'b', False],
            ['a', 'c', False],
            ['a', 'd', False],
            ['b', 'c', False],
            ['b', 'd', False],
            ['c', 'd', False]])

        # \ A B C D
        # A   X X X
        # B     X X
        # C       X
        # D

        # Big list
        size = 100
        pairs_big_list = DAWG._list_to_pairs(list(range(size)))
        self.assertEqual((size*(size-1))/2, len(pairs_big_list))
