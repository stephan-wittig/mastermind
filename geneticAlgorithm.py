import random
import string

class SmartAlgo():
    def __init__(self, numOfDigits, mQuotient):
        self.numOfDigits = numOfDigits
        self.lastScore = []
        self.lastGuesses = []
        self.maxScore = numOfDigits * 5 * 10

    def nextDraw(self):
        nextGuesses = []
        if len(self.lastGuesses) > 0:
            for _ in range(5):
                # Create 5 new guesses
                nextGuess = ""
                for j in range  (self.numOfDigits):
                    # Choose x digits (according to game rules)
                    #Combine last guesses
                    choice =  random.choices(range(len(self.lastScore)), self.lastScore)[0]
                    nextGuess += self.lastGuesses[choice][j]
                nextGuesses.append(nextGuess)
            self.lastGuesses = nextGuesses
            return nextGuesses
            
        else:
            for _ in range(5):
                # Randomly generate string in first draw
                nextGuesses.append("".join([random.choice(string.digits) for j in range(self.numOfDigits)]))
            self.lastGuesses = nextGuesses
            return nextGuesses

    def results(self, results):
        self.lastScore = results

