"""
Given 3 int values, a b c, return their sum.
However, if one of the values is 13 then it does not count towards the sum and values to its right do not count.
So for example, if b is 13, then both b and c do not count.

lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1
"""
def lucky_sum(a, b, c):
    if a == 13 and c == 13 or a == 13 and b == 13:
        sum = 0
        return sum

    elif a == 13 or b == 13 or c == 13:
        if a == 13:
            sum = 0
            return sum

        elif b == 13:
            sum = a
            return sum

        else:
            sum = a + b
            return sum

    else:
        sum = a + b + c
        return sum


a = 1
b = 2
c = 3

lucky_sum(a,b,c)

