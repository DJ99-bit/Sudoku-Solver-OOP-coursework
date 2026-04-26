class Validator:
    @staticmethod
    def is_row_valid(board, row):
        values = []
        for col in range(6):
            value = board.get_value(row, col)
            if value != 0:
                values.append(value)
        return len(values) == len(set(values))

    @staticmethod
    def is_column_valid(board, col):
        values = []
        for row in range(6):
            value = board.get_value(row, col)
            if value != 0:
                values.append(value)
        return len(values) == len(set(values))

    @staticmethod
    def is_box_valid(board, start_row, start_col):
        values = []
        for row in range(start_row, start_row + 2):
            for col in range(start_col, start_col + 3):
                value = board.get_value(row, col)
                if value != 0:
                    values.append(value)
        return len(values) == len(set(values))

    @staticmethod
    def is_board_valid(board):
        for row in range(6):
            if not Validator.is_row_valid(board, row):
                return False

        for col in range(6):
            if not Validator.is_column_valid(board, col):
                return False

        for start_row in range(0, 6, 2):
            for start_col in range(0, 6, 3):
                if not Validator.is_box_valid(board, start_row, start_col):
                    return False

        return True

    @staticmethod
    def is_valid_move(board, row, col, value):
        if value < 1 or value > 6:
            return False

        if not board.is_empty(row, col):
            return False

        for current_col in range(6):
            if board.get_value(row, current_col) == value:
                return False

        for current_row in range(6):
            if board.get_value(current_row, col) == value:
                return False

        start_row = (row // 2) * 2
        start_col = (col // 3) * 3

        for current_row in range(start_row, start_row + 2):
            for current_col in range(start_col, start_col + 3):
                if board.get_value(current_row, current_col) == value:
                    return False

        return True