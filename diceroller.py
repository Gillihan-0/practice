# Dice Roller
import random


def rollDice(dice, sides):
    total = 0
    if dice > 1 and sides > 1:
        print(f"Rolling {dice}d{sides}...")
        for x in range(0, dice):
            die = random.randint(1, sides)
            total += die
            print()
            print(f"--= [{die}] =--")
            print()
        return total
    else:
        print("Please chose a valid die configuration.")


if __name__ == "__main__":
    print()
    print()
    print("Welcome to Dicey's Ultimate Dice Thrower.")
    print()
    print()
    sides = 6
    dice = 2
    print(f"Currently rolling {dice}d{sides}")
    while True:
        command = input("[R]oll the dice, [C]hange die or [Q]uit.\n")
        if command == 'r' or command == 'R':
            dicetotal = rollDice(dice, sides)
            print(f"The dice total {dicetotal}")
        elif command == 'c' or command == 'C':
            try:
                dice = int(input("How many dice are you going to roll?\n"))
                sides = int(input("How many faces are on your die?\n"))
                if sides < 1 or dice < 1:
                    print("Chose a positive, nonzero number.")
            except ValueError:
                print("Invalid input. Input must be an integer. Try again.")
        elif command == 'q' or command == 'Q':
            print("Thanks for using Dicey's Ultimate Dice Thrower.")
            break
        else:
            print("Invalid input. Try again.")