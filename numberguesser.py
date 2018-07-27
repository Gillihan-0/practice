import random

print("Hello and welcome to the random number guesser. Your job is to guess a randomly generated number between 1"
              "and 20.")
while True:
    theNumber = random.randint(1, 20)

    found = False

    while found == False:

        answer = input("Guess a number: ")
        answer = int(answer)
        if answer == theNumber:
            print("Great job! You guessed the right number.")
            found = True
        elif answer < theNumber:
            print("Your answer is less than the number. Try again.")
        elif answer > theNumber:
            print("Your answer is greater than the number. Try again.")


    replay = input("Do you want to play again?")
    if replay == "y":
        continue
    else:
        quit(1)