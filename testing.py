import game
import smartAlgo

numOfDigits = 4
numOfDraws = 60
g = game.Game(numOfDraws, numOfDigits)
a = smartAlgo.SmartAlgo(numOfDigits)
print("Game started!")
print("The secret is " + str(numOfDigits) + " digits long.")
print("The game runs for " + str(numOfDraws) + " draws.")

for i in range(numOfDraws):
    nextDraw = a.nextDraw()
    a.results(g.submitGuesses(nextDraw))
print("Rounds won: " + str(g.getRoundNumber()))
print("Total Score: " + str(g.getTotalScore()))