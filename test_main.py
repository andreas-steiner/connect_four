import unittest
from main import Board, PlayBoard


class test_game(unittest.TestCase):
        
    def setUp(self):

        self.blank_game_state_1 = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
        ]

        self.test_game_state_2 = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, "2", "1", None, None, None],
            [None, None, "1", "2", None, None, None],
            ["1", "2", "2", "1", "2", "1", "2"],
            ["1", "1", "2", "2", "1", "2", "1"],
        ]

        self.test_game_stat_3 = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, "2", "1", None, None, None],
            [None, None, "2", "1", None, None, None],
            ["1", "2", "2", "1", "2", "1", "2"],
            ["1", "1", "2", "2", "1", "2", "1"],
        ]

        self.test_win_cond_1 = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            ["2", "2", "2", None, None, None, None],
            ["1", "1", "1", "1", None, None, None],
        ]

        self.test_win_cond_2 = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, "1", None, None, None],
            [None, None, "1", "2", None, None, None],
            ["2", "1", "2", "1", None, None, None],
            ["1", "2", "1", "2", None, None, None],
        ]

        self.test_win_cond_3 = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            ["1", None, None, None, None, None, None],
            ["1", "2", None, None, None, None, None],
            ["1", "2", None, None, None, None, None],
            ["1", "2", None, None, None, None, None],
        ]

    def test_win_cond(self):
        pass

    def test_place_stone(self):
        pass


    def test_make_board(self):
        pass

    def test_loc_valid(self):
        pass

    def test_next_row(self):
        pass

if __name__ == '__main__':
    unittest.main()

