# This program gives largest number in the list

# Function for finding largest next_number

def largest_list(list):
    max =list[-1]
    for i in range(i, i+1):
        if i > max:
            max = i
    return


if __name__ == "__main__":
    list = int(input("Enter three or more number to find larger number :> "))
    print(largest_list(list))
