import time
import os
from termcolor import colored

# Function to print the Sudoku board in a grid format with colored text
def print_board(board, initial_board):
    os.system('cls')  # For Linux/Mac, use 'cls' for Windows
    for i in range(9):
        row = []
        for j in range(9):
            if board[i][j] == 0:
                row.append(".")  # Print "." for empty spaces
            elif initial_board[i][j] != 0:
                # Hardcoded numbers are green
                row.append(colored(str(board[i][j]), 'green'))
            else:
                # Numbers being tried are cyan
                row.append(colored(str(board[i][j]), 'cyan'))
        print(" ".join(row))
    time.sleep(0.04)  # Reduced sleep time for smoother transition

# Function to find an empty spot on the board (represented by 0)
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

# Function to check if placing num at position (row, col) is valid
def is_valid(board, num, pos):
    # Check row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # Check 3x3 grid
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

# Backtracking brute-force Sudoku solver
def brute_force_sudoku_solver(board, initial_board):
    empty = find_empty(board)
    if not empty:
        return True  # No empty space, puzzle is solved
    row, col = empty

    for i in range(1, 10):  # Try numbers 1 through 9
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            print_board(board, initial_board)  # Visualize the current board
            if brute_force_sudoku_solver(board, initial_board):
                return True
            board[row][col] = 0  # Reset and backtrack

    return False

# Example Sudoku board (0 represents empty spaces)
initial_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Copy the initial board to be modified by the solver
board = [row[:] for row in initial_board]

# Call the solver and show steps
brute_force_sudoku_solver(board, initial_board)
print("Solved Sudoku Board:")
print_board(board, initial_board)
