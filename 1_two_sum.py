# Given array of ints - nums, and int - target:
# Return indicies of the two numbers that add up to target
# each input has exactly 1 solution
# answers can be returned in any order
# can't use same element twice

def two_sum(nums, target):
    # init a dictionary such that key is target-num and value is the index
    complements = {(target-num):i for i, num in enumerate(nums)}
    # loop through nums
    for i,num in enumerate(nums):
        # if num in complements dictionary
        if num in complements:
            # no duplicates
            if i != complements[num]:
                # return [i, complements[num]]
                return [i, complements[num]]
    return complements

print(two_sum([2,7,11,15], 9)) #[0,1]
print(two_sum([3,2,4], 6)) #[1,2]
print(two_sum([3,3], 6)) #[0,1]
