# This program prints dinomination

d = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
# Function for dinomination
def denomination(amt):
    change = []

    for i in range(0,len(d)):
        # Loop for comparing with amount
        if amt >= d[i] and amt > 0:
            rupee = amt%d[i]
            rupee_count = int(amt/d[i])
            change.append((d[i], rupee_count))
            amt = rupee
    return change


# Main
if __name__ =="__main__":
    amt = 10900
    print(amt, " change => ",denomination(amt))
