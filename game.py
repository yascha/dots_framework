import time
from dots_framework import board, colours
import colours

class Game(object):
    
    def __init__(self, numRows=6, numColumns=6, seed=time.time()):
        self._Board = board.Board(numRows, numColumns, seed)




