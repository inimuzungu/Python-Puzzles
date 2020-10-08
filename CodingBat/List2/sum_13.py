"""

Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky,
so it does not count and numbers that come immediately after a 13 also do not count.

sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6

nums.index(13) >= 0:
"""


def sum13(nums):
    count = 0
    while count <= len(nums):
        if nums[-1] == 13:
            del nums[-1]
            count += 1

        elif 13 in nums:
            pos_13 = nums.index(13)
            del nums[pos_13 + 1]
            del nums[pos_13]
            count += 1
        else:
            break
    print(nums)
    print(sum(nums))



nums = [13, 13]
sum13(nums)


"""
def sum13(nums):
    if 13 in nums:
        pos_13 = nums.index(13)
        a = sum(nums[0:pos_13])
        return a

    else:
        a = sum(nums)
        return a
        
"""

"""
def sum13(nums):
    #loop for length of list
    #del 13 and next item
    count = 0
    while count <= len(nums):
        if 13 in nums:
            pos_13 = nums.index(13)
            print(nums)
            del nums[pos_13 + 1]
            del nums[pos_13]
            print(nums)
            count += 1
        else:
            break

    print(sum(nums))
    print("End")





"""