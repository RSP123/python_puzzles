# This program gives largest number in the list

# Function for finding largest next_number

def largest_list(list_larger):
    max = list_larger[0]
    for b in list_larger:
        if b > max:
            max = b
    return max

# Main Function

if __name__ == "__main__":
    #Input from user
    list_larger=list(map(int,input("Enter the number >:").split()))
    print(largest_list(list_larger))
