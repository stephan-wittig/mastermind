import random
import string
    
class basicBercow():
    def __init__(self, numOfDigits):
        self.numOfDigits = numOfDigits
        self.lastScore = []
        self.lastGuesses = []
        self.maxScore = numOfDigits * 10
        self.roundNumber = 0
        self.digits = []

    def nextDraw(self):
        nextGuesses = []
        
        # First, find out number of each digit
        if self.roundNumber == 0:
            for d in range(5):
                nextGuesses.append("".join([string.digits[d] for _ in range(self.numOfDigits)]))
        elif self.roundNumber == 1 and not len(self.digits) == self.numOfDigits:
            for d in range(5):
                nextGuesses.append("".join([string.digits[d+5] for _ in range(self.numOfDigits)]))
        # Then, establish ORDEEEER
        else:
            for _ in range(5):
                # Create 5 new guesses
                nextGuesses.append(self.createRandomGuess())

        self.lastGuesses = nextGuesses
        return nextGuesses

    def results(self, results):
        self.lastScore = results

        if self.roundNumber <= 1:
            for i, result in enumerate(results):
                if result > 0:
                    for _ in range(int(result / 10)):
                        self.digits.append(self.lastGuesses[i][0])

        self.roundNumber += 1
        
        if max(results) == self.maxScore:
            self.__init__(self.numOfDigits)

    def createRandomGuess(self):
        guess = ""
        pot = self.digits[:]
        for _ in range (self.numOfDigits):
            # Adds one of the digits from the array, and removes it from the array
            guess += pot.pop(random.randint(1, len(pot)) - 1)
        return guess