import unittest
from src.board import SudokuBoard


class TestSudokuBoard(unittest.TestCase):
    def setUp(self):
        self.board = SudokuBoard([
            [1, 0, 0, 4, 0, 6],
            [0, 5, 6, 0, 2, 0],
            [2, 0, 0, 5, 0, 1],
            [0, 1, 3, 0, 6, 0],
            [3, 0, 1, 6, 0, 2],
            [0, 6, 5, 0, 1, 0]
        ])

    def test_get_value(self):
        self.assertEqual(self.board.get_value(0, 0), 1)

    def test_set_value(self):
        self.board.set_value(0, 1, 2)
        self.assertEqual(self.board.get_value(0, 1), 2)

    def test_is_empty(self):
        self.assertTrue(self.board.is_empty(0, 1))
        self.assertFalse(self.board.is_empty(0, 0))

    def test_find_empty(self):
        self.assertEqual(self.board.find_empty(), (0, 1))

    def test_invalid_value_raises_error(self):
        with self.assertRaises(ValueError):
            self.board.set_value(0, 0, 9)


if __name__ == "__main__":
    unittest.main()