# This program check weather the given number is prime or not
# Function to check prime number

def prime_number(number):
	# Returning False for number 1 and less then 1
	if number == 2 or number == 1:
		return True
	elif number < 1 or number%2 == 0:
		return False
	else:
		# Iterating from 2 to check the number is prime or not
		for i in range(3, int((number/3))+1, 2):
			if (number%i) == 0:
			    return False
	return True


# Main function
def main():
	number=int(input("Enter a number to check weather it is prime or not: "))

	if number == 1:
		print("It's neither prime nor composite !!!")
		return None
	if prime_number(number):
		print("The given number => ", number, " is a prime number")
	else:
	    print("The given number => ", number, " is not a prime number")


# Checks the program call name
if __name__ == '__main__':
	main()
