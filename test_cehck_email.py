import re


def check_mobile_num(number):
    if re.match("^d{10}", number):
        if re.match("^ \s (.\d)[a-zA-Z] (! @ # $ - % ^ & * ) ", number):
            return False
        return True



if __name__ == "__main__":
    phone_number = str(input("Enter ur num > "))
    print(check_mobile_num(phone_number))
