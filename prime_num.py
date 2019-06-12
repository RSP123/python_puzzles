# This program check weather the given number is prime or not
# Function to check prime number
def prime_number(number):
	# Checking number equals to 1
	if (number == 1)!=(number < 0):
		return False
	for i in range(2, number):
	   	if (number % i) == 0:
	    	# When condition is true
		   	return False
	else:
        	# When condition is false
			return True
""" 2 line indentation ??? """
# Main Function """ Is this main function ????"""
if __name__ == '__main__':
	# Getting a number from the user
	number=int(input("Enter a number to check weather it is prime or not: "))
    # Input from user
	if prime_number(number):
		print("The given number => ", number, " is a prime number")
	else:
	    print("The given number => ", number, " is not a prime number")
