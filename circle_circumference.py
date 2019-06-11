#This program print the circumference and area of the circle
PI = 3.14
#Function to calculate the circumference
def circumference_circle(radius):
    ci = PI * float(2.0*radius)
    #Prints the circumference
    return ci

#Function to calculate the area
def area_circle(r):
    area = PI * float(radius^2)
    #Prints the area
    return area
 
radius = float(input("Enter the Radius of circle >> "))
circumference_circle(r)
area_circle(r)
print("Circumference of Cirlce is :"+ci, "Area of circle is :" +area )
