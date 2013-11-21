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
            # TODO: Look into actually printing each char in colour.
            # There are lots of python libraries that do cross-platform
            # ANSI colouring of text

    def _isValidMove(self, coordsList):
        """ 
        Check if the requested move is valid.
        Returns true if the move is valid, false otherwise.
        Takes:
            coordsList - a list of tuples of the form (xcoord, ycoord) 
                where (0,0) is the bottom left corner of the board.
        """
        
        # For a move to be valid, all dots must be the same colour,
        # the path must not cross the same dot more than twice,
        # and the same path between two dots cannot be traversed more
        # than once.
        
        # Make sure all the coordinates are valid
        for (x,y) in coordsList:
            if not self._areValidCoords(x,y):
                return False
        
        # Make sure all the dots are the same colour
        firstDotColour = self._getColour(coordsList[0][0], coordsList[0][1])
        if not all(firstDotColour == self._getColour(coords[0], coords[1]) 
                   for coords in coordsList):
            return False
        
        # Now make sure they are all connected
        
        
        
        return True
    
    def _getColour(self, xcoords, ycoords):
        """
        Gets the numerical colour (from Colours) of the dot at the 
        specified coordinates where (0,0) is the bottom left corner
        of the board.
        Assumes the coordinates are valid.
        """
        
        return self.columns[xcoords][ycoords]

    def _areValidCoords(self, xcoords, ycoords):
        """
        Checks if the coordinates are valid in the coordinate system where 
        (0,0) is the bottom left corner of the board.
        Returns true if so, false otherwise.
        """
        if (xcoords == None or ycoords == None):
            return False
        if not (xcoords >= 0 and xcoords < self.numColumns and 
                ycoords >= 0 and ycoords < self.numRows):
            return False
        return True


    def _isNeighbour(self, firstDotCoords, secondDotCoords):
        """
        Checks if the two passed in locations are vertical or
        horizontal neighbours.
        Returns true if so, false otherwise.
        """
        # TODO: Implement this
        return True


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
