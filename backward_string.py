# This program prints backwards of string

# Function for converting backward of string
def backward(str):
    result = []

    #converting to backward
    for j in range(len(str)):
        result = str[::-1]

    return result


# Main
if __name__=="__main__":
    str = "iannehc morf peedarp mi olleh iih"
    print("backward of string :",backward(str))
