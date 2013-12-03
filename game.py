import time
from dots_framework import board, colours, score
import colours

class Game(object):
    
    def __init__(self, numRows=6, numColumns=6, seed=time.time(), numMoves=30):
        self._board = board.Board(numRows, numColumns, seed)
        self._score = score.Score()
        self._movesLeft = numMoves
        self._move = [] #TODO: Remove this, it's just a hack until I add command-line move parsing


    def _isGameOver(self):
        return self._movesLeft < 1


    def play(self):
        self._board.printBoard()
        while not self._isGameOver():
            self._doMove()
        print "Final score: " + self._score


    def _doMove(self):
        print "Enter Move:"
        while(1):
            move = raw_input()
            try:
                self._board._isValidMove(move)
                break
            except Exception as e: 
                if type(e) is board.InvalidMoveException:
                    print "Invalid move, please try again."
                else:
                    print e
        points = self._board.move(self._move)
        self._score.addToScore(points)
        self._movesLeft -= 1


if __name__ == "__main__": 
    game = Game()
    print "Starting new game"
    print "Enter moves as a series of x,y coordinate pairs.  ie. (0,0), (1,0), (1,1), (1,2)."
    game.play()
