# Dice Roller
import random


def rollDice(dice, sides):
    print(f"Rolling {dice}d{sides}...")
    total = 0
    for x in range(0, dice):
        die = random.randint(1, sides)
        total += die
        print()
        print(f"--= [{die}] =--")
    print()
    print(f"The dice total {total}")


if __name__ == "__main__":

    print("Welcome to Dicey's Ultimate Dice Thrower.")
    sides = 1
    dice = 1
    print(f"Currently rolling {dice}d{sides}")
    while True:
        print()
        command = input("[R]oll the dice, [C]hange die or [Q]uit.\n")
        if command == 'r' or command == 'R':
            rollDice(dice, sides)
        elif command == 'c' or command == 'C':
            try:
                sides = int(input("How many faces are on your die?\n"))
                dice = int(input("How many dice are you going to roll?\n"))
                if sides < 1 or dice < 1:
                    print()
                    print("Your (non-existent) die was eaten by a grue. You have lost.")
                    quit()
            except ValueError:
                print()
                print("Invalid input. Input must be an integer. Try again.")
                print()
        elif command == 'q' or command == 'Q':
            print()
            print("Thanks for using Dicey's Ultimate Dice Thrower.")
            break
        else:
            print()
            print("Invalid input. Try again.")
            print()