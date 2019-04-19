import game
import geneticAlgorithm
import statistics

numOfDigits = 4
numOfDraws = 60
numOfGames = 2000

scores = []
roundsWon = []

print("The secrets are " + str(numOfDigits) + " digits long.")
print("Simulation starts")
print("Quotient; Rounds won; Score; Score/Guess")
for q in [1]:
    for i in range(numOfGames):
        g = game.Game(numOfDraws, numOfDigits)
        a = geneticAlgorithm.SmartAlgo(numOfDigits, q)

        for j in range(numOfDraws):
            nextDraw = a.nextDraw()
            a.results(g.submitGuesses(nextDraw))

        roundsWon.append(g.getRoundNumber())
        scores.append(g.getTotalScore())

    print(str(q) + "; " + str(statistics.mean(roundsWon)) + "; " + str(statistics.mean(scores)) + "; " + str(statistics.mean(scores) / (numOfDraws * 5)))

print("Finished simulation")