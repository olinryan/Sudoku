'''
Accesses various classes to read, solve and display sudoku puzzle
'''

import sys

from readPuzzle import ReadPuzzle
from displayPuzzle import displayPuzzle
from checker import *
from solver import *

puzObj = ReadPuzzle(sys.argv[1])
puzObj = puzObj.createPuzzleMatrix()
print("Original Puzzle: ")
displayPuzzle(puzObj)
# print(puzObj)
# print(checkPuzzle(puzObj))
solvedPuzzle = solveMethod1(puzObj)
print("Validation: ",checkPuzzle(solvedPuzzle))
# print(callSquareIndex(puzObj,4,4))