# This program gives largest number in the list

# Function for finding largest next_number

def largest_list(list_larger):
    max = list_larger[0]
    for b in list_larger:
        if b > max:
            max = b
    return max


if __name__ == "__main__":
    element = int(input("Enter the element to find largest element in list :> "))
    for i in range(1, element+1):
        list_larger=list(map(int,input("Enter the number >:").split()))
        # list.append(a)
    print(largest_list(list_larger))
