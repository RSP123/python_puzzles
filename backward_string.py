# Program prints backwards of string

# Function for converting backward of string
def backward(str):
    reverse = []
    backward = []

    # Spliting string into words and reverse words
    str = str.split()
    reverse = str.reverse()
    backward = " ".join(str)

    return backward


# Main
if __name__=="__main__":
    str = "hii hello im pradeep from chennai"
    print("backward of string :",backward(str))
