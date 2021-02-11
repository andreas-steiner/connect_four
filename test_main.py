import unittest
import numpy as np
from main import Board, PlayBoard


# TODO
# draw - I think it's done
# win_cond - I think it's done
# loc_valid
# place_stone
# game_over


class test_game(unittest.TestCase):

    def setUp(self) -> None:

        self.columns = 7
        self.rows = 6


        self.win_1 = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0], [2, 2, 2, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0]])

        self.win_2 = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0]])

        self.not_win = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0]])

        self.draw = np.array([[1, 1, 2, 1, 2, 1, 2, ], [2, 1, 2, 1, 2, 1, 1, ], [2, 1, 2, 1, 2, 1, 2, ],
                              [1, 2, 1, 2, 1, 2, 1, ], [1, 2, 1, 2, 1, 2, 2, ], [1, 2, 1, 2, 1, 2, 1, ]])

        self.not_draw = np.array([[1, 0, 0, 1, 2, 1, 2, ], [2, 1, 2, 1, 2, 1, 1, ], [2, 1, 2, 1, 2, 1, 2, ],
                              [1, 2, 1, 2, 1, 2, 1, ], [1, 2, 1, 2, 1, 2, 2, ], [1, 2, 1, 2, 1, 2, 1, ]])

        self.stone = PlayBoard.place_stone(self, self.win_1, 5, 5, 0)


    def test_draw(self):
        self.assertTrue(PlayBoard.draw(self.draw), msg="It's not a draw!")
        self.assertFalse(PlayBoard.draw(self.not_draw), msg="It's actually a draw!")



    def test_win_cond(self):
        self.assertTrue(PlayBoard.win_cond(self, self.win_1, any([1, 1])), msg="Has not won!")
        self.assertTrue(PlayBoard.win_cond(self, self.win_2, any([1, 1])), msg="Has not won!")
        self.assertFalse(PlayBoard.win_cond(self, self.not_win, any([1, 1])), msg="Has actually won!")


    #def test_place_stone(self):
    #    test = self.test_win_cond_1_2
    #    erg = PlayBoard.place_stone(self, self.test_win_cond_1, 1, 5, None)
    #    self.assertEqual(test, erg)
    #    pass

    def test_make_board(self):
        pass

    def test_loc_valid(self):
        pass

    def test_next_row(self):
        pass


if __name__ == '__main__':
    unittest.main()



