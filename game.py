import random
import string


class Game():
    """One game with multiple rounds."""

    def __init__(self, numOfDraws, numOfDigits):
        self.totalDraws = numOfDraws
        self.remainingDraws = numOfDraws

        self.rounds = []

    def getCurrentRound(self):
        if len(self.rounds) != 0 and self.rounds[-1].running:
            return self.rounds[-1]
        else:
            # return new round

    def _newRound(self):
        # create new Round and add to array

    def getTotalScore(self):
        # return sum of round scores

    def getRemainingDraws(self):
        # return number of remaining draws (5 draws per guess)

    def getAllDraws(self):
        # return all draws (guesses + results) for each round

    def getRoundNumber(self):
        return len(self.rounds)

    def submitGuesses(self):
        # direct one draw (= 5 guesses) to current round and return results

class Round():
        """One round against one enemy (=secret)"""
    def __init__(self, numOfDigits):
        self.secret = createSecret(numOfDigits)
        self.draws = []
        self.score = 0
        self.draws = []

    def getScore(self):
        return self.score

    def submitGuesses(self, guesses):
        results = []
        for guess in guesses:
            results.append(self._calcResult(guess))
        return results

    def _calcResult(self, guess):
        # Calculate result for one guess

    def _createSecret(self, numOfDigits):
        return "".join([random.choice(string.digits) for i in xrange(32)])
