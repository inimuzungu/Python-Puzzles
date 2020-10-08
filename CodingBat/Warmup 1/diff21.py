'''
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
'''


def diff21(n):
    n = 10
    # subtract n from 21 and double the difference if n > 21
    if n > 21:
        print((21 - n) * -2)
    # if n < 21 then return the result of (21 - n)
    else:
        print(n)
