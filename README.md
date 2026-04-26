# Sudoku-Solver-OOP-coursework
Dominykas Jarutis EF-25/2 Coursework

This project is a Python based 6x6 sudoku solver created for OOP coursework. The aim of the project is to apply OOP principles in a practical application solving a sudoku puzzle. It implements a 6x6 sudoku solver that can read a puzzle, check if it is valid, solve it and save the solution to a file. The application is built using seperate modules for the sudoku board, validation, solving logic and file managment. The project also includes unit tests.

How to use the program
- open the project in Visual Studio Code or another Python IDE
- prepare the puzzle file in 'data/puzzle.txt'
- the file must contain 6 lines and each line must contain 6 digits
- run the program with: python main.py

The project is divided into separate modules:
- board.py for storing the sudoku board
- validator.py for sudoku rule validation
- solver.py for the abstract solver
- backtracking_solver.py for the recursive solving algorithm
- file_manager.py for loading and saving files
- solver_factory.py for solver object creation

The application is built from seperate components that work together: the board, validator, solver, file manager and solver factory. This demonstrates composition and modular object oriented design.

Core functionality is tested using Python's unittest framework.
The test covers:
- board creation and modification
- board validation
- move validation
- solving a sudoku puzzle

Results
- the program succesfully loads a 6x6 sudoku puzzle from a text file
- it validates the board before solving it
- the backtracking algorithm solves valid sudoku boards
- the solved board is displayed and saved to an output file

Conclusions: this coursework resulted in a working 6x6 sudoku solver written in Python. The project applies OOP principles, uses a design pattern, supports file input and output, includes unit tests.

Future improvements:
- support for different sudoku sizes
- additional solving strategies
- a graphical user interface
