# This program prints panlindrom of given string

# Function for panlindrom
def palindrom(p):

    # Check for panlindrom
    while (p != 0):
        original = p
        reversed = p[::-1]
        if original == reversed:
            return True
        return False

# Main Function
if __name__=="__main__":
    p = input("Enter the palindrom to check : ")
    check = palindrom(p)
    if check:
        print("String is palindrom")
    else:
        print("String is not palindrom")
