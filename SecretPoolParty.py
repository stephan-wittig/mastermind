#Mattis Deisen(Github: Skatam)

#Derping around with what appears to be smart but ressource intensive on first thought. Only works with 4 digits atm!
import collections
import random

class secretPoolEliminator():

    def __init__(self, numOfDigits):
        self.numOfDigits = numOfDigits
        self.lastScore = []
        self.lastGuesses = []
        self.maxScore = numOfDigits * 10
        #initialize List with all possible secrets
        self.possibleSecretPool = self.generatePossibleSecrets()
        print('New Round!')


    #returns 5 new codes to evaluate
    def nextDraw(self):
        nextGuesses = []

        #if the correct score was guessed last round, initialize again
        for score in self.lastScore:
            if score == self.maxScore:
                self.__init__(self.numOfDigits)
                return self.firstGuesses()

        #In first round take default guesses (improve those guesses later)
        if not self.lastGuesses:
            return self.firstGuesses()

        #Remove impossible secrets from pool
        self.removeImpossibleSecrets()

        #Randomly select secrets from pool <--- this is stupid and should be changed to select codes that are somewhat different from each other
        for _ in range(5):
            # Create 5 new guesses
            choice = random.choice(self.possibleSecretPool)
            choice = self.stringifyIntList(choice)
            nextGuesses.append(choice)
            self.lastGuesses = nextGuesses
        return nextGuesses

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

    #returns guesses for first round
    def firstGuesses(self):

        firstGuesses = []
        firstGuesses.append('0123')
        firstGuesses.append('1234')
        firstGuesses.append('5678')
        firstGuesses.append('9012')
        firstGuesses.append('3456')

        self.lastGuesses = firstGuesses
        return firstGuesses

    #This should be optimized and generalized. Needs to generate all possible combinations in a list (10^4 for 4 digits to 10^10 for 10 digits)
    @staticmethod
    def generatePossibleSecrets():
        secrets = []
        for a in range(10):
            for b in range(10):
                for c in range(10):
                    for d in range(10):
                        secrets.append(str(a)+str(b)+str(c)+str(d))
        return secrets

    def results(self, results):
        self.lastScore = results

    #stringifyIntList stringifies IntList to stringList because python datatypes are confusing and this is set up badly...
    def stringifyIntList(self, intList):
        stringyThing = [str(i) for i in intList]
        stringyThing = ("".join(stringyThing))
        return stringyThing