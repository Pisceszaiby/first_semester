print("Enter Quit to leave the program")
expression=input("Enter Any Expression To Be Evaluated: ") #Expression stores the entered expression by the user
while(expression!='Quit'): #Loop Continues unless user enters Quit
    result=eval(expression) #eval function evaluates the expression and stores the result in store
    print("Evaluated Result is :",result)
    expression=input("Enter Any Expression To Be Evaluated: ") 
if expression=='Quit': #exit() is used when the user finally enters Quit
    print("User wishes to quit the program")
    exit()

