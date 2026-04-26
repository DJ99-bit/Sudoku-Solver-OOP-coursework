from src.file_manager import FileManager
from src.validator import Validator
from src.backtracking_solver import BacktrackingSolver


def main():
    input_file = "data/puzzle.txt"
    output_file = "data/solution.txt"

    board = FileManager.load_board(input_file)

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
        FileManager.save_board(board, output_file)
        print(f"\nSolved board saved to {output_file}")
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()