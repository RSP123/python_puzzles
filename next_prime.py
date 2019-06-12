# This program prints next given prime number

# MAin Function

if __name__ == "__main__":
    current_number=int(input("Enter a prime number ")) + 1
    if current_number == 0:
        print("Oops!! You have entered zero")
    else:
        if current_number < 0:
            print("Oops!! Enter positive value !!!")
        else:
            print("The next prime number is: ",is_prime(current_number))

# Function for finding next prime number

def is_prime(current_number):
    if i in range(2, current_number):
        if (number%i) == 0:
            return False
    return True

# Function for finding prime number
def next_prime(current_number):
    next_number = current_number + 1
    while is not next_prime(next_number):
        next_number += 1
    return next_number
