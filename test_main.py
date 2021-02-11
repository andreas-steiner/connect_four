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
        self.player_one = 1
        self.player_two = 2
        self.win_1 = np.array([[0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [2, 2, 2, 0, 0, 0, 0],
                               [1, 1, 1, 1, 0, 0, 0]])

        self.win_2 = np.array([[0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 2, 0, 0, 0, 0, 0],
                               [1, 2, 0, 0, 0, 0, 0],
                               [1, 2, 0, 0, 0, 0, 0],
                               [1, 2, 1, 0, 0, 0, 0]])

        self.win_3 = np.array([[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 1, 0, 0, 0],
                              [0, 0, 1, 2, 0, 0, 0],
                              [0, 1, 2, 1, 0, 0, 0],
                              [1, 2, 1, 2, 0, 0, 0]])

        self.not_win = np.array([[0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0],
                                 [1, 0, 0, 0, 0, 0, 0],
                                 [1, 0, 0, 0, 0, 0, 0],
                                 [1, 0, 0, 0, 0, 0, 0]])

        self.draw = np.array([[1, 1, 2, 1, 2, 1, 2, ],
                              [2, 1, 2, 1, 2, 1, 1, ],
                              [2, 1, 2, 1, 2, 1, 2, ],
                              [1, 2, 1, 2, 1, 2, 1, ],
                              [1, 2, 1, 2, 1, 2, 2, ],
                              [1, 2, 1, 2, 1, 2, 1, ]])

        self.not_draw = np.array([[1, 0, 0, 1, 2, 1, 2, ],
                                  [2, 1, 2, 1, 2, 1, 1, ],
                                  [2, 1, 2, 1, 2, 1, 2, ],
                                  [1, 2, 1, 2, 1, 2, 1, ],
                                  [1, 2, 1, 2, 1, 2, 2, ],
                                  [1, 2, 1, 2, 1, 2, 1, ]])

        self.board_state_1 = np.array([[0, 0, 0, 0, 0, 0, 0, ],
                                       [0, 0, 0, 0, 0, 0, 0, ],
                                       [0, 0, 0, 0, 0, 0, 0, ],
                                       [0, 0, 0, 0, 0, 0, 0, ],
                                       [0, 0, 0, 0, 0, 0, 0, ],
                                       [1, 2, 1, 2, 1, 2, 1, ]])

        self.board_state_2 = np.array([[1, 1, 2, 1, 2, 1, 2, ],
                                       [2, 1, 2, 1, 2, 1, 1, ],
                                       [2, 1, 2, 1, 2, 1, 2, ],
                                       [1, 2, 1, 2, 1, 2, 1, ],
                                       [1, 2, 1, 2, 1, 2, 2, ],
                                       [1, 2, 1, 2, 1, 2, 1, ]])


    def test_draw(self):
        """
        Tests if current board state is a draw.
        """
        self.assertTrue(PlayBoard.draw(self.draw), msg="It's not a draw!")
        self.assertFalse(PlayBoard.draw(self.not_draw), msg="It's not a draw!")



    def test_win_cond(self):
        """
        Tests if Player has won after setting his piece.
        """
        self.assertTrue(PlayBoard.win_cond(self, self.win_1, self.player_one), msg="Player 1 has not won!")
        self.assertTrue(PlayBoard.win_cond(self, self.win_2, self.player_two), msg="Player 1 has not won!")
        self.assertTrue(PlayBoard.win_cond(self, self.win_3, self.player_one), msg="Player 1 has not won!")
        self.assertFalse(PlayBoard.win_cond(self, self.not_win, any([1, 1])), msg="Has actually won!")

    #def test_loc_valid(self):
        #self.assertTrue(self, self.board_state_1)
        #self.assertTrue(self, self.board_state_2)

    def test_place_stone(self):
        pass

    def test_make_board(self):
        pass

    def test_next_row(self):
        pass


if __name__ == '__main__':
    unittest.main()



