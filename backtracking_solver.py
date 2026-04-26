from src.solver import Solver
from src.validator import Validator


class BacktrackingSolver(Solver):
    def solve(self, board):
        empty_position = board.find_empty()

        if empty_position is None:
            return True

        row, col = empty_position

        for value in range(1, 7):
            if Validator.is_valid_move(board, row, col, value):
                board.set_value(row, col, value)

                if self.solve(board):
                    return True

                board.set_value(row, col, 0)

        return False