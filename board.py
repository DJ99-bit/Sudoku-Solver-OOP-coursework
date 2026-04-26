class SudokuBoard:
    def __init__(self, grid):
        if len(grid) != 6:
            raise ValueError("Board must have exactly 6 rows.")

        for row in grid:
            if len(row) != 6:
                raise ValueError("Each row must have exactly 6 columns.")

            for value in row:
                if not isinstance(value, int):
                    raise ValueError("Board values must be integers.")
                if value < 0 or value > 6:
                    raise ValueError("Board values must be between 0 and 6.")

        self._grid = grid

    def get_value(self, row, col):
        return self._grid[row][col]

    def set_value(self, row, col, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        if value < 0 or value > 6:
            raise ValueError("Value must be between 0 and 6.")

        self._grid[row][col] = value

    def is_empty(self, row, col):
        return self._grid[row][col] == 0

    def find_empty(self):
        for row in range(6):
            for col in range(6):
                if self._grid[row][col] == 0:
                    return row, col
        return None

    def __str__(self):
        lines = []
        for row in self._grid:
            lines.append(" ".join(str(value) for value in row))
        return "\n".join(lines)