# def avgscript():
#     total = 0.0
#     count = 0
#     print ("this is an average calculator.")
#     variable1 = float(input("Enter how many numbers are you going to average out?\n"))
#     while count < variable1:
#         number = float(input("Enter a number here: \n"))
#         total = total + number
#         count = count + 1
#     average = total / variable1
#     print (f"the average is {average}")
# avgscript()
#
# question = input("Do you wish to calculate again? y/n: \n")
#
# if question == "y":
#     avgscript()





# score = input("Etner a score:")
# score = int(score)
# if score >= 80:
#     grade = 'A'
# else:
#     if score >= 70:
#         grade = 'B'
#     else:
#         if score >= 55:
#             grade = 'C'
#         else:
#             if score >= 50:
#                 grade = 'Pass'
#             else:
#                 grade= 'Fail'
# print("\n\nGrade is: " + grade)






# while loops repeat code because true will always be true. Therefore the code will always repeat

# totalScore = 0
# scoreCount = 0
#
# while True:
#     score = input("Enter a score here. (type 'end' to end)\n")
#     if score == 'end':
#         average = totalScore / scoreCount
#         print("Your average is", round(average,2))
#         break
#     score = int(score)
#     totalScore += score
#     scoreCount += 1




# print("This is the start of the program")
# answer = 'y'
# while answer == 'y' or answer == 'Y':
#     print("This is a statement from within the while loop")
#     print("And some more stuff from within the while loop")
#     answer = input("Do you want to run this program again? y/n\n")
# print("Goodbye.")





# This is how these functions are set up, I guess

# def many_greetings_with_name(n, the_name):
#     for i in range(n):
#         print("Hello Again" + the_name + "!")
#
# x = int(input("How many greetings do you want?: "))
# many_greetings_with_name(x, " lololo")





# This explains what the first variable in 'for x in range whatever' can do

# def cube( y ):
#     return y * y * y
# for x in range (1,5):
#     print(cube(x))
# print(f"The last value of x is {x}")

# def cube( y ):
#     return y * y * y
# def doubleIt(z):
#     return 2 * z
#
# print("1 to 5 cubed")
# for x in range (1,6):
#     print (cube(x),)
# print()
# print()
#
# print ("1 to 5 doubled")
# for x in range (1,6):
#     print(doubleIt(x),)

# So, basically... for x in range (1-6): >>> x becomes one through five. So When it says print(cube(x)) below, you have
# x = 1
# print(cube(x))



#importing from another file in the same project folder
# import myFunctions
#
# print ("1 to 5 cubed")
# for x in range (1,6):
#     print (myFunctions.cube(x))
# print()
# print()
# print("1 to 5 doubled")
# for x in range (1,6):
#     print (myFunctions.doubleIt(x),)





# # creating and using python lists
# result = [0, 0, 0, 0, 0, 0, 0, 0]
# print(result)
# result[0] = 75
# result[1] = 90
# result[4] = 72
# print(result)
# print(result[0])
# print(result[1])
# print(result[2])
# print(result[3])
# print(result[4])
# print(result[5])
# print(result[6])
# print(result[7])




# # demonstrates rows and columns on lists?
# tictactoe = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# print(tictactoe[0])
# print(tictactoe[1])
# print(tictactoe[2])
# print(tictactoe[3])
#
# print(tictactoe[3][1])
#
# row = 1
# column = 0
# the_value = (tictactoe[row][column])
# print(f"Row {row} column {column} has a value of {the_value}")




# # for every character in a string...
# s = 'steven was here'
# for c in s:
#     if c == 'e':
#         print(c, end="000")
#     else:
#         print(c, end="")
# print()
# print('bill' in s)
# print('steven' in s)
# print(' ' in s, end=" ")
# print('x' in s)



# # DOING STUFF TO FILES WOOOOOOOOOOO

# 'r' is read
# 'w' is write
# {filename}.open
# {filename}.write
# {filename}.close
# {filename}.read
# {filename}.readline


# file1 = open('C:\\Users\\sgillihan\\Documents\\doc1.txt','r')
# # the line above opens C:\temp\file1.txt for reading
# string = file1.readline()
# print (string)


# file1 = open('C:\\Users\\Sgillihan\\Documents\\doc1.txt', 'w')
# print(file1)
# file1.write("Today is Tuesday\n")
# file1.write("Tomorrow is Wednesday")
# file1.close()

# file2 = open('C:\\users\\sgillihan\\documents\\doc1.txt', 'r')
# print(file2)
# string1 = file2.read()
# print(string1)
# file2.close()
# file2 = open('c:\\users\\sgillihan\\documents\\doc1.txt', 'r')
# string1 = file2.read(5)
# print (string1)
# string1 = file2.read(5)
# print (string1)
# string1 = file2.read(5)
# print (string1)
# file2.close()


# def copy_file(oldFile, newFile):
#     f1 = open(oldFile, "r")
#     f2 = open(newFile, "w")
#     while 1:
#         text = f1.read(50)
#         if text == "":
#             break
#         f2.write(text)
#     f1.close()
#     f2.close()
#     return
#
# filecopy = "c:\\users\\sgillihan\\documents\\doc1copy.txt"
# fileold = "c:\\users\\sgillihan\\documents\\doc1.txt"
# copy_file(fileold, filecopy)




# filename = input('Enter a file name: ')
# try:
#   f = open (filename, "r")
# except:
#   print ('There is no file named', filename )




# list1= [14, 15, 16, 17, 18, 19, 20, 21]
# goodnumber = int(input("How many years does it have?\n"))
# found = 0
# for i in list1:
#     if goodnumber == i:
#         print("Very good")
#         found = 1
# if found == 0:
#     print("Not good enough")




# def theFunc():
#     myList=[1, 3, 5, 7, 10, 20, 30, 40]
#     n = len(myList)
#     search = int(input("\nPlease enter a number to search for: "))
#     found = False
#     for i in range(n):
#         if myList[i] == search:
#             found = True
#             index = i
#     print()
#     if found == True:
#         tryAgain = input((f"You found {search} at index {index}. Try again? y/n?"))
#         if tryAgain == 'y':
#             theFunc()
#         else:
#             quit(0)
#     else:
#         print("Search not found. Try again.")
#         theFunc()
# theFunc()



# import random
# numberslist = []
# number = 0
# while number < 10000:
#     value = random.randint(1,20000)
#     if not(value in numberslist):
#         numberslist.append(value)
#         number += 1
# print(numberslist)




# import random
#
# # define the bubble sort function
# def sort(values):
#    length = len(values)
#    for time in range(0, length-1):
#       for position in range(0, (length-time-1)):
#          if values[position] > values[position+1]:
#             values[position], values[position+1] = values[position+1], values[position]
#
# # generate a list of ten random numbers
# numbers = []
# number = 0
# while number < 10:
#    value = random.randint(1,100)
#    if not(value in numbers):
#       numbers.append(value)
#       number = number + 1
#
# # show unsorted list, sort the list, and show sorted list
# print ("Before:", numbers)
# sort(numbers)
# print ("After :", numbers)


# MY PROGRAMS ----------------------------------------------------------------------------------------------------------

# Dice Roller
# import random
#
#
# def rollDice(sides):
#     dice = random.randint(1, sides)
#     print()
#     print(f"--= [{dice}] =--")
#     print()
#     init(sides)
#
#
# def init(sides):
#     command = input("[R]oll the dice, [C]hange die or [Q]uit.")
#     if command == 'r' or command == 'R':
#         rollDice(sides)
#     elif command == 'c' or command == 'C':
#         print()
#         choseSides()
#     elif command == 'q' or command == 'Q':
#         print("Thanks for using Dicey's Ultimate Dice Thrower.")
#         quit()
#     else:
#         print()
#         print("Invalid input. Try again.")
#         print()
#         init(sides)
#
#
# def choseSides():
#     try:
#         sides = int(input("How many faces are on your die?"))
#         if sides > 0:
#             print()
#             init(sides)
#         else:
#             print()
#             print("Your (non-existent) die was eaten by a grue. You have lost.")
#             quit()
#     except ValueError:
#         print()
#         print("Invalid input. Sides must be an integer. Try again.")
#         print()
#         choseSides()
#
#
#
#
#
# print("Welcome to Dicey's Ultimate Dice Thrower.")
# choseSides()


from diceroller import rollDice

print(rollDice(4,6))