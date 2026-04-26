from src.board import SudokuBoard
from src.validator import Validator
from src.backtracking_solver import BacktrackingSolver


def main():
    board = SudokuBoard([
        [1, 2, 0, 4, 5, 6],
        [4, 0, 6, 1, 2, 3],
        [2, 3, 4, 5, 0, 1],
        [5, 6, 1, 0, 3, 4],
        [3, 4, 0, 6, 1, 2],
        [6, 1, 2, 3, 4, 0]
    ])

    print("Original board:")
    print(board)
    print()

    print("Is the board valid?")
    print(Validator.is_board_valid(board))
    print()

    solver = BacktrackingSolver()
    solved = solver.solve(board)

    if solved:
        print("Solved board:")
        print(board)
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()