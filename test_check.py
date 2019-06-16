# # from time_greetings_4 import currentTime
#
# for i in range(2,9):
#     print(i)
# # print(currentTime("Jayanth Nagaraj"))



def check(s):
    s_count = 0

    with open(s ,'r') as new_file:

        s_count = new_file.readlines()

    return s_count

s = "open.txt"
print(check(s))
f = check(s)
print(len(f))
