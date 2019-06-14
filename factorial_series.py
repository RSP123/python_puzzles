# This program prints factorial series
# Function factorial series
def factorial(number):
    fact = 1
    # Factorial loop
    for i in range(1, number+1):
        fact = fact * i
    return fact


# Main Function

if __name__ == "__main__":
    number  = int(input("Enter a number to find factorial >"))
    print("Factorial series:",factorial(number))
