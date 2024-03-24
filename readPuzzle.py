'''
Method to read in a sudoku puzzle file, confirm it is a file and return a puzzle matrix 
puzzle can be a string of numbers or a text file with a string of numbers
'''

import sys
import numpy as np

class ReadPuzzle:
    def __init__(self,inputfile):
        
        try:
            puzzleData = open(inputfile)
            self.puzzleData = puzzleData.read()
        except FileNotFoundError:
            self.puzzleData = inputfile
            
        self.checkFileLength()


    def checkFileLength(self):
        # Checks that file is correct size [9x9]
        
        length = len(str(self.puzzleData))
        if not ( length == 81):
            raise TypeError("Puzzle is incorrect size, must be 9x9")
        pass
    
    def createPuzzleMatrix(self):
        # creates a puzzle matrix 

        res = list(self.puzzleData)
        res = [int(i) for i in res] 
        self.puzMatrix = np.reshape(res,(9,9))
        return self.puzMatrix


