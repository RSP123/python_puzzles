# Program for removing duplicate element in tthe list using set

# function to remove the duplicates
def duplicate(input):
    result = []

    res = set(input)   # Converting list to set
    for i in res:
        result.append(i)

    return result


# Main
if __name__=="__main__":
    input = [1, 2, 2, 3, 4, 8, 8, 7, 8, 9, 5]
    print(type(input))
    print("without duplicates",duplicate(input))
    print(type(duplicate(input)))
