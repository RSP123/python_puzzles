# This program prints LCM

# Function for LCM
def lcm(a, b):
    if a > b:
        s = a
    else:
        s = b

    while True:
        if s%a == 0 and s%b == 0:
            lcm = s
            break
        s = s+1

    return lcm

if __name__ == "__main__":

    a = 6
    b = 4
    print("LCM of a =>", a, "b => ", b, "is =>", lcm(a, b))

    a = 63
    b = 43
    print("LCM of a =>", a, "b => ", b, "is =>", lcm(a, b))

    a = 23
    b = 46
    print("LCM of a =>", a, "b => ", b, "is =>", lcm(a, b))

    a = 56
    b = 35
    print("LCM of a =>", a, "b => ", b, "is =>", lcm(a, b))
