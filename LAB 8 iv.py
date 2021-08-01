import math 
num = int(input("Enter Number to find Next Prime: "))
def nextPrime(num):   
    def is_prime(num):  
        for i in range(2,num): 
            if (num <=1):
                return False 
            if (num<=3):
                return True 
            if(num%2==0 or num%3==0):
                return False 
            for i in range(5,int(math.sqrt(num))+1,6):
                if num%i==0 or num%(i+2)==0: 
                    return False
            return True               
    for nextnum in range(num+1,2*num):   
        if is_prime(nextnum)==True: 
            return nextnum
num=str(num)       
while(num.isdigit()==True):
    num=int(num)
    print ("Next Prime is : ",nextPrime(num)) 
    num = input("Enter Number to find Next Prime: ")
    if num.isdigit()==False: 
        print("YOU HAVE ENTERED AN INVALID CHARACTER")
