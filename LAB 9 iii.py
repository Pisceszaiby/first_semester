def new_list(): #Function for Entering New List
    global list_num #list_num, num1, length will be used throughout the program
    global num1
    global length
    print("Press X to Stop getting Numbers") #X will prompt the user to operate on the numbers entered in the list
    num1=int(input("Enter first number: ")) 
    list_num=[num1] #First number will be stored in the list
    for i in list_num:
        i=input("Enter Number Again: ")
        if i!='X':
            list_num.append(int(i)) #All the numbers entered after the first one will be added to the list
    length=len(list_num) #length will store the length of the list using len()
def max_min_list(): #Function for finding Maximum and Minimum Number in the list
    maximum=num1 #Maximum variable will be initialized with the first num of the list
    for i in range(1,length):
        if maximum<=list_num[i]: #if maximum is not greater than next number then maximum takes the value of next number
            maximum=list_num[i]           
    print("Maximum Number in List is",maximum) #prints maximum number
    minimum=num1  #Minimum variable will be initialized with the first num of the list
    for i in range(1,length):
        if minimum>=list_num[i]: #if minimum is not smaller than next number then minimum takes the value of next number
            minimum=list_num[i] 
    print("Minimum Number in List is",minimum) #prints minimum number
def sort_list(): #Sorts the list in ascending order
    print("Current List: \n",list_num) #First prints the actual list
    for i in range(1,length+1): #loop works till the last item on the list
        for j in range(1,length+1-i): #inner loop checks for the iteration of i
            if list_num[j-1]>list_num[j]: #numbers will be replaced if the next number is smaller than the current number
                list_num[j-1],list_num[j]=list_num[j],list_num[j-1]
    print("Sorted List: \n",list_num)   #prints the sorted list                               
new_list() #Using this function first to enter numbers in the list    
print("\n A -- Enter the list of numbers again")
print("\n B -- Maximum and minimum numbers in the list ")
print("\n C -- Sum of the squares of each number in the list")
print("\n D -- Sort the list in ascending order")
print("\n E -- Exit the program") #Selection Menu
option=input("\nSelect Any Option from the given Operations: ") #option stores the letters from the selection menu
while (option!='A' and option!='a' and option!='B' and option!='b' and option!='C' and option!='c' and option!='D' and option!='d' and option!='E' and option!='e'):
    print("Invalid Selection") #For Invalid Selection
    option=input("Select Any Option from the given Operations: ") #Prompts the user to select again
while (option=='A' or option=='a' or option=='B' or option=='b' or option=='C' or option=='c' or option=='D' or option=='d' or option=='E' or option=='e'): #Loop for evaluating options from the selection menu
    if option=='A' or option=='a':
        new_list() #Function Call for new numbers for the next list
        
    elif option=='B' or option=='b':
        max_min_list()#Function call for maximum and minimum function
        
    elif option=='C' or option=='c':
        squared_sum = sum(map(lambda i : i * i,list_num))#Anonymous function is used with map function to find sum of squares of all the numbers in the list
        print("The Sum of Squares of Numbers in list: ",squared_sum)#Prints the squared_sum which is the result of the above function
        
    elif option=='D' or option=='d':
        sort_list()#Function Call for Sorting the list in Ascending Order
        
    elif option=='E' or option=='e':
        print("The user wishes to exit the program")
        exit() #Exits the program

    option=input("\nSelect Again Any Option from the given Operations: ") #Prompts the user to select Again
    
        
        
    
        
        
    
    
        





	
