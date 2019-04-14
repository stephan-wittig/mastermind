import game
import smartAlgo
import statistics

numOfDigits = 4
numOfDraws = 60
numOfGames = 1000

scores = []
roundsWon = []

print("The secrets are " + str(numOfDigits) + " digits long.")
print("Each game runs for " + str(numOfDraws) + " draws.")
print("Let the games begin")
for i in range(numOfGames):
    g = game.Game(numOfDraws, numOfDigits)
    a = smartAlgo.SmartAlgo(numOfDigits)

    for j in range(numOfDraws):
        nextDraw = a.nextDraw()
        a.results(g.submitGuesses(nextDraw))

    roundsWon.append(g.getRoundNumber())
    scores.append(g.getTotalScore())
    print("Finished game " + str(i))

print("Rounds won on average: " + str(statistics.mean(roundsWon)))
print("Average game score: " + str(statistics.mean(scores)))
print("Average score per guess: " + str(statistics.mean(scores) / (numOfDraws * 5)))