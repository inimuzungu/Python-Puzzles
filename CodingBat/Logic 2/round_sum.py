"""
For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more,
so 15 rounds up to 20.

Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5,
so 12 rounds down to 10.

Given 3 ints, a b c, return the sum of their rounded values.
To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times.
 Write the helper entirely below and at the same indent level as round_sum().

round_sum(16, 17, 18) → 60
round_sum(12, 13, 14) → 30
round_sum(6, 4, 4) → 10
"""


def round_sum(a, b, c):
    a_1 = round10(a)
    b_1 = round10(b)
    c_1 = round10(c)


    revised_sum = a_1 + b_1 + c_1

    print(revised_sum)
    return revised_sum


def round10(num):
    round_check = num % 10

    if round_check >= 5:
        roundedup_num = 10 - round_check
        revised_value = num + roundedup_num
        return revised_value
        print(revised_value)

    else:
        roundeddown_num = num - round_check
        revised_value = num - roundeddown_num
        return roundeddown_num
        print(roundeddown_num)



a = 12
b = 13
c = 14

round_sum(a, b, c)
