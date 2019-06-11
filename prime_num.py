#This program check weather the given number is prime or not
#Function to check prime number
def prime_number(number):
    if number%2 == 0:
        #When condition is true
        return True
    else:
        #When condition is false
        return False

#Main Function
if __name__ == '__main__':
    #Getting a number from the user
    number=int(input("Enter a number to check weather it is prime or not: "))
    prime_number(number)
