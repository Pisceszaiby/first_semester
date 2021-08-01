
def miles_km(miles):
    print('"Conversion of Miles to Km"')
    print("Length in Miles: ", miles)
    km=miles*1.609
    print("Length in Km: ",km)

def Cel_F(c):
    print('"Conversion of Celcius to Fahrenheit"')
    print("Temperature in Celcius: ", c)
    f=((c*1.8)+32.00)
    print("Temperature in Fahrenheit: ",f)

def feet_m(feet):
    print('"Conversion of Feet to Meters"')
    print("Length in feet: ", feet)
    m=feet*0.3048
    print("Length in meters: ",m)

def yards_m(yards):
    print('"Conversion of Yards to Meters"')
    print("Length in yards: ", yards)
    m=yards*0.9144
    print("Length in meters: ",m)



print(' a="Miles to Km"\n','b="Celsius to Fahrenheit"\n','c="Feet to meters"\n','d="Yards to meters"\n','e="Exit program"\n')
x=input("Press from a to e to perform the above specific tasks:")
if  (x!='a' and x!='b' and x!='c' and x!='d' and x!='e'):
    print("Invalid letter, Try Again")
    x=input("Press from a to e to perform the above specific tasks:")
elif x=='e':
    print("User wants to Exit Program",exit())
while(x=='a' or x=='b' or x=='c' or x=='d' or x=='e' ):
    
    if x=='a':
        miles=int(input("Enter Length in Miles: "))
        miles_km(miles)
    if x=='b':
        c=int(input("Enter Temperature in Celcius: "))
        Cel_F(c)
    if x=='c':
        feet=int(input("Enter Length in feet: "))
        feet_m(feet)
    if x=='d':   
        yards=int(input("Enter Length in yards: "))
        yards_m(yards)
    if x=='e':
        print("User wants to Exit Program",exit())
    print("\n")
    x=input("Press from a to e to perform the specific tasks:")
