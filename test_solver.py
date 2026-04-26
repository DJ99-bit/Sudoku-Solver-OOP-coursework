import unittest
from src.board import SudokuBoard
from src.backtracking_solver import BacktrackingSolver
from src.validator import Validator


class TestBacktrackingSolver(unittest.TestCase):
    def test_solver_solves_valid_board(self):
        board = SudokuBoard([
            [1, 2, 0, 4, 5, 6],
            [4, 0, 6, 1, 2, 3],
            [2, 3, 4, 5, 0, 1],
            [5, 6, 1, 0, 3, 4],
            [3, 4, 0, 6, 1, 2],
            [6, 1, 2, 3, 4, 0]
        ])

        solver = BacktrackingSolver()
        solved = solver.solve(board)

        self.assertTrue(solved)
        self.assertTrue(Validator.is_board_valid(board))
        self.assertIsNone(board.find_empty())


if __name__ == "__main__":
    unittest.main()