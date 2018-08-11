#average calculator

import time


def cls():
    print("\n " * 25)


def average():
    count = 0
    total = 0

    while True:
        number = input("Enter a number, [c]alculate or [q]uit: ")
        if number.isnumeric():
            number = int(number)
            count += 1
            total += number

        elif number == 'c' or number == 'C':
            average = total / count
            average = round(average, 2)
            print()
            print(f"The average is {average}")
            print()
            count = 0
            total = 0

        elif number == 'q' or number == 'Q':
            cls()
            print("Quitting.")
            time.sleep(1)
            break

        else:
            cls()
            print("Invalid command.")


if __name__ == "__main__":
    print("This program calculates the average of all the numbers you enter.")
    time.sleep(1)
    average()
