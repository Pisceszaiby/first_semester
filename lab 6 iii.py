
num=int(input("Enter any odd number:"))
t=num
r = int((num + 1) / 2) #Formula to be used for rows
if num%2==0:
    print(num, "is not an odd number")
else:
    while num%2!=0 and 0<num<10: #Single digit odd numbers
        for row in range(1, r+1):
            if row == 1: #Prints the entered number in num numbers of time
                for k in range(num, 0, -1): #loop for the first row
                    print(num,end=" ")

                print()



            elif row==r : #Prints the last number i.e 1 in the middle of row only once

                for j in range(int(t+1/2),1,-1): #loop for the last row
                    print(end=" ")
                for j in range(1):
                    print(1,end=" ") 



            else:
                
                for k in range(0,row-1): #loop for the middle rows
                    print(end="  ")      #Double loops for printing numbers and printing spaces between the numbers
                print(num,end=" ")



                for k in range(num-2):
                    print(" ", end=" ")
                print(num,end=" ")

                print("\r")
                
            
            num -= 2# decrementing each number by 2 as an odd number is only applicable in the program
