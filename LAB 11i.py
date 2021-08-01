import math
def point_distance(x,y): #Here parameters x and y are tuples
    sq_distance=((y[0]-x[0])**2)+((y[1]-x[1])**2) #index[0] and [1] represent x and y coordinates respectively
    distance=float(math.sqrt(sq_distance)) #Using Distance formula
    return distance
points=int(input("Enter Number of Points: ")) #Number of Points
tuple_list=list() #Tuples will be stored in this List
for i in range(1,points+1):
    tuple_point=eval(input("Enter Point:")) #Tuple point will be entered in the form of (x,y)
    tuple_point=tuple(tuple_point) #Tuple point will be conveted to type tuple
    tuple_list.append(tuple_point) #All the tuple entries will be stored in the tuple list
temp=0
total_distance=0 
while temp<=points-2: #For points=3, index 2 will be the highest
    total_distance+=(point_distance(tuple_list[temp],tuple_list[temp+1]))#tuple_list[0] is the first tuple and second tuple is tuple_list[1] and so on
    temp+=1 
print("Total Distance between the",points,"points: %.2f"%total_distance)

