#number guesser
import random


def guess():
    while True:
        count = 0
        theNumber = random.randint(1, 20)
        found = False

        while found == False:

            answer = input("Guess a number: ")
            answer = int(answer)
            count += 1
            if answer == theNumber:
                print("Great job! You guessed the right number.")
                if count == 1:
                    print("You found the number on your first guess.")
                    found = True
                elif count > 1:
                    print(f"It took you {count} tries to guess correctly.")
                    found = True
            elif answer < theNumber:
                print("Your answer is less than the number. Try again.")
            elif answer > theNumber:
                print("Your answer is greater than the number. Try again.")

        replay = input("Do you want to play again?")
        if replay == "y":
            count = 1
            continue
        else:
            break


if __name__ == "__main__":

    print("Hello and welcome to the random number guesser. Your job is to guess a randomly generated number between 1"
          " and 20.")
    guess()

