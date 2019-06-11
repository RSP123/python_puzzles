#This program check weather the given number is prime or not
#Function to check prime number
def prime_number(number):
    if number%2 == 0:
        #When condition is true
        return False
    else:
        #When condition is false
        return True

#Main Function
if __name__ == '__main__':
    #Getting a number from the user
    number=int(input("Enter a number to check weather it is prime or not: "))
    if prime_number(number):
        print("The given number => ", number, " is a prime number")
    else:
        print("The given number => ", number, " is not a prime number")
