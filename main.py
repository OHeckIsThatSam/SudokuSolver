import numpy as np


def main():

    solve(sudoku_input())


def sudoku_input():
    sudoku = [[0, 8, 0, 5, 0, 4, 0, 0, 3],
              [0, 4, 0, 0, 7, 0, 0, 0, 0],
              [2, 0, 0, 0, 9, 0, 0, 8, 0],
              [0, 1, 0, 4, 0, 0, 0, 0, 0],
              [0, 0, 4, 6, 0, 0, 0, 0, 0],
              [9, 6, 0, 0, 0, 0, 0, 0, 1],
              [7, 0, 0, 0, 0, 0, 3, 0, 6],
              [0, 0, 0, 0, 5, 0, 8, 0, 0],
              [1, 0, 0, 2, 0, 0, 9, 7, 0]]
    return sudoku


def solve(sudoku):
    """ Function to solve the given sudoku, using recursion and back tracking to brute force the solution """
    # Loop every cell in sudoku until the value of a cell is 0
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                # Test integers 1-9 to see if one is legal in this position
                for n in range(1, 10):
                    if is_legal(sudoku, x, y, n):
                        # Assign the value of the cell to the legal integer and call the function to solve the value
                        # of the next empty cell
                        sudoku[x][y] = n
                        solve(sudoku)
                        # If the function reaches a dead end with no legal integers for a position then the function
                        # backtracks with a different legal integer
                        sudoku[x][y] = 0
                # When there are no more empty cells the sudoku is solved
                return
    print(np.matrix(sudoku))
    input("Done? ")


def is_legal(sudoku, row, column, number):
    """ Function that determines if a number is legal in a specific position in the sudoku grid """
    # If the number already exists in the row then return false
    if sudoku[row].count(number) != 0:
        return False

    # If the number already exists in the column then return false
    for i in range(0, 9):
        if sudoku[i][column] == number:
            return False

    # Takes the coordinate a cell and calculates the coordinate of the 3x3 square it's in
    square_row = (row // 3) * 3
    square_column = (column // 3) * 3
    # If the number already exists in the square then return false
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[square_row + i][square_column + j] == number:
                return False

    return True


main()
