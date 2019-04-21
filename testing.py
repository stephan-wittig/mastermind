import game
import smartAlgorithms
import statistics
import csv
import SecretPoolParty

numOfDigits = 4
numOfDraws = 60
numOfGames = 100
# Add your algorithm here to test it
algorithms = [
    smartAlgorithms.genetic,
    smartAlgorithms.totallyRandom,
    SecretPoolParty.secretPoolEliminator
]

scores = []
roundsWon = []

print("The secrets are", str(numOfDigits), "digits long.")
print(str(len(algorithms)),"algorithms will be tested.")
print("Simulation starts.")

with open("results.csv", mode="a", newline="") as csv_file:
    fieldnames = ["Algorithm", "Sample_size", "Number of Digits", "Rounds_won", "Score", "Score/Guess"]
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    for algo in algorithms:
        for i in range(numOfGames):
            # Initiate game
            g = game.Game(numOfDraws, numOfDigits)
            # Initiate algorithm
            a = algo(numOfDigits)


            for j in range(numOfDraws):
                nextDraw = a.nextDraw()
                a.results(g.submitGuesses(nextDraw))

            roundsWon.append(g.getRoundNumber())
            scores.append(g.getTotalScore())

            #Debugging
            print(i)

        print("Finished testing", type(a).__name__ +".")
        writer.writerow({ 
            "Algorithm": type(a).__name__, 
            "Sample_size": numOfGames, 
            "Number of Digits": numOfDigits, 
            "Rounds_won": str(sum(roundsWon)), 
            "Score": str(sum(scores)), 
            "Score/Guess": str(statistics.mean(scores) / (numOfDraws * 5))
        })
csv_file.close()
print("Finished simulation")