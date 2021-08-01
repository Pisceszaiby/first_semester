num=int(input("Enter Number: "))
print("The multiplication table of",num, "is: ")
for mul in range(1,11):
    if mul<10:
        print(num, "x", mul," =",mul*num)
    else:
        print(num, "x", mul,"=",mul*num) #Used this staement for the correct format of
                                         #= sign as 2 digit number precedes it
