# This program gives largest number in the list

# Function for finding largest next_number

def largest_list(list):
    max =list[-1]
    for i in range(i, i+1):
        if i > max:
            max = i
    return


if __name__ == "__main__":
    element = int(input("Enter the element to find largest element in list :> "))
    for i in range(1, element+1):
        a=int(input("Enter the number >:"))
        list.append(a)
    print(largest_list(list))
