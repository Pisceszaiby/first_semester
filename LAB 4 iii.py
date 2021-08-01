a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))
if (a*a)==(b*b)+(c*c) or (b*b)==(a*a)+(c*c) or (c*c)==(b*b)+(a*a):
    print("These are the sides of Right-Angeled triangle.")
else:
    print("These are not the sides of Right-Angeled triangle.")
