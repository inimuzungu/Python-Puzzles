py """
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
"""

def has22(nums):
    #iterate through list to find 2
    if len(nums) < 2:
        return False
    else:
        nums.index("2")
        for i in range(len(nums)):
            if nums[i] == 2:
                if nums[i-1] == 2 or nums[i+1] == 2:
                    return True
                else:
                    return False
            else:
                return False


nums = [1, 2, 2]
has22(nums)