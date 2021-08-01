num=int(input("Enter Number of elements in the list: "))
num_list=[] #For NewNumList() function, numbers will be stored here
frequency=list() #Initializing lists
sorted_frequency=list()
def NewNumList():
    print("Enter Numbers after each line")
    for i in range(num):
        element=int(input(''))
        num_list.append(element)
    print("Original List is",num_list)
    return num_list #This function takes all the numbers to append in the list
list1=NewNumList() #List1 will be used for checking frequency of elements
list2=list(list1) #List2 is a copy of List1 with all the original elements without modification
def frequency_list(): #This function makes an array of frequency (of more than 1) of elements 
    for i in list1:
        freq=list1.count(i)
        if freq>1:
            frequency.append(freq)
            while freq>1:
                list1.remove(i) #Remove is used here to avoid repetition of the frequency of the same element
                freq=freq-1
    return frequency
length=len(frequency_list())

def sorting_list(frequency):
    for i in range(0,length-1): #Here Sorting is used in reverse order to store highest frequency first till the lowest
        for j in range(1,length-i):
            if frequency[j-1]<=frequency[j]:
                temp=frequency[j-1] #Swapping of elements in the list
                frequency[j-1]=frequency[j]
                frequency[j]=temp    
    return frequency #Now the frequency is sorted

sorted_frequency=sorting_list(frequency) #Sorted_frequency is stored with sorted frequency

print("\tFREQUENCY \tITEM")
for j in sorted_frequency:    
    for i in list2: 
        if list2.count(i)==j and j>1: #if the number of elemnts in the list matches the highest frequency, the element alongwith frequency will be printed
            print("\t",j,"\t\t",i)
            while j>1:
                list2.remove(i) #Here remove is used to avoid repetition of printing elements 
                j-=1
print("New List without Duplicates",list1) #List1 is without duplicated elements, so the list will be printed.
        
    
    
    

    
