#This program print the circumference and area of the circle
PI = 3.14

#Function to calculate the circumference
def circumference_circle(radius):
    ci = PI * 2 * radius
    return ci

#Function to calculate the area
def area_circle(radius):
    area = PI * radius * radius
    return area

#Main Function
def main():
    # This function can be called from  another program to know the \
    # flow of the program
    radius = float(input("Enter the Radius of circle >> "))
    ci=circumference_circle(radius)
    area=area_circle(radius)

    print("Circumference of Cirlce is %.5f:" %ci, "Area of circle is :%f" %area )



if __name__ == "__main__" :
    # This block executes if this program is dicrectly called or executed by the user

    radius = float(input("Enter the Radius of circle >> "))
    ci=circumference_circle(radius)
    area=area_circle(radius)

    #Prints the values of circumference and area of circle
    print("Circumference of Cirlce is %.5f:" %ci, "Area of circle is :%f" %area )
