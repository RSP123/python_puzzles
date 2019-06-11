#This program gives radius of circle, when area is given
import math
PI = 3.14
#Function for radius calculation
def radius_of_circle(area):
    radius= math.sqrt((area/PI))
    return radius
#Main function
if __name__ =='__main__':
    area=float(input("Enter the area of circle:"))
    # radius_of_circle(area)
    print("Radius of circle is:%f" %radius_of_circle(area))
