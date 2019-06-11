def greeting(name = "Your_Full_Name"):
    return "Hi " + name.split(" ")[0] + "!"

name = input("Type your Firstname and lastname > ")

print(greeting(name))

#
# new_str = "Hi jayanth this is sample "
# print(new_str, "  =>  ", type(new_str))
#
# new_str = new_str.split(" ")
# print(new_str, "  =>  ", type(new_str))
# print(new_str[2])
