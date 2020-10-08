"""
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
"""

def array123(nums):
    if len(nums) >= 3:
      for i in range(len(nums)):
            if nums[i] == 1 or nums[i] == 2 or nums[i] == 3:
                print(True)
            else:
                print(False)
    else:
      print(False)

nums = [1, 2, 3]
array123(nums)


def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    else:
        return False