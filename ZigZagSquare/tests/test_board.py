from pickle import NONE
from more_itertools import first
import Board
import unittest

class MyTestCase(unittest.TestCase):
    def test_populate_board(self):
        test_board_vals = [
                            [NONE, 4 ,NONE, NONE, NONE, NONE, NONE, 2 ,8],
                            [3, NONE, NONE, NONE, 7, NONE, 3, 5, 6],
                            [5, NONE, 7, NONE, NONE, NONE, NONE, NONE, NONE,],
                            [NONE, NONE, 5, NONE, 1, 3, 5, NONE, NONE],
                            [NONE, 4, NONE, NONE, 2, 8, NONE, NONE, NONE],
                            [NONE, 8, NONE, 4, NONE, NONE, 2, NONE, 3],
                            [4, 5, NONE, 2, 7, 4, NONE, 5, 2],
                            [NONE, 6, 3, 0, NONE, 1, NONE, 0, NONE],
                            [NONE, 7, NONE, 6, NONE, NONE, NONE, NONE, NONE]
                            ]
        first_board = Board.Board.inital_vals(test_board_vals)

if __name__ == "__main__":
    unittest.main()