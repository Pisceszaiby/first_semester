print("Count sum of 10 even numbers entered by the user")
n=10
s=0
while n<=10 and n>0:
    print("Remaining Numbers: ",n,end="\t")
    x=int(input("Enter any even Number:"))
    s+=x
    if x%2!=0:
         print(x,"is not an even number, Try Again.")
         n+=1
         s=s-x
    n-=1
print("The sum of 10 even numbers is",s)
    
