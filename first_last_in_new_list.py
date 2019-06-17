# This program prints first and last element in new list from given largest_list

# Function for new list
def new_list(old):
    new = []
    new.append(old[0])
    new.append(old[-1])
    return new


if __name__ == "__main__":

    # old = [23, 34, 45, 56, 67, 78]
    old = input("Enter the elements;").split()

    print(type(old))
    # print(type(new_list(new)))
    f = new_list(old)
    print(new_list(old))
    print(type(f))
