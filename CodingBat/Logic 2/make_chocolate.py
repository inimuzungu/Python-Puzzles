"""
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2

"""

def make_chocolate(small, big, goal):
    big_weight = big * 5
    num_bb = goal / 5
    bb_weight_req = num_bb * 5
    weight_diff = goal - bb_weight_req

    if bb_weight_req <= big_weight:
        if weight_diff <= small:
            return weight_diff
        else:
            return -1

    elif bb_weight_req > big_weight:
        small_need = goal - big_weight
        if small_need <= small:
            return small_need
        else:
            return -1

    else:
        return -1