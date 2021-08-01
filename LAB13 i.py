expression=input("Please enter any arithmetic expression: ") #Expression will be entered by User
while expression!='Exit':
    if expression=='History': #To view History
        print("\nHistory of all entered Expressions: ")
        with open('exp.txt') as file:
            for line in file:
                print(line, end="") #Each line the file will be printed
    elif expression=='Clear': #To clear History
        with open('exp.txt','w') as file:
            file.write('')#File will be overwritten by a space
        print("\nAll previous entries have been removed")
    else:
        
        try:
            print("\nResult: ",eval(expression))
            with open('exp.txt','a') as file: #Expression will be evaluated and result will be displayed if it is valid
                file.write(expression)
                file.write("\n")
        except Exception as e: #otherwise error will be shown
            print("\n ERROR: ",e)
    print("\nEnter History to view all previous entries, Clear to clear all entries and Exit To Exit the program or simply write an expression")        
    expression=input("Enter your Choice/Expression: ")    
print("User wishes to exit the program")     #User will be prompted to enter choice, if Exit is entered Program will end
exit()
