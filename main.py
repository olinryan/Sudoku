'''
Accesses various classes to read, solve and display sudoku puzzle
'''

from readPuzzle import ReadPuzzle
import sys
from displayPuzzle import displayPuzzle


puzObj = ReadPuzzle(sys.argv[1])
puzObj = puzObj.createPuzzleMatrix()
print("Original Puzzle: ")
displayPuzzle(puzObj)