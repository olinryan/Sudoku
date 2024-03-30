'''
methods for checking various components of a sudoku puzzle
and the whole puzzle
'''

import numpy as np

def checkRow(puzzleRow):
    # check a single row of a sudoku puzzle
    # confirm input is a row
    if not (puzzleRow.shape == (9,)):
        raise ValueError("Cannot check row, not a row")
    
    for i in range(1,10):
        if not i in puzzleRow:
            return False
        if not np.count_nonzero(puzzleRow == i) == 1:
            return False
    return True

def checkCol(puzzleCol):
    # check a single column of a sudoku puzzle
    # confirm input is a column

    if not (puzzleCol.shape == (9,)):
        raise ValueError("Cannot check column, not a column")
    
    for i in range(1,10):
        if not i in puzzleCol:
            return False
        if not np.count_nonzero(puzzleCol == i) == 1:
            return False
    return True

def checkSquare(puzzleSquare):
    # check a single column of a sudoku puzzle
    # confirm input is a column

    if not (puzzleSquare.shape == (3,3)):
        raise ValueError("Cannot check square, not a square")
    
    for i in range(1,10):
        if not i in puzzleSquare:
            return False
        if not np.count_nonzero(puzzleSquare == i) == 1:
            return False
    return True

def callSquare(puzzle, squareNum):
    # Call a particular square in the puzzle
    # -------------------------------
    # |1        |4        |7        |
    # |    1    |    2    |    3    |
    # |         |         |         |
    # |-----------------------------|
    # |         |         |         |
    # |    4    |    5    |    6    |
    # |         |         |         |
    # |-----------------------------|
    # |         |         |         |
    # |    7    |    8    |    9    |
    # |         |         |         |
    # -------------------------------
    
    if squareNum > 9 or squareNum < 1:
        raise ValueError("Square index is not in range")
    
    # hard coded bc i am lzy:
    if squareNum == 1:
        square = puzzle[0:3,0:3]
    if squareNum == 2:
        square = puzzle[0:3,3:6]
    if squareNum == 3:
        square = puzzle[0:3,6:9]
    if squareNum == 4:
        square = puzzle[3:6,0:3]
    if squareNum == 5:
        square = puzzle[3:6,3:6]
    if squareNum == 6:
        square = puzzle[3:6,6:9]
    if squareNum == 7:
        square = puzzle[6:9,0:3]
    if squareNum == 8:
        square = puzzle[6:9,3:6]
    if squareNum == 9:
        square = puzzle[6:9,6:9]
    
    return square
    
def callSquareIndex(puzzle, row, col):
    # Call a particular square using an index in the puzzle
    
    if row > 8 or row < 0:
        raise ValueError("Row index is not in range")
    if col > 8 or col < 0:
        raise ValueError("Column index is not in range")

    # TODO: make this not hard coded:
    if row in [0,1,2] and col in [0,1,2]:
        square = puzzle[0:3,0:3]
    if row in [0,1,2] and col in [3,4,5]:
        square = puzzle[0:3,3:6]
    if row in [0,1,2] and col in [6,7,8]:
        square = puzzle[0:3,6:9]
    if row in [3,4,5] and col in [0,1,2]:
        square = puzzle[3:6,0:3]
    if row in [3,4,5] and col in [3,4,5]:
        square = puzzle[3:6,3:6]
    if row in [3,4,5] and col in [6,7,8]:
        square = puzzle[3:6,6:9]
    if row in [6,7,8] and col in [0,1,2]:
        square = puzzle[6:9,0:3]
    if row in [6,7,8] and col in [3,4,5]:
        square = puzzle[6:9,3:6]
    if row in [6,7,8] and col in [6,7,8]:
        square = puzzle[6:9,6:9]
    
    return square
    
def callAdjacentIndex(index):
    # input an index and return the other two indices
    # in same square row

    if index in [0,3,6]:
        return index + 1, index + 2
    elif index in [1,4,7]:
        return index - 1, index + 1
    elif index in [2,5,8]:
        return index - 2, index - 1
    else:
        raise ValueError("Index out of bounds for 9x9 puzzle")

def checkPuzzle(puzzle):
    # check entire puzzle
    for i in range(1,10):
        if not checkRow(puzzle[i-1]): return False
        if not checkCol(puzzle[:,i-1]): return False
        if not checkSquare(callSquare(puzzle,i)): return False
    return True