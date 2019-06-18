# This program prints dinomination

# Function for dinomination
def denomi(amt):
    d = list(map(int,[2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]))
    for i in range(len(d)):
        if amt >= d[i]:
            change = d[i]
            print("amt -loop",change)
        else:
            d[i] = i + 1
            print("else loop",d[i])
    return change

if __name__ =="__main__":
    amt = 553
    print("result",denomi(amt))
