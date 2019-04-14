import random
import string
import collections

class Game():
    """One game with multiple rounds."""

    def __init__(self, numOfDraws, numOfDigits):
        self.totalDraws = numOfDraws
        self.remainingDraws = numOfDraws
        self.numOfDigits = numOfDigits
        self.rounds = []

    """ Returns the current round. If that round is finished, create and returns a new round""" 
    def getCurrentRound(self):
        if len(self.rounds) != 0 and self.rounds[-1].running:
            return self.rounds[-1]
        else:
            self.rounds.append(Round(self.numOfDigits))
            return self.rounds[-1]

    """Adds up and returns score of each round"""
    def getTotalScore(self):
        totalScore = 0
        for round in self.rounds:
            totalScore += round.score
        return totalScore

    """Returns number of remaining draws"""
    def getRemainingDraws(self):
        return self.remainingDraws

    """Returns past draws and their results"""
    def getAllDraws(self):
        drawsByRounds = []
        for round in self.rounds:
            drawsByRounds.append(round.draws)
        return drawsByRounds

    """Returns current round number (Round numbers start at 0)"""
    def getRoundNumber(self):
        return len(self.rounds)-1

    """Submits multiple guesses by redirecting them to the active round"""
    def submitGuesses(self, guesses):
        if self.remainingDraws > 0:
            self.remainingDraws -= 0
            return self.getCurrentRound().submitGuesses(guesses)
        else:
            return [0] #Could throw an exception

class Round():
    """One round against one enemy (=secret)"""
    
    def __init__(self, numOfDigits):
        self.numOfDigits = numOfDigits
        self.secret = self._createSecret()
        self.countedSecret = collections.Counter(self.secret)
        self.draws = []
        self.score = 0
        self.running = True

    """ Returns score of this round only"""
    def getScore(self):
        return self.score

    """Submits a guess. Don't submit directly to rounds, as draw numbers are not tracked!"""
    def submitGuesses(self, guesses):
        results = []
        draw = []
        for guess in guesses:
            results.append(self._calcResult(guess))
            draw.append({"guess": guess, "result": results[-1]})
        self.draws.append(draw)
        self.score += sum(results)
        return results

    def _calcResult(self, guess):
        if len(guess) != len(self.secret):
            return 0 #Could throw an exception, too, I guess
        elif guess == self.secret:
            self.running = False
            return len(self.secret)*10
        else:
            countedGuess = collections.Counter(guess)
            close = sum(min(self.countedSecret[k], countedGuess[k]) for k in self.countedSecret)
            exact = sum(a==b for a,b in zip(self.secret,guess))
            close -= exact
            return exact * 10 + close * 5

    def _createSecret(self):
        return "".join([random.choice(string.digits) for j in range(self.numOfDigits)])