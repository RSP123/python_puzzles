# This program prints the lenght of the given string

# Function for the finding length

def string_function(string):
    len = 0
    for i in string:
        # Calculating length of string
        len = len + 1
    return len



if __name__ == "__main__":
    string = str(input("Enter a string here > "))    # User input
    print(string_function(string))
    # print("Given string is : ", string,"Length is : ", string_function(string))
