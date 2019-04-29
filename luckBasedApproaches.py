import random
import string

class totallyRandom():
    def __init__(self, numOfDigits):
        self.numOfDigits = numOfDigits
        self.lastScore = []
        self.lastGuesses = []

    def nextDraw(self):
        nextGuesses = []
        for _ in range(5):
            # Randomly generate string in first draw
            nextGuesses.append("".join([random.choice(string.digits) for j in range(self.numOfDigits)]))
        self.lastGuesses = nextGuesses
        return nextGuesses

    def results(self, results):
        pass