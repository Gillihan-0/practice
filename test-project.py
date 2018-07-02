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



# def checkio(data: str) -> bool:
#
#     #replace this for solution
#     return True or False
#
# #Some hints
# #Just check all conditions


# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio('A1213pokl') == False, "1st example"
#     assert checkio('bAse730onE4') == True, "2nd example"
#     assert checkio('asasasasasasasaas') == False, "3rd example"
#     assert checkio('QWERTYqwerty') == False, "4th example"
#     assert checkio('123456123456') == False, "5th example"
#     assert checkio('QwErTy911poqqqq') == True, "6th example"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


# while loops repeat code because true will always be true. Therefore the code will always repeat

totalScore = 0
scoreCount = 0

while True:
    score = input("Enter a score here. (type 'end' to end)\n")
    if score == 'end':
        average = totalScore / scoreCount
        print("Your average is", round(average,2))
        break
    score = int(score)
    totalScore += score
    scoreCount += 1



