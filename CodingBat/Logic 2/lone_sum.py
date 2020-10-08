"""
Given 3 int values, a b c, return their sum.
However, if one of the values is the same as another of the values,
it does not count towards the sum.

lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
"""

def lone_sum(a, b, c):
    #checks if there is a duplicate value
    if a == b and b == c and c == a:
        return 0

    elif a == b or b == c or c == a:
        if a == b:
            return c
        elif b == c:
            return a
        else:
            return b
    #sums all values if there are no duplicate values
    else:
        sum_total = a + b + c
        return sum_total



a = 3
b = 3
c = 3

lone_sum(a,b,c)
