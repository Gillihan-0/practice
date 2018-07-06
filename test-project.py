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

def cube( y ):
    return y * y * y
def doubleIt(z):
    return 2 * z

print("1 to 5 cubed")
for x in range (1,6):
    print (cube(x),)
print()
print()

print ("1 to 5 doubled")
for x in range (1,6):
    print(doubleIt(x),)

# So, basically... for x in range (1-6): >>> x becomes one through five. So When it says print(cube(x)) below, you have
# x = 1
# print(cube(x))


