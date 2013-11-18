from time import *
from random import *


class Board(object):

    def __init__(numRows, numColumns, seed=time.time()):
        self.seed = seed
        self.numRows = numRows
        self.numColumns = numColumns
        random.seed(seed)
        



class Colour:
    RED = 0
    BLUE = 1
    GREEN = 2
    YELLOW = 3
    PURPLE = 4

