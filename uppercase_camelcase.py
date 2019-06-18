# This program convert lowercase to uppercase and camelcase
# Function for uppercase
def upper_case(str):
    upper = ''
    # Checks if char is lowercase then changes to uppercase
    for char in str:
        if ord(char) >= 65:
            upper += chr(ord(char) - 32)
            uppercase = upper.split()
    return upper_case

# Function for CamelCase
def camel_case(lower):
    camel = ''
    text = ''
    # Chaning to CamelCase
    for char in lower:
        camel = text[:1].upper()


    return camel.upper()

if __name__ == "__main__":
    lower = str(input("Enter a string here: >"))
    print("To Uppercase :",upper_case(lower))
    print("To CamelCase :",camel_case(lower))
