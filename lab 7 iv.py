def factorial(num):
    prod=1
    for i in range(1,num+1):
        prod=i*prod
    return prod

n=int(input("Enter any number: "))
temp=n
s=0
t='y'
while t=='y' or t=='Y':
    while(n):
        x=int(n%10)
        y= factorial(x)
        s+=y
        n=n//10
    if(s==temp):
        print(temp,"is a strong number")
    else:
        print(temp,"is not a strong number")

    print("\nPress y to continue or Press q to quit the program")
    t=input("Enter y or q: ")
    if t=="y" or t=="Y":
        n=int(input("Enter any number: "))
        temp=n
        s=0
    elif t=="q" or t=="Q":
        print("Program Ended")
        exit()
    else:
        print("Program Ended")
