import unittest
import numpy as np
from main import Board, PlayBoard


# TODO
# draw - I think it's done
# win_cond - I think it's done
# loc_valid
# place_stone
# game_over


class test_main(unittest.TestCase):
    """
    Unit Test class for main.py
    -------------
    """

    def setUp(self) -> None:
        """
        Sets up different "game states" for following Unit Test functions.
        -------------
        """
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
        """
        Game state: Player 1 won with 4 horizontal pieces
        -------------
        """

        self.win_2 = np.array([[0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 2, 0, 0, 0, 0, 0],
                               [1, 2, 0, 0, 0, 0, 0],
                               [1, 2, 0, 0, 0, 0, 0],
                               [1, 2, 1, 0, 0, 0, 0]])
        """
        Game state: Player 2 won with 4 vertical pieces
        -------------
        """

        self.win_3 = np.array([[0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 1, 0, 0, 0],
                               [0, 0, 1, 2, 0, 0, 0],
                               [0, 1, 2, 1, 0, 0, 0],
                               [1, 2, 1, 2, 0, 0, 0]])
        """
        Game state: Player 1 won with 4 diagonal pieces
        -------------
        """

        self.not_win = np.array([[0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0],
                                 [2, 0, 0, 0, 0, 0, 0],
                                 [1, 0, 0, 0, 0, 0, 0],
                                 [1, 1, 0, 0, 0, 0, 0],
                                 [1, 2, 2, 0, 0, 0, 0]])
        """
        Game state: Neither player has won yet
        -------------
        """

        self.draw = np.array([[1, 1, 2, 1, 2, 1, 2, ],
                              [2, 1, 2, 1, 2, 1, 1, ],
                              [2, 1, 2, 1, 2, 1, 2, ],
                              [1, 2, 1, 2, 1, 2, 1, ],
                              [1, 2, 1, 2, 1, 2, 2, ],
                              [1, 2, 1, 2, 1, 2, 1, ]])
        """
        Game state: Draw
        -------------
        """

        self.not_draw = np.array([[1, 0, 0, 1, 2, 1, 2, ],
                                  [2, 1, 2, 1, 2, 1, 1, ],
                                  [2, 1, 2, 1, 2, 1, 2, ],
                                  [1, 2, 1, 2, 1, 2, 1, ],
                                  [1, 2, 1, 2, 1, 2, 2, ],
                                  [1, 2, 1, 2, 1, 2, 1, ]])
        """
        Game state: Neither player has won yet, close to a draw
        -------------
        """


        self.board_state_1 = np.array([[0, 0, 0, 0, 0, 0, 0, ],
                                       [0, 0, 0, 0, 0, 0, 0, ],
                                       [0, 0, 0, 0, 0, 0, 0, ],
                                       [0, 0, 0, 2, 0, 0, 0, ],
                                       [1, 0, 0, 2, 0, 0, 0, ],
                                       [1, 2, 1, 2, 1, 2, 1, ]])

        """
        Game state: still running game
        -------------
        """

    def test_draw(self):
        """
        Tests if current board state is a draw.
        -------------
        """
        self.assertTrue(PlayBoard.draw(self.draw), msg="It's not a draw!")
        """
        Tests for draw.
        """
        self.assertFalse(PlayBoard.draw(self.not_draw), msg="It's not a draw!")

    def test_win_cond(self):
        """
        Test for function win_cond():
        -------------
        """
        self.assertTrue(PlayBoard.win_cond(self, self.win_1, self.player_one), msg="Player 1 has not won!")
        """
        Tests for horizontal win condition on player ones' side
        -------------
        """
        self.assertTrue(PlayBoard.win_cond(self, self.win_2, self.player_two), msg="Player 2 has not won!")
        """
        Tests for vertical win condition on player twos' side
        -------------
        
        """
        self.assertTrue(PlayBoard.win_cond(self, self.win_3, self.player_one), msg="Player 1 has not won!")
        """
        Tests for diagonal win condition on player ones' side
        -------------
        """
        self.assertFalse(PlayBoard.win_cond(self, self.not_win, any([1, 1])), msg="Has actually won!")

    def test_next_row(self):
        """
        Test for function next_row():
        -------------
        """
        self.assertEqual(PlayBoard.next_row(self, self.board_state_1, 6), 0)
        """
        Return value should be 0 if there is a free space available in the column
        -------------
        """
        self.assertEqual(PlayBoard.next_row(self, self.draw, 3), None)
        """
        Return value should be None if there is no free space available in the column
        -------------
        """

    # def test_loc_valid(self):
    # self.assertTrue(self, self.board_state_1)
    # self.assertTrue(self, self.board_state_2)

    def test_place_stone(self):
        pass


if __name__ == '__main__':
    unittest.main()
