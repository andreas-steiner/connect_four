import unittest
import numpy as np
from game.main import PlayBoard


class test_main(unittest.TestCase):
    """
    Unit Test class for main.py

    Returns
    -------------
    Unit Tests class for main.py
    """

    def setUp(self) -> None:
        """
    Board class used as parent class for the future playing board

    Parameters
    ___________
    columns : int
        number of Columns
    rows : int
        number of Rows
    player_one : int
        player one
    player_two : int
        player two
    win_1 : numpy array
        Game state: Player 1 won with 4 horizontal pieces
    win_2 : numpy array
        Game state: Player 2 won with 4 vertical pieces
    win_3 : numpy array
        Game state: Player 1 won with 4 diagonal pieces
    win_4 : numpy array
        Game state: Player 2 won with 4 diagonal pieces
    not_win : numpy array
        Game state: Neither player has won yet
    draw : numpy array
        Game state: Draw
    not_draw : numpy array
        Game state: Neither player has won yet, close to a draw
    board_state_1 : numpy array
        Game state: still running game
    board_state_2 : numpy array
        Game state: still running game
    board_state_3 : numpy array
        Game state: still running game; Identical to self.board_state_2
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

        self.win_4 = np.array([[0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [2, 0, 0, 0, 0, 0, 0],
                               [1, 2, 1, 2, 0, 0, 0],
                               [1, 1, 2, 1, 0, 0, 0],
                               [1, 2, 1, 2, 0, 0, 0]])

        self.not_win = np.array([[0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0],
                                 [2, 0, 0, 0, 0, 0, 0],
                                 [1, 0, 0, 0, 0, 0, 0],
                                 [1, 1, 0, 0, 0, 0, 0],
                                 [1, 2, 2, 0, 0, 0, 0]])

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
                                       [0, 0, 0, 2, 0, 0, 0, ],
                                       [1, 0, 0, 2, 0, 0, 0, ],
                                       [1, 2, 1, 2, 0, 2, 1, ]])

        self.board_state_2 = np.array([[0, 0, 0, 0, 0, 0, 0, ],
                                       [0, 0, 0, 0, 0, 0, 0, ],
                                       [0, 0, 0, 0, 0, 0, 0, ],
                                       [0, 0, 0, 2, 0, 0, 0, ],
                                       [1, 0, 0, 2, 0, 0, 0, ],
                                       [1, 2, 1, 2, 1, 2, 1, ]])

        self.board_state_3 = np.array([[0, 0, 0, 0, 0, 0, 0, ],
                                       [0, 0, 0, 0, 0, 0, 0, ],
                                       [0, 0, 0, 0, 0, 0, 0, ],
                                       [0, 0, 0, 2, 0, 0, 0, ],
                                       [1, 0, 0, 2, 0, 0, 0, ],
                                       [1, 2, 1, 2, 1, 2, 1, ]])

    def test_draw(self):
        """
        Tests if current board state is a draw.

        Parameters
        ___________
        draw : numpy array
            a representation of the board in array form
        not_draw : int
            a representation of the board in array form

        Returns
        ___________
        bool
            returns true if board state it is a draw
            returns false if board state is not a draw
        """
        self.assertTrue(PlayBoard.draw(self.draw), msg="It's not a draw!")
        self.assertFalse(PlayBoard.draw(self.not_draw), msg="It's not a draw!")

    def test_win_cond(self):
        """
        Tests for win_cond():

        Parameters
        ___________
        win_1 : numpy array
            Game state: Player 1 won with 4 horizontal pieces
        win_2 : numpy array
            Game state: Player 2 won with 4 vertical pieces
        win_3 : numpy array
            Game state: Player 1 won with 4 diagonal pieces
        win_4 : numpy array
            Game state: Player 2 won with 4 diagonal pieces
        not_win : numpy array
            Game state: Neither player has won yet
        player_one : int
            player one
        player_two : int
            player two

        Returns
        ___________
        bool
            returns true for win_1 to win_4
            returns false for not_win
        """
        self.assertTrue(PlayBoard.win_cond(self, self.win_1, self.player_one), msg="Player 1 has not won!")
        self.assertTrue(PlayBoard.win_cond(self, self.win_2, self.player_two), msg="Player 2 has not won!")
        self.assertTrue(PlayBoard.win_cond(self, self.win_3, self.player_one), msg="Player 1 has not won!")
        self.assertTrue(PlayBoard.win_cond(self, self.win_4, self.player_two), msg="Player 2 has not won!")
        self.assertFalse(PlayBoard.win_cond(self, self.not_win, self.player_one), msg="Has actually won!")

    def test_next_row(self):
        """
        Test for function next_row():

        Parameters
        ___________
        board_state_1 : numpy array
            Game state: still running game
        draw : numpy array
            Game state: Draw
        col : int
            identifier for column position

        Returns
        ___________
        bool
            returns true for board_state_1
            returns false for draw
        """
        self.assertEqual(PlayBoard.next_row(self, self.board_state_1, 6), 0)
        self.assertEqual(PlayBoard.next_row(self, self.draw, 3), None)

    def test_loc_valid(self):
        """
        Test for function loc_valid():

        Parameters
        ___________
        board_state_1 : numpy array
            Game state: still running game
        col : int
            identifier for column position

        Returns
        ___________
        bool
            returns true for board_state_1 after checking col 4
            returns false for board_state_1 after checking col 3
        """
        self.assertTrue(PlayBoard.loc_valid(self, self.board_state_1, 4), msg="location is not valid")
        self.assertFalse(PlayBoard.loc_valid(self, self.board_state_1, 3), msg="location is valid")

    def test_place_stone(self):
        """

        Parameters
        ___________
        board_state_1 : numpy array
            Game state: still running game
        board_state_2 : numpy array
            Game state: still running game
        col : int
            identifier for column position
        row : int
            row coordinate where the stone will be placed
        player_one : int
            player one
        player_two : int
            player two

        Returns
        ___________
        bool
            returns true if board_state_1 after placing stone is identical to board_state_2
            returns false if board_state_2 after placing stone is not identical to board_state_3
        """
        test = str(PlayBoard.place_stone(self, self.board_state_1, 5, 4, self.player_one))
        result = str(self.board_state_2)
        self.assertEqual(test, result)
        test_2 = str(PlayBoard.place_stone(self, self.board_state_2, 5, 4, self.player_two))
        result_2 = str(self.board_state_3)
        self.assertNotEqual(test_2, result_2)


if __name__ == '__main__':
    unittest.main()
