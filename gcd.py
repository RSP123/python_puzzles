# This program print GCD of two numbers

# Function for GCD
def gcd(a, b):
    if a > b:
        smallest = b
    else:
        smallest = a
    for i range(1,smallest +1 ):
        if (a % i) and (b % i):
            res = i 
    return res

# Main
if __name__ == "__main__":
    a = int(input("Enter a no :"))
    b = int(input("Enter a no :"))

    print("GCD = ",gcd(a, b))
