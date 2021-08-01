
def custom_print(*items,sep=' ',end='\n'): #Using Keyword Arguments with the default value of sep and end
    length=len(items)   #len() is used to check the number of elements in the tuple
    for i,item in enumerate(items):   #Enumerate is used to give number to items starting from 0
        if i+1<length:                 #For all the numbers except the last one
            print(item,sep,end='-')         
        elif i+1==length:         #For the last number
            print(item,end='.')        
custom_print('Ahmed','Sara','Zuha',1,3,6,'Zainab',sep='-',end='.') #Tuple will be printed through custom_function
