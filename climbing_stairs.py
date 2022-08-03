# climb a staircase that takes n steps to reach the top
# each step you can either climb 1 or 2 steps
# how many ways can you climb to the top?

def climb_stairs(n):
    # Dynamic programming:
    # memoize how many ways to climb 0,1,2,3..n steps in a list
    # dp[0] = number of ways to climb 0 stairs, dp[1] = number of ways to climb 1 stair
    dp = [0 for i in range(n + 1)]
    # base cases: can climb 0 steps 1 way, can climb 1 step 1 way
    dp[0] = 1
    dp[1] = 1
    # from two steps and on, can only come from 1 step before, and two steps before
    # keeps a running total of ways to get to n steps as i increases
    for i in range(2, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp)
    return dp[n]


print(climb_stairs(2)) # 2
print(climb_stairs(3)) # 3
