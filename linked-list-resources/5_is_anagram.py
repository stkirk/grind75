# Given string s and t:
# if t is an anagram of s, return True
# else return False
# Constraint: s and t only consist of lowercase english letters
# must use the original letters only once

from collections import deque


def is_anagram(s,t):
    # edge case: check to see if string lengths are the same
    if len(s) != len(t):
        return False
    # split both strings into sorted lists
    t_list = list(t)
    t_list.sort()
    # convert s_list to a queue
    s_list = list(s)
    s_list.sort()
    sq = deque(s_list)

    # loop through indexes in t:
    for i, letter in enumerate(t_list):
        if s_list[i] == t_list[i]:
            sq.popleft()
        # else letters don't match
        else:
            return False

    # loop finished, if sq is empty return True, else return false
    if len(sq) == 0:
        return True
    else:
        return False

# using dictionary
def is_anagram2(s,t):
    # edge case: check to see if string lengths are the same
    if len(s) != len(t):
        return False
    for letter in s:
        if s.count(letter) != t.count(letter):
            return False
    return True

def is_anagram3(s,t):
    # using hashmaps
    if len(s) != len(t):
        return False
    s_count, t_count = {}, {}

    for i in range(len(s)):
        # instead of if/else statement .get adds a key with a default value to the dict if not there so it doesn't throw a key error
        s_count[s[i]] = 1 + s_count.get(s[i], 0)
        t_count[t[i]] = 1 + t_count.get(t[i], 0)

    for letter in s:
        if s_count[letter] != t_count.get(letter, 0): # avoids key error if letter not in t dict
            return False
    return True

# print(is_anagram("anagram","nagaram")) # True
# print(is_anagram("rat","car")) # False

# print(is_anagram2("anagram","nagaram")) # True
# print(is_anagram2("rat","car")) # False

print(is_anagram3("anagram","nagaram")) # True
print(is_anagram3("rat","car")) # False
