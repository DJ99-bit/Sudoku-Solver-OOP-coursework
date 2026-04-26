from src.board import SudokuBoard


class FileManager:
    @staticmethod
    def load_board(file_path):
        grid = []

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if len(line) != 6 or not line.isdigit():
                    raise ValueError("Each line must contain exactly 6 digits.")
                grid.append([int(char) for char in line])

        if len(grid) != 6:
            raise ValueError("File must contain exactly 6 lines.")

        return SudokuBoard(grid)

    @staticmethod
    def save_board(board, file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            for row in range(6):
                line = "".join(str(board.get_value(row, col)) for col in range(6))
                file.write(line + "\n")