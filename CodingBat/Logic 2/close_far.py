"""
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1),
while the other is "far", differing from both other values by 2 or more.
Note: abs(num) computes the absolute value of a number.

close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True
"""

def close_far(a, b, c):
    diff_ab = abs(a - b)
    diff_ac = abs(a - c)
    diff_bc = abs(b - c)

    print(diff_ab)
    print(diff_ac)

    if diff_ab <= 1 and diff_ac >= 2 and diff_bc >= 2:
        print(True)
        return True
    elif diff_ab >= 2 and diff_ac <= 1 and diff_bc >= 2:
        print(True)
        return True
    else:
        print(False)
        return False

close_far(10, 8, 9)