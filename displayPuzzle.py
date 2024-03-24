'''
method to display puzzle in window
'''

import numpy as np

def displayPuzzle(puzMatrix):
    # Display user freindly sudoku puzzle [9x9]
    puzString = "-------------------------------\n"
    for k in range(9):
        puzString = puzString + "|"
        for j in range(3):
            for i in range(3):
                if (puzMatrix[k][i+j*3] == 0):
                    puzString = puzString + "   "
                else:
                    puzString = puzString + " " + str(puzMatrix[k][i+j*3]) + " "
            puzString = puzString + "|"
        puzString = puzString + "\n"
        if (k == 2 or k == 5):
            puzString = puzString + "|-----------------------------|\n"
    puzString = puzString + "-------------------------------"
    print(puzString)

    return