# Program print birthday date using dictionary

# Function for birthday date using dictionary
def birthday(name):
    details = {
    "pradeep" : "28-05-1994",
    "jayanth" : "20-1-1996",
    "krishoth": "16-3-1996",
    "hema"    : "31-6-1995",
    }


    return details[name]


if __name__ == "__main__":
    name = input("enter name :")
    print("DOB =",birthday(name))
