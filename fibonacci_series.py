# This program prints  Fibonacci series

# Function for  Fibonacci series

def  fibonacci(fib):
    first_temp = 1
    second_temp = 0
    num = 0;
    for i in range(0, fib):
        first_temp = first_temp + second_temp
        second_temp = first_temp - second_temp
    return second_temp


if __name__ == "__main__":
    fib=int(input("Enter a number to print  Fibonacci Series > :"))
    print(" Fibonacci Series are >>> ",fibonacci(fib))
