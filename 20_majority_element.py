# Given an array, nums, size n
# return the majority element
    # majority element appears more than n / 2 times
    # assume a majority element always exists

def majority_element(nums):
    majority_number = len(nums) / 2
    occurences = {}

    for num in nums:
        occurences[num] = 1 + occurences.get(num, 0)
        if occurences[num] > majority_number:
            return num

print(majority_element([3,2,3])) #3
print(majority_element([2,2,1,1,1,2,2])) #2
