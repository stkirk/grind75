# Given an array of ints, nums, and target:
# if target exists in nums return its index, otherwise -1
# nums is sorted in ascending order and unique

# solution must have O(log n) time complexity

def binary_search(nums, target):
    # init pointers for left, right bounds
    right = len(nums) - 1
    left = 0

    while left <= right:
        guess = (right + left) // 2

        if nums[guess] == target:
            return guess

        elif nums[guess] > target:
            # move right bound to guess_idx - 1
            right = guess - 1
        # else - guess < target, move left boundary to guess_idx + 1
        else:
            left = guess + 1

    # loop finished without finding target
    return -1

print(binary_search([-1,0,3,5,9,12], 9)) # 4
print(binary_search([-1,0,3,5,9,12], 2)) # -1
