'''
Accesses various classes to read, solve and display sudoku puzzle
'''

import sys

from readPuzzle import ReadPuzzle
from displayPuzzle import displayPuzzle
from checker import *
from solver import *

###########################
# Solve method to use:
# solver = 1 # Basic
solver = 2 # Backtrack
# solver = 3 # Other

# Read in puzzle from termianl line:
try:
    puzObj = ReadPuzzle(sys.argv[1])
except IndexError:
    puzObj = ReadPuzzle("Puzzles/easy032824")

# Turn input to a matrix and display:
puzObj = puzObj.createPuzzleMatrix()
print("Original Puzzle: ")
displayPuzzle(puzObj)

# Check using basic method:
if solver == 1:
    solvedPuzzle = solveMethod1(puzObj)
    print("Validation: ",checkPuzzle(solvedPuzzle))

# Check using backtrack method:
if solver == 2:
    solvedPuzzle = solveBacktrackMethod(puzObj)
    print("Validation: ",checkPuzzle(solvedPuzzle))

if solver == 3:
    print(checkRules(puzObj))