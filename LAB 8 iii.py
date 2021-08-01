import math
def show_difference():
    length=int(input("Enter length of the rectangle: "))#Length of Rectangle
    width=int(input("Enter width of the rectangle: "))#Width of Rectangle
    ellipse=None #ellipse and circle will be used in the inner program
    circle=None
    def area_calculation(length,width):
        nonlocal ellipse
        nonlocal circle
        ellipse=(length/2)*(width/2)*3.14   #Formula of area of ellipse is a*b*pi where a and b
        #are major and semi major axis
        circle=((math.sqrt((length**2)+(width**2)))/2)**2*(3.14)#Here Pythagoras formula is used to find the hypotenuse
        #which is in this case the diametre of the cirlce. SO the area of circle is ((diametre)/2)^2*pi  
        return ellipse,circle
    area_calculation(length,width)
    print("Area of ellipse is ",ellipse)
    print("Area of circle is ",circle)
    print("Difference of Area is ",circle-ellipse)

show_difference()    
