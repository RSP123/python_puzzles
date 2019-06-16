# This program print GCD of two numbers

# Function for GCD
def gcd(a, b):
    if a > b:
        s = b
    else:
        s = a
    for i in range(1, s+1):
        if ((a % i==0) and (b % i==0)):
            res = i
    return res

# Main
if __name__ == "__main__":
    a = int(input("Enter a no :"))
    b = int(input("Enter a no :"))

    print("GCD = ",gcd(a, b))
