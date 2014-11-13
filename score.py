

class Score(object):
    def __init__(self):
        self._score = 0
    
    def addToScore(self, pointsToAdd):
        self._score += pointsToAdd
        return self._score

    def getScore(self):
        return self._score
