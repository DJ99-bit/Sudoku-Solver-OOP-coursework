from src.board import SudokuBoard


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


if __name__ == "__main__":
    main()