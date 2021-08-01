x=int(input("Enter first integer:"))
y=int(input("Enter second integer:"))
z=int(input("Enter third integer:"))
if x>y and x>z:
    print(x,"is the largest")
elif y>x and y>z:
    print(y,"is the largest")
else:
    print(z,"is the largest")

if x<y and x<z:
    print(x,"is the smallest")
elif y<x and y<z:
    print(y,"is the smallest")
else:
    print(z,"is the smallest")
