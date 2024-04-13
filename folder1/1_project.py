print("**GUESS THE NUMBER**")

import random

target = random.randint(1,100)

while True:
    userchoice = input("Guess the number or Quit: ")
    if (userchoice == "Quit"):
        break
    elif (userchoice == "quit"):
        break

    userchoice = int(userchoice)
    if (userchoice == target):
        print("Sucess : correct guess!!")
        break
    elif (userchoice < target):
        print("Your number was too small. Take a bigger guess..")
    else:
        print("Your number is too big. Take a smaller guess..")

print("----GAME OVER----")