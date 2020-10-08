"""
Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
"""

def max_end3(nums):
    a = nums[0]
    c = nums[-1]
    if a >= c:
        list_max_value = [a, a, a]
        return list_max_value
    else:
        list_max_value = [c, c, c]
        return list_max_value

nums = [3, 1]
max_end3(nums)