'''
Roman numerals are represented by seven different symbols: 
    - I = 1
    - V = 5
    - X = 10
    - L = 50
    - C = 100
    - D = 500
    - M = 1000
'''
# IV = 4, IX = 9
# XL = 40, XC = 90
# CD = 400, CM = 900

from collections import deque


def roman_to_int(s):
    # edge case, look backward from first numeral and index becomes -1
    # add dummy start index
    s_deque = deque(s)
    s_deque.appendleft('dummy')
    # init total to keep running tally of dec value
    total = 0
    # loop i,numeral in enumerate(s):
    for i, numeral in enumerate(s_deque):
        if numeral == 'I':
            # add 1 to total
            total += 1
        elif numeral == 'V':
            # if i-1 == I
            if s_deque[i-1] == 'I':
                total += 3
            # else add 5
            else:
                total += 5
        elif numeral == 'X':
            # if i-1 = I
            if s_deque[i-1] == 'I':
                # add 8
                total += 8
            else:
                total += 10
        elif numeral == 'L':
            # if i-1 == X
            if s_deque[i-1] == 'X':
                # add 30
                total += 30
            else:
                total += 50
        elif numeral == 'C':
            # if i-1 == X
            if s_deque[i-1] == 'X':
                # add 80
                total += 80
            # else add 100
            else:
                total += 100
        elif numeral == 'D':
            # if i-1 == C
            if s_deque[i-1] == "C":
                # add 300
                total += 300
            # else add 500
            else:
                total += 500
        # elif its M
        elif numeral == 'M':
            # if i-1 == D
            if s_deque[i-1] == 'C':
                # add 800
                total += 800
            # else add 1000
            else:
                total += 1000
        # else its the dummy start element, continue

    # return total decimal number
    return total


print(roman_to_int("III")) #3
print(roman_to_int("LVIII")) #58
print(roman_to_int("MCMXCIV")) # 1994