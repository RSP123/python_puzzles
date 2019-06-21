# Program returns boolean value if the given number is in the list

# Function for sorting and finding element
def sort_find(input_list,n):
    res = []

    input_list.sort()
    if n in input_list:
        return True
    return False

if __name__=="__main__":
    input_list = [1, 2, 8, 4, 5, 6, 7, 3, 9]
    n = int(input("enter number to find"))
    check = sort_find(input_list,n)
    if check:
        print("Number found !")
    else:
        print("not found")
