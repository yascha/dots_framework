import time
import board
import score
import re
import argparse

DEFAULT_NUM_COLS = 6
DEFAULT_NUM_ROWS = 6
DEFAULT_SEED = int(time.time())
DEFAULT_NUM_MOVES = 30

class Game(object):
    
    def __init__(self, numRows, numColumns, seed, numMoves):
        self._board = board.Board(numRows, numColumns, seed)
        self._score = score.Score()
        self._movesLeft = numMoves

        # Valid input must be a list of (x0,y0),(x1, y1),...(xn, yn)
        # coordinates where x and y are integer values indicating
        # a cell position on the board with the origin (0,0) located
        # at the bottom left corner of the board.
        # The list of coordinates must of length >= 2.
        self._validInputRegex = re.compile(r"(\((\d+),(\d+)\)(?=($|,\()))+")


    def _isGameOver(self):
        return self._movesLeft < 1


    def _printGameStatus(self):
        print "SCORE: {0}\nMOVES LEFT: {1}".format(self._score.getScore(),
                                                   self._movesLeft)


    def play(self):
        self._board.printBoard()
        self._printGameStatus()

        while not self._isGameOver():
            try:
                self._doMove()
                self._movesLeft -= 1
                self._printGameStatus()
            except board.InvalidMoveException, invalidMove:
                print "Invalid move: {0}\n" \
                      "Please try again.".format(invalidMove)
            except Exception, err:
                print "Unexpected error: {0}".format(err)

        print "Final score: {0}".format(self._score.getScore())


    def _parseUserCoords(self, userInput):
        if not self._validInputRegex.match(userInput):
            raise board.InvalidMoveException("User input format invalid. Must be "
                                             "a list of at least 2 or more (x,y) "
                                             "coordinate tuples delimited by "
                                             "commas (with 0,0 being the bottom "
                                             "left corner). "
                                             " e.g. (1,2),(3,4)")

        coordsList = [(int(matchingGroups[1]), int(matchingGroups[2]))
                      for matchingGroups in self._validInputRegex.findall(userInput)]
        if len(coordsList) < 2:
            raise board.InvalidMoveException("Number of coordinates provided must "
                                             "be >= 2.")
        return coordsList

    def _doMove(self):
        print "Enter Move:"
        userInput = raw_input()
        coordsList = self._parseUserCoords(userInput)
        points = self._board.move(coordsList)
        self._score.addToScore(points)


def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", "-r", type=int, default=DEFAULT_NUM_ROWS, help="Number of rows.")
    parser.add_argument("--columns", "-c", type=int, default=DEFAULT_NUM_COLS, help="Number of columns.")
    parser.add_argument("--seed", "-s", type=int, default=DEFAULT_SEED, help="Board seed.")
    parser.add_argument("--numMoves", "-m", type=int, default=DEFAULT_NUM_MOVES, help="Number of moves.")
    return parser.parse_args()


if __name__ == "__main__":
    args = getArgs()
    game = Game(args.rows, args.columns, args.seed, args.numMoves)
    print "Starting new game with the following settings:"
    print "Num Rows: {0}\n" \
          "Num Columns: {1}\n" \
          "Seed: {2}\n" \
          "Num Moves: {3}\n".format(args.rows, args.columns, args.seed, args.numMoves)
    print "Enter moves as a series of x,y coordinate pairs.  ie. (0,0),(1,0),(1,1),(1,2)."
    game.play()
