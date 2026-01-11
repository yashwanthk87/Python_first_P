import random

computer = random.choice([-1, 0, 1])

choice = input("Enter your choice: ")

choiceDict = {"s": -1, "w": 0, "g": 1}

yourchoice = choiceDict[choice]

choosenOption = {-1: "snake", 0: "water", 1: "gun"}

print(f"you choose {choosenOption[yourchoice]} \n The computer choose {choosenOption[computer]}")

if (computer == yourchoice):
    print("Draw")

else:
    if (computer == -1 and yourchoice == 1):
        print("You won!")
    elif (computer == 1 and yourchoice == -1):
        print("You lost!")
    elif (computer == 0 and yourchoice == -1):
        print("You lost!")
    elif (computer == -1 and yourchoice == 0):
        print("You won!")
    elif (computer == 0 and yourchoice == 1):
        print("You lost")
    elif (computer == 1 and yourchoice == 0):
        print("You won!")
    else:
        print("Something went wrong, Try again!")