# This program prints dinomination

# Function for dinomination
def denomi(amt):
    d = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    for i in d:
        if amt >= d:
            change = d
            print(change)
        else:
            i += 1
    return change

if __name__ =="__main__":
    amt = 553
    print("",denomi(amt))
