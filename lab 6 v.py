num=int(input("Enter any natural number: "))
num1=num
reverse=0
while(num>0):
    reverse=(reverse*10)+(num%10)
    num=num//10

print("The reverse of",num1,"is",reverse)
if num1==reverse:
    print("The number",num1,"is a palindrome")
else:
    print("The number",num1,"is not a palindrome")
    
