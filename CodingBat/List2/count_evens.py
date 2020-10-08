"""
Return the number of even ints in the given array.
Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
"""



def count_evens(nums):
    tracker = 0
    count = 0
    while tracker <= len(nums):
        if nums % 2 == 0:
            count += 1
            tracker += 1
        else:
            tracker += 1
    print(count)



nums = [2, 4, 5]
count_evens(nums)
