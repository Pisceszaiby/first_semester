        
def check_disarium(): #Main Function to check Disarium 
    n=(input("Enter Number: "))# n is a string,Number to be identified
    global Num#Num will be used outside the function body
    temp=int(n) #temp is a temporary variable to store int(n)
    length=0 #Length and Sum are initialized 0
    Sum=0
    num=len(n) #where num stores the number od digits in n 
    length=int(num)#Length is now integer type variable
    n=temp   #n is now an integer,ready for arithmetic/logical computation
    while(n):
        x=int(n%10) #x stores the last place digit first
        y= x**length     #x is raised to the power length and the result is stored in y
        Sum+=y #y is added in the sum with every iteration
        n=n//10 #n is divided to decrease place values by 1
        length=length-1#hence length is also decremented by 1
    if Sum==temp: #if final sum is equal to temp, the number which stored the actual number
        print(temp,"is a valid disarium number")#then the number is disarium
        Num=True
    else:
        print(temp,"is not a valid disarium number")#otherwise it is not
        Num=False
              
Num=False   #if n is not disarium and has False truth value         
while (Num==False):    #then loop will continue till a True value is obtained   
    check_disarium() #Function is called to check disarium Number


