import game
import statistics
import csv
import time
import progressbar

# Import your algorithms
from SecretPoolParty import secretPoolEliminator
from luckBasedApproaches import totallyRandom
from geneticAlgorithms import genetic
from bercowAlgorithms import basicBercow, bercowPoolParty

numOfDigits = 10
numOfDraws = 60
numOfGames = 100

# Add your algorithm here to test it
algorithms = [
    bercowPoolParty
]

scores = []
roundsWon = []
runtimes = []

print("The secrets are", str(numOfDigits), "digits long.")
print(str(len(algorithms)),"algorithms will be tested.")
print("Simulation starts.")

with open("results.csv", mode="a", newline="") as csv_file:
    fieldnames = ["Algorithm", "Sample_size", "Number of Digits", "Rounds_won", "Score", "Score/Guess", "Runtime"]
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    writer.writeheader()
    for algo in algorithms:
        for i in progressbar.progressbar(range(numOfGames)):
            start = time.time()
            # Initiate game
            g = game.Game(numOfDraws, numOfDigits)
            # Initiate algorithm
            a = algo(numOfDigits)


            for j in range(numOfDraws):
                nextDraw = a.nextDraw()
                a.results(g.submitGuesses(nextDraw))

            roundsWon.append(g.getRoundNumber())
            scores.append(g.getTotalScore())
            
            runtimes.append(time.time() - start)

            #Debugging
            #print(i)

        print("Finished testing", type(a).__name__ +".")
        writer.writerow({ 
            "Algorithm": type(a).__name__, 
            "Sample_size": numOfGames, 
            "Number of Digits": numOfDigits, 
            "Rounds_won": str(statistics.mean(roundsWon)), 
            "Score": str(statistics.mean(scores)), 
            "Score/Guess": str(statistics.mean(scores) / (numOfDraws * 5)),
            "Runtime": str(statistics.mean(runtimes))
        })
csv_file.close()
print("Finished simulation")