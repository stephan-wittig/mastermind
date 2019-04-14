import random
import string

class SmartAlgo():
    def __init__(self, numOfDigits):
        self.numOfDigits = numOfDigits

    def nextDraw(self):
        nextDraw = []
        for i in range(5):
            nextDraw.append("".join([random.choice(string.digits) for j in range(self.numOfDigits)]))
        return nextDraw

    def results(self, results):
        pass
