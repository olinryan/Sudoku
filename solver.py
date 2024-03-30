'''
methods to solve a suduko puzzle

'''
import os
import numpy as np
import time

from displayPuzzle import displayPuzzle
from checker import *

def solveMethod1(puzzle):
    # iterate through each element and 
    # check each number against row col and square
    print("Solving Puzzle ...")
    loopNum = 0
    while not checkPuzzle(puzzle):
        changed = False
        sqnum = 1

        # nested loop for each element:
        for row in range(9):
            for col in range(9):

                # check elemnt is empty:
                if puzzle[row][col] == 0:
                    candidate = np.array([])    # create candidate array

                    # loop each number 1-9
                    for i in range(1,10):
                        square = callSquareIndex(puzzle,row,col)

                        # Check number is not in row, column or square
                        if not i in puzzle[row] and not i in puzzle[:,col] and not i in square:
                            candidate = np.append(candidate,i)      # add to candidate list

                    # If there is only one cadidate, set puzzle element to candidate
                    if len(candidate) == 1:
                        # os.system("clear")    # used to simulate animation
                        puzzle[row][col] = candidate
                        displayPuzzle(puzzle)
                        changed = True
                        # time.sleep(0.2)         # used to simulate animation

                sqnum = 1
        loopNum += 1

        # if puzzle has not been changed after iterating through, try something else
        if not changed:
            print("Solver is stuck using basic solve algorithm after ",loopNum," Iterations.")
            print("Attmpting adjecent method...")
            puzzle, changed = solveMethod2(puzzle)
            if not changed:
                break
    return puzzle

def solveMethod2(puzzle):
    # iterate through each element and check that number is not in adjcent rows/columns
    # and adjacent column/row is not empty

    changed = False

    # nested loop for each element:
    for row in range(9):
        for col in range(9):
            
            # check elemnt is empty
            if puzzle[row][col] == 0:
                
                # create candidate array, for this algorithm length will always be 1
                candidate = np.array([])    
                square = callSquareIndex(puzzle,row,col)
            
                # call adjacent row and col indices
                adj_col_1, adj_col_2 = callAdjacentIndex(col)
                adj_row_1, adj_row_2 = callAdjacentIndex(row)
                
                for i in range(1,10):
                    # check element is not in square:
                    if not i in square:
                        
                        # check adjacent rows have i and adjacent col are not empty
                        if (i in puzzle[adj_row_1] and i in puzzle[adj_row_2] and 
                            (not puzzle[row][adj_col_1] == 0 or i in puzzle[:,adj_col_1] ) and 
                            (not puzzle[row][adj_col_2] == 0 or i in puzzle[:,adj_col_2] )):
                            candidate = np.append(candidate,i)      # add to candidate list
                        
                        # check adjacent columns have i and adjcent rows are not empty
                        elif (i in puzzle[:,adj_col_1] and i in puzzle[:,adj_col_2] and 
                        (not puzzle[adj_row_1][col] == 0 or i in puzzle[adj_row_1]) and
                        (not puzzle[adj_row_2][col] == 0 or i in puzzle[adj_row_2] )):
                            candidate = np.append(candidate,i)      # add to candidate list

                # If there is only one cadidate, set puzzle element to candidate
                if len(candidate) == 1:
                    # os.system("clear")    # used to simulate animation
                    puzzle[row][col] = candidate
                    displayPuzzle(puzzle)
                    changed = True
                    # time.sleep(0.2)         # used to simulate animation

    if changed:
        print("Finished Adjacent method.")
        return puzzle, changed
    else:
        print("Solver is stuck using adjacent solve method.")
        return puzzle, changed


                
                    
