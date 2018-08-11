import time, diceroller, numberguesser, avgcalculator


def cls():
    print("\n " * 25)


print("Welcome to the test program hub.")
time.sleep(1)
print()
print("Program 1 = Diceroller")
print("Program 2 = Number Guesser")
print("Program 3 = Average calculator")
while True:
    print()
    print()
    progselect = input("You are inside the main loop. Program[1], program[2], program[3] or [Q]uit: ")
    print()
    print()

    if progselect == '1':
        while True:
            print("You chose program 1. Enter 'back' at any point to return to the main program.")
            print()
            x = input("chose the number of dice: ")
            if x == 'back':
                break
            y = input("chose the number of sides: ")
            if y == 'back':
                break
            x = int(x)
            y = int(y)
            diceroller.rollDice(x,y)

    elif progselect == '2':
        while True:
            print("You are in program 2.")
            print()
            command = input("Proceed with number guesser? y/n: ")
            if command == 'y':
                numberguesser.guess()
            else:
                break

    elif progselect == '3':
        while True:
            print("You are in program 3.")
            print()
            command = input("Proceed with average calculator? y/n: ")
            if command == 'y':
                avgcalculator.average()
            else:
                break
    elif progselect == 'q' or progselect == 'Q':
        cls()
        print("Quitting.")
        time.sleep(1)
        break

    else:
        print("Invalid command.")
