# This program prints separetes odd and even in the new_list

# Function to finding odd or even
def odd_even(list):
    for i in list:
        new = []
        # Checking for odd element
        if (i%2) != 0:
            new.append(i)
        # Checking for even element
        elif (i%2) == 0:
            new.append(i)
    return new

# Main
if __name__ == "__main__":

    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(type(list))
    print(odd_even(list))
