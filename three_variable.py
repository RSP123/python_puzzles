# This program prints three variable
# Function for largest number
def largest(a, b, c):
    # Checking a is largest by comparing a with b and c
    if (a > b) and (a > c):
        return a
    # Checking b is largest by comparing b with a and c
    elif (b > a) and (b > c):
        return b
    # Else, the greates should be 'C'
    return c
