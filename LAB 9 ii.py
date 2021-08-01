from area import Area_Calculation #Using Module from area
import math    
def cylinder_surface_area(): #Function to find Surface Area of Cylinder
    Radius=int(input("Enter Radius: "))
    height=int(input("Enter Height: "))
    Area=(2*math.pi*Radius*height)+(2*math.pi*Radius*Radius)
 #Formula for Surface Area of Cylinder
    print("Surface Area of Cylinder is ",Area) #Surface area will be printed
    return Area
#Selection Menu for Finding Area of Given Shapes
print("\t\tT-For Area of Triangle")
print("\n\t\tC- For Area of Circle")
print("\n\t\tR-For Area of Rectangle")
print("\n\t\tS-For Surface Area of Cylinder") 
print('\n\t\tE-To exit the program')
shape=input("\nSelect your Choice: ") #Here shape will store the selection option
while shape!='T' and shape!='t' and shape!='r' and shape!='R' and shape!='C' and shape!='c' and shape!='S' and shape!='s' and shape!= 'E' and shape!= 'e':
    print("Invalid Selection") #if the selection option is not from the menu
    shape=input("\nSelect your Choice: ") #In this case user will again enter shape.
while shape=='T' or shape=='t' or shape=='r' or shape=='R' or shape=='C' or shape=='c' or shape=='S'or shape=='s' or shape=='E' or shape== 'e':#Loop for valid Choice
#If the shape is S,T,C then function area_calculation will be used, furthermore the area #of the shape will be printed according to the shape input constant
    if shape=='t'or shape=='T' or shape=='r' or shape=='R' or shape=='C' or shape=='c':
        Area_Calculation(shape)
    elif shape=='S' or shape=='s': #For Surface Area of Cylinder
        cylinder_surface_area() #Function exists in the main program
    elif shape== 'E' or shape== 'e': #For exiting the program
        print('\nUser wishes to exit the program') 
        exit()    
    shape=input("\nSelect your Choice Again: ")
 #Once a function is called, Again the user will be prompted to select.
