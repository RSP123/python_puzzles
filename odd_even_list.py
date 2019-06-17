# This program prints separetes odd and even in the new_list

# Function to finding odd or even
def odd_even(list):
    # Checking for odd element
    new_even = []
    new_odd = []
    lis = []
    for i in list:
        if (i%2) != 0:
            new_odd.append(i)
        else:
            new_even.append(i)
        lis = new_odd + new_even
    return lis

# Main
if __name__ == "__main__":

    list = [1, 26, 3, 34, 5, 56, 7, 28, 2, 10]

    # print(type(odd_even(list)))
    print(odd_even(list))
