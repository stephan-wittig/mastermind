import random
import string
import itertools
import collections
    
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

class bercowPoolParty():
    def __init__(self, numOfDigits):
        self.numOfDigits = numOfDigits
        self.lastScore = []
        self.lastGuesses = []
        self.maxScore = numOfDigits * 10
        self.roundNumber = 0
        self.digits = []
        self.possibleSecretPool = []

    def nextDraw(self):
        nextGuesses = []
        
        # First, find out number of each digit
        if self.roundNumber == 0:
            for d in range(5):
                nextGuesses.append("".join([string.digits[d] for _ in range(self.numOfDigits)]))
        elif self.roundNumber == 1 and not len(self.digits) == self.numOfDigits:
            for d in range(5):
                nextGuesses.append("".join([string.digits[d+5] for _ in range(self.numOfDigits)]))
        # Then, establish ORDEEEER, this time using poolParty
        else:
            if len(self.possibleSecretPool) == 0:
                self.createSecretPool()
            for _ in range(5):
                # Create 5 new guesses
                # The pool party should take place here
                nextGuesses.append("".join(random.choice(self.possibleSecretPool)))

        self.lastGuesses = nextGuesses
        return nextGuesses

    def results(self, results):
        self.lastScore = results

        if self.roundNumber <= 1:
            for i, result in enumerate(results):
                if result > 0:
                    for _ in range(int(result / 10)):
                        self.digits.append(self.lastGuesses[i][0])
        else:
            self.lastScore = results
            self.removeImpossibleSecrets()

        self.roundNumber += 1
        
        if max(results) == self.maxScore:
            self.__init__(self.numOfDigits)

    def createSecretPool(self):
        # Creates all permutations of the pool and removes duplicates
        self.possibleSecretPool = list(set(itertools.permutations(self.digits)))

    #Name is telling
    def removeImpossibleSecrets(self):

        #Combines guesses and scores for iteration
        for guessandscore in zip(self.lastGuesses, self.lastScore):

            #Goes through every possible remaining secret and checks whether it would have lead to the received score for
            #the guess that was submitted. If not, drop it like its hot.
            for secret in self.possibleSecretPool:
                if self.evaluateTargets(secret, guessandscore[0]) == guessandscore[1]:
                    continue
                else:
                    self.possibleSecretPool.remove(secret)

    #Calculates and returns score that guess would have gotten if secret from possibleSecretPool was the correct one.
    def evaluateTargets(self, secret, guess):
        if len(guess) != len(secret):
            raise Exception('Secret length not same as guess length #BetterThrowException')
        else:
            countedGuess = collections.Counter(guess)
            countedSecret = collections.Counter(secret)
            close = sum(min(countedSecret[k], countedGuess[k]) for k in countedSecret)
            exact = sum(a == b for a, b in zip(secret, guess))
            close -= exact
            return exact * 10 + close * 5