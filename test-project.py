def avgscript():
    total = 0.0
    count = 0
    print ("this is an average calculator.")
    variable1 = float(input("Enter how many numbers are you going to average out?\n"))
    while count < variable1:
        number = float(input("Enter a number here: \n"))
        total = total + number
        count = count + 1
    average = total / variable1
    print (f"the average is {average}")
avgscript()

question = input("Do you wish to calculate again? y/n: \n")

if question == "y":
    avgscript()