import time
import random
import colours

from colorama import init as colorama_init

class Board(object):

    def __init__(self, numRows=6, numColumns=6, seed=time.time()):
        self.seed = seed
        self.numColumns = numColumns
        self.numRows = numRows
        self._setupBoard(numRows, numColumns, self.seed)
        self._colours = colours.Colours()
        colorama_init()


    def _setupBoard(self, numRows, numColumns, seed):
        """ Sets up the initial board state """
        random.seed(seed)
        self.columns = []
        
        # TODO: Make a column class that is derived from list
        for _ in xrange(0, numColumns):
            col = []
            for _ in xrange(0, numRows):
                col.append(self._getNewDotColour())
            self.columns.append(col)
            
    def printBoard(self, spacing=4):
        """ Prints the board state """
        # Remember that the first piece in each column is at the bottom
        for row in xrange(self.numRows-1, -1, -1):
            boardRow = ""
            for col in self.columns:
                try:
                    boardRow += " "*spacing + self._colours.colour(col[row])
                except IndexError:
                    boardRow += " "*spacing + " "
            print boardRow + "\n"

    def move(self, coordsList, printBoard=True):
        """
        Play a move and print the new boardstate (if requested).
        Returns the number of dots that were cleared with this move.
        If the move is invalid, raises InvalidMoveException.
        """
        if not self._isValidMove(coordsList):
            raise InvalidMoveException

        isBox = self._isBox(coordsList)
        numberOfDots = len(coordsList)
        
        if isBox:
            moveColour = self._getDotColour(coordsList[0][0], coordsList[0][1])
            numberOfDots = self._removeAllDotsOfOneColour(moveColour)
            self._fillBoard(moveColour)
        else:
            self._removeDots(coordsList)
            self._fillBoard()

        if printBoard:
            self.printBoard()

        return numberOfDots


    def _isValidMove(self, coordsList):
        """ 
        Check if the requested move is valid.
        Returns True if the move is valid, raises InvalidMoveException otherwise.
        Takes:
            coordsList - a list of tuples of the form (xcoord, ycoord)
                         where (0,0) is the bottom left corner of the board.
        """ 
        # For a move to be valid, all dots must be the same colour,
        # the path must not cross the same dot more than twice,
        # and the same path between two dots cannot be traversed more
        # than once.

        # Make sure all the coordinates are valid
        for (x, y) in coordsList:
            if not self._areValidCoords(x, y):
                raise InvalidMoveException("Coordinates ({0},{1}) are not "
                                           "valid.".format(x, y))
        
        # Make sure all the dots are the same colour
        firstDotColour = self._getDotColour(coordsList[0][0], coordsList[0][1])
        if not all(firstDotColour == self._getDotColour(coords[0], coords[1]) 
                   for coords in coordsList):
            raise InvalidMoveException("All specified dots must be of the "
                                       "same colour.")
        
        # Make sure they are all connected
        for position in xrange(1, len(coordsList)):
            prevPos = coordsList[position-1]
            currentPos = coordsList[position]
            if not self._coordsAreNeighbours(prevPos, currentPos):
                raise InvalidMoveException("Dots {0} and {1} are not "
                                           "connected.".format(prevPos, currentPos))
        
        # Make sure they don't cross the same path twice
        paths = [(coordsList[position-1], coordsList[position]) for position in xrange(1, len(coordsList))]
        if len(set(paths)) != len(paths):
            raise InvalidMoveException("Detected multiple crossing of the same path.")
        
        # Check if they did the same path in the other direction
        reversePaths = []
        for coords in paths:
            reversePaths.append((coords[1], coords[0]))
        
        # You can't go backwards
        for path in reversePaths:
            if path in paths:
                raise InvalidMoveException("Detected multiple crossing of the same path.")
        
        return True
    
    def _getDotColour(self, xcoords, ycoords):
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


    def _coordsAreNeighbours(self, firstDotCoords, secondDotCoords):
        """
        Checks if the two passed in locations are vertical or
        horizontal neighbours.
        Returns true if so, false otherwise.
        """
        getXNeighbours = lambda x, y : [(x2, y) for x2 in range(max(x-1, 0), 
            min(x+2, self.numColumns)) if -1 < x < self.numColumns and x != x2]
        getYNeighbours = lambda x, y : [(x, y2) for y2 in range(max(y-1, 0), 
            min(y+2, self.numRows)) if -1 < y < self.numRows and y != y2]

        firstDotNeighbours = getXNeighbours(firstDotCoords[0], firstDotCoords[1]) + getYNeighbours(firstDotCoords[0], firstDotCoords[1])
        
        if secondDotCoords in firstDotNeighbours:
            return True
        
        return False

    def _isBox(self, coordsList):
        """ 
        Checks if the passed in move makes a box.
        Returns True if so, False otherwise.
        Note: Assumes that the move is valid.
        """
        # To be a box, the same coordinates have to be touched twice.
        if len(coordsList) > len(set(coordsList)):
            return True
        
        return False

    def _removeDots(self, coordsList):
        """
        Remove the dots specified in coordsList.
        Assumes that the move is not a box.
        """
        # TODO: Make this better   :(
        for (x,y) in coordsList:
            self.columns[x][y] = -1

        self._removeAllDotsOfOneColour(-1)


    def _removeAllDotsOfOneColour(self, colour):
        """
        Remove all of the dots of a given colour.
        """
        def filterColour(myColour):
            return myColour != colour

        dotsRemoved = 0

        for col in xrange(0, self.numColumns):
            self.columns[col] = filter(filterColour, self.columns[col])
            dotsRemoved += self.numRows - len(self.columns[col])
        
        return dotsRemoved

    def _fillBoard(self, filterColour=None):
        for col in self.columns:
            while len(col) < self.numRows:
                col.append(self._getNewDotColour(filterColour))

    def _getNewDotColour(self, filterColour=None):
        """
        Get a colour to populate on the board.
        If filterColour is not None, don't return filterColour.
        Returns a colour from the Colours class.
        """
        if filterColour is None:
            return random.randint(0, colours.Colours.NUM_COLOURS-1)
        else:
            returnColour = random.randint(0, colours.Colours.NUM_COLOURS-1)
            while (returnColour == filterColour):
                returnColour = random.randint(0, colours.Colours.NUM_COLOURS-1)
            return returnColour


class InvalidMoveException(Exception):
    pass

