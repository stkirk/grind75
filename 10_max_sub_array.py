# given an array of ints, nums:
# find the contiguos subarray (containing at least 1 number) which has the largest sum
# return the sum

def max_sub_array(nums):
    # max_sum is the max of the cur_sum and the cur_num
    max_sum = nums[0]
    # cur_sum stores the total sum of the current contiguous sub array
    cur_sum = 0

    for num in nums:
        # compare current num to cur_sum and take the max of the two and set that to cur_sum
        # so cur_sum could either be an existing subarray plus num or reset to num
        cur_sum = max(cur_sum + num, num)

        # compare cur_sum to max_sum and set max_sum to the bigger value
        max_sum = max(max_sum, cur_sum)

    return max_sum
print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4])) # 6 --> [4,-1, 2, 1]
print(max_sub_array([1])) # 1
print(max_sub_array([5,4,-1,7,8])) # 23
