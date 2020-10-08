"""
Given 3 int values, a b c, return their sum.
However, if any of the values is a teen -- in the range 13..19 inclusive --
then that value counts as 0, except 15 and 16 do not count as a teens.
Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule.
In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
Define the helper below and at the same indent level as the main no_teen_sum().

no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3

"""


def no_teen_sum(a, b, c):
    a_1 = fix_teen(a)
    b_1 = fix_teen(b)
    c_1 = fix_teen(c)

    revised_sum = a_1 + b_1 + c_1
    print(revised_sum)
    return revised_sum


def fix_teen(a):
    if a == 15 or a == 16:
        return a
    elif 13 <= a <= 19:
        return 0
    else:
        return a


a = 13
b = 13
c = 13

no_teen_sum(a, b, c)
