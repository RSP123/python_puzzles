# This program check weather the given number is prime or not
# Function to check prime number

def prime_number(number):
	# Returning False for number 1 and less then 1
	if number == 1 or number < 0:
		return False

	# Iterating from 2 to check the number is prime or not
	for i in range(2, number):
		print(i)
		if (number % i) == 0:
		# Returns False if the number is even
			return False
		else:
			return True


def main():
	# Main function
	number=int(input("Enter a number to check weather it is prime or not: "))
	if prime_number(number):
		print("The given number => ", number, " is a prime number")
	else:
	    print("The given number => ", number, " is not a prime number")

# Checks the program call name
if __name__ == '__main__':
	# NOTE: This block runs when the user compiles this file only ***
	main()
