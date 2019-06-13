# # from time_greetings_4 import currentTime
#
# for i in range(2,9):
#     print(i)
# # print(currentTime("Jayanth Nagaraj"))




def text(num):
    if 0 > num > -250:
        num = range(num)
        print(num)
        text(num)

def chumma(n):
    while n < 0:
        chumma(7)
        print("chumma")

def edhu_chumma(num):
    m = 10
    a = range(num)
    print(m,*a)


def m_n(m, n):
    a = range(m, m*n+1, n)
    print(*a)

m_n(3, 6)
