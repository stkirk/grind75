# given n versions, [v1, v2, v3,...,vn] and an API called isBadVersion(version) that takes the int version and returns a bool value if the version is bad or not
# return the first bad version
# Constraint: must be solved in O(log n) time

def first_bad_v(n):
    # init left and right bounds, 0 and len(versions) -1
    left = 1
    right = n
    # keep track of lowest version that is bad starting at n
    lowest = n
    # while loop, left <= right
    while left <= right:
        print('left-->', left, ' right-->', right)
        # guess the middle index, (right-left)//2
        guess = (right + left) // 2
        # badVersion = pass versions[guess] into isBadVersion
        bad = isBadVersion(guess)
        if bad:
            # compare to lowest, if lower, lowest = [guess]
            if guess < lowest:
                lowest = guess
            # move the right bounds to guess - 1
            right = guess - 1
        # else its a good version, the bad  start at higher index
        else:
            # move the left bound to guess + 1
            left = guess + 1

    # while loop finished, lowest bad version should be found
    return lowest
# no test cases, isBadVersion is a black box leetcode has
print(first_bad_v(5))
print(first_bad_v(6))
