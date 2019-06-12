# This program gives radius of circle, when area is given

PI = 3.14

# Function for radius calculation

def radius_of_circle(area):
    radius= (area/PI) ** 0.5
    return radius

# Main function

if __name__ =='__main__':
    area=float(input("Enter the area of circle: "))
    # radius_of_circle(area)
    print("Radius of circle is: %f " %radius_of_circle(area))
