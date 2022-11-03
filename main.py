import random

import os

import re

os.system('cls' if os.name == 'nt' else 'clear')

scoreMe = 0

scoreComp = 0

gameRound = 0

x = 1

while (x < 2):

  if (scoreMe == 3 or scoreComp == 3):

    x = 2

    if (x == 2):
      if (scoreMe > scoreComp):
        print("You win: " + str(scoreMe) + " - " + str(scoreComp) + "Me")
      else:
        print("I win: " + str(scoreComp) + " - " + str(scoreMe) + " You")

    break

  print("\n")

  print("Rock, Paper, Scissors - Shoot!")

  userChoice = input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")

  if not re.match("[SsRrPp]", userChoice):

    print("Please choose a letter:")

    print("[R]ock, [S]cissors or [P]aper.")

    continue

  choices = ['R', 'P', 'S']

  opponenetChoice = random.choice(choices)

  print("You: " + userChoice + " vs " + "CPU: " + opponenetChoice)

  if opponenetChoice == str.upper(userChoice):

    print("Tie! ")

  elif opponenetChoice == 'R' and userChoice.upper() == 'S':

    gameRound += 1
    scoreComp += 1
    print("Scissors beats rock, I win round " + str(gameRound) + ".")
    print("")
    print("The current score is: You: " + str(scoreMe) + " vs CPU: " +
          str(scoreComp))

    continue

  elif opponenetChoice == 'S' and userChoice.upper() == 'P':

    gameRound += 1
    scoreComp += 1
    print("Scissors beats paper! I win round " + str(gameRound) + ".")
    print("")
    print("The current score is: You: " + str(scoreMe) + " vs CPU: " +
          str(scoreComp))

    continue

  elif opponenetChoice == 'P' and userChoice.upper() == 'R':

    gameRound += 1
    scoreComp += 1
    print("Paper beat rock, I win round " + str(gameRound) + ".")
    print("")
    print("The current score is: You: " + str(scoreMe) + " vs CPU: " +
          str(scoreComp))

    continue

  else:

    gameRound += 1
    scoreMe += 1
    print("You win round " + str(gameRound) + ".")
    print("")
    print("The current score is: You: " + str(scoreMe) + " vs CPU: " +
          str(scoreComp))
