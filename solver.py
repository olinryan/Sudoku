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
        # print("*********************************************************************************")
        changed = False
        sqnum = 1
        print("Itteration: ", loopNum)
        for row in range(9):
            for col in range(9):
                # print("Index: ",row,",",col)

                if puzzle[row][col] == 0:
                    candidate = np.array([])
                    for i in range(1,10):
                        square = callSquareIndex(puzzle,row,col)
                        if not i in puzzle[row] and not i in puzzle[:,col] and not i in square:
                            candidate = np.append(candidate,i)
                    # print("Candidates: ",candidate)
                    if len(candidate) == 1:
                        os.system("clear")
                        puzzle[row][col] = candidate
                        displayPuzzle(puzzle)
                        changed = True
                        time.sleep(0.2)

                sqnum = 1
        loopNum += 1
        if not changed:
            print("Solver is stuck after ",loopNum," Iterations.")
            break
    return puzzle


                
                    
