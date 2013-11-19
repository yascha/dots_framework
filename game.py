from time import *
from random import *


class Board(object):

    def __init__(numRows, numColumns, seed=time.time()):
        self.seed = seed
        random.seed(seed)
        _setupBoard()


    def _setupBoard(self, numRows, numColumns):
        self.columns = []
        for col in numColumns:
            # Make a row



class Colour:
    RED = 0
    BLUE = 1
    GREEN = 2
    YELLOW = 3
    PURPLE = 4

