'''
Given an array of ints, nums
    # if any value appears >= 2 times --> return True
    # if every element is distinct --> return False
'''

def contains_duplicates(nums):
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)
        if count[num] > 1:
            return True
    return False

print(contains_duplicates([1,2,3,1])) # True
print(contains_duplicates([1,2,3,4])) # False
print(contains_duplicates([1,1,1,3,3,4,3,2,4,2])) # True
