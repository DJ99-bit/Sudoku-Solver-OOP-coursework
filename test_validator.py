import unittest
from src.board import SudokuBoard
from src.validator import Validator


class TestValidator(unittest.TestCase):
    def setUp(self):
        self.valid_board = SudokuBoard([
            [1, 0, 0, 4, 0, 6],
            [0, 5, 6, 0, 2, 0],
            [2, 0, 0, 5, 0, 1],
            [0, 1, 3, 0, 6, 0],
            [3, 0, 1, 6, 0, 2],
            [0, 6, 5, 0, 1, 0]
        ])

    def test_row_is_valid(self):
        self.assertTrue(Validator.is_row_valid(self.valid_board, 0))

    def test_column_is_valid(self):
        self.assertTrue(Validator.is_column_valid(self.valid_board, 0))

    def test_box_is_valid(self):
        self.assertTrue(Validator.is_box_valid(self.valid_board, 0, 0))

    def test_board_is_valid(self):
        self.assertTrue(Validator.is_board_valid(self.valid_board))

    def test_valid_move_returns_true(self):
        self.assertTrue(Validator.is_valid_move(self.valid_board, 0, 1, 2))

    def test_invalid_move_returns_false_if_value_in_row(self):
        self.assertFalse(Validator.is_valid_move(self.valid_board, 0, 1, 1))


if __name__ == "__main__":
    unittest.main()