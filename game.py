import time
import random


class Board(object):

    def __init__(self, numRows=6, numColumns=6, seed=time.time()):
        self.seed = seed
        self.numColumns = numColumns
        self.numRows = numRows
        self._setupBoard(numRows, numColumns, self.seed)


    def _setupBoard(self, numRows, numColumns, seed):
        """ Sets up the initial board state """
        random.seed(seed)
        self.columns = []
        
        # TODO: Make a column class that is derived from list
        for _ in xrange(0, numColumns):
            col = []
            for _ in xrange(0, numRows):
                col.append(random.randint(0, Colours.NUM_COLOURS-1))
            self.columns.append(col)
            
    def printBoard(self, spacing=4):
        """ Prints the board state """
        # Remember that the first piece in each column is at the bottom
        for row in xrange(self.numRows-1, -1, -1):
            boardRow = ""
            for col in self.columns:
                boardRow += " "*spacing + Colours.chars[col[row]]
            print boardRow + "\n"

    def isValidMove(self, coordsList):
        """ 
        Check if the requested move is valid.
        Returns true if the move is valid, false otherwise.
        Takes:
            coordsList - a list of tuples of the form (xcoord, ycoord) 
                where (0,0) is the bottom left corner of the board.
        """
        


class Colours:
    RED = 0
    BLUE = 1
    GREEN = 2
    YELLOW = 3
    PURPLE = 4

    NUM_COLOURS = 5

    chars = {
                RED : 'r',
                BLUE : 'b',
                GREEN : 'g',
                YELLOW : 'y',
                PURPLE : 'p'
            } 

