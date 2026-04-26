from src.board import SudokuBoard
from src.validator import Validator


def main():
    board = SudokuBoard([
        [1, 0, 0, 4, 0, 6],
        [0, 5, 6, 0, 2, 0],
        [2, 0, 0, 5, 0, 1],
        [0, 1, 3, 0, 6, 0],
        [3, 0, 1, 6, 0, 2],
        [0, 6, 5, 0, 1, 0]
    ])

    print("Current board:")
    print(board)
    print()

    print("Is the whole board valid?")
    print(Validator.is_board_valid(board))
    print()

    print("Can we place 2 at row 0, col 1?")
    print(Validator.is_valid_move(board, 0, 1, 2))


if __name__ == "__main__":
    main()