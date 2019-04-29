#Mattis Deisen(Github: Skatam)

#Derping around with what appears to be smart but ressource intensive on first thought.
import collections
import random

class secretPoolEliminator():

    def __init__(self, numOfDigits):
        self.numOfDigits = numOfDigits
        self.lastScores = []
        self.lastGuesses = []
        self.maxScore = numOfDigits * 10
        self.possibleSecretPool = self.generatePossibleSecrets(numOfDigits)

    # Is done after every draw and lastScores are taken into account for next code guess determination
    def results(self, results):
        self.lastScores = results

    # Generates all possible secrets in a list as strings
    @staticmethod
    def generatePossibleSecrets(numofdigits):
        secrets = []
        #print(10**numofdigits)
        for i in range (1, 10**numofdigits):
            secrets.append(str(i).zfill(numofdigits))
        return secrets


    # Applies the algorithm to decide on the next 5 guesses which are returned
    def nextDraw(self):
        nextGuesses = []

        # In first round take default guesses (improve those guesses later)
        if not self.lastGuesses:
            return self.firstGuesses()

        #If the correct score was guessed last round, initialize again for new code
        if (self.maxScore in self.lastScores):
            self.__init__(self.numOfDigits)
            return self.firstGuesses()

        #Remove impossible secrets from pool
        self.removeImpossibleSecrets()

        #Randomly select secrets from pool <--- this is stupid and should be changed to select codes that are somewhat different from each other
        for _ in range(5):
            # Create 5 new guesses
            choice = random.choice(self.possibleSecretPool)
            nextGuesses.append(choice)
            self.lastGuesses = nextGuesses
        return nextGuesses

    #Name is telling
    def removeImpossibleSecrets(self):

        #Combines guesses and scores for iteration
        for guessandscore in zip(self.lastGuesses, self.lastScores):

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
        for _ in range(5):
            firstGuesses.append(str(random.randint(0,10**self.numOfDigits-1)).zfill(self.numOfDigits))
        self.lastGuesses = firstGuesses
        return firstGuesses



