# This program get arguments and passed to the program

# Function to display arguments
import sys
def args_function(argument_zero,argument_one,argument_two):
    print(argument_zero)
    print(argument_one)
    print(argument_two)
    pass


if __name__ == "__main__":
    argument_zero = sys.argv[0]
    argument_one = sys.argv[1]
    argument_two = sys.argv[2]

    print(args_function(argument_zero,argument_one,argument_two))
    if argument_one == "pradeep":
         print("sucess")
