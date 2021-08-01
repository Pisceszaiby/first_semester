import math
  
def points_distance(x1,x2,y1,y2):
    horizontal=x2-x1
    vertical=y2-y1
    sq_distance=(horizontal**2)+(vertical**2)
    distance=float(math.sqrt(sq_distance))
    print("Distance between the two points is",distance)
    return distance

x1=float(input("Enter 1st X coordinate: "))
x2=float(input("Enter 2nd X coordinate: "))
y1=float(input("Enter 1st Y coordinate: "))
y2=float(input("Enter 2nd Y coordinate: "))  

points_distance(x1,x2,y1,y2)


