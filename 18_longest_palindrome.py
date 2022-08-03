# Given string, s, which has both lowercase and uppercase letters
# return the LENGTH of the longest palindrome that can be built with those letters
# Constraint: letters are case sensitive, 'aA' is not a palindrome here

def longest_palindrome(s):
    longest = 0
    occurences = {}

    # loop through s, keeping track of frequency letters occur
    for letter in s:
        # this line adds each letter to the dict if it isn't there with a default value of 0, then increments by 1 or if it is there increments by 1
        occurences[letter] = 1 + occurences.get(letter, 0)
        # if letter gets to 2 occurences, add 2 to longest then reset key to 0 occurences
        if occurences[letter] == 2:
            longest += 2
            occurences[letter] = 0

    # check if any keys in the dict have a value of 1
    if 1 in occurences.values():
        # there is a 1, increment longest
        longest += 1
    return longest
    
print(longest_palindrome("abccccdd")) # 7
print(longest_palindrome("a")) # 1
