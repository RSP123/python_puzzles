# This program prints next given prime number

# Function for finding next prime number
def is_prime(current_number):
    limit = current_number * 2
    # Current_number checking with prime Function
    for i in range(current_number,limit):
        if prime_number(i):
            return i


# Prime Function
def prime_number(number):
	# Returning False for number 1 and less then 1
	if number == 2 or number == 1:
		return True
	elif number < 1:
		return False
	else:
		# Iterating from 2 to check the number is prime or not
		for i in range(3, int((number/3))+1, 2):
			if (number%i) == 0:
			    return False
	return True



# Main
if __name__ == "__main__":
    current_number=int(input("Enter a prime number ")) + 1
    print("The next prime number is: ",is_prime(current_number))
