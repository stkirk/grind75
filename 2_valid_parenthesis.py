# Given a string containing only '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
    # open/close must be same bracket type
    # open brackets must be closed in the correct order

# first in last out stack
from collections import deque


def valid_brackets(s):
    # init a dictionary that maps close brackets to open brackets
    map_brackets = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    # init stack using deque to add open brackets to
    stack = deque()

    # loop through brackets in s
    for bracket in s:
        # if its an open bracket, add it to the stack
        if bracket == '(' or bracket == '{' or bracket == '[':
            stack.append(bracket)
        # else its a close bracket
        else:
            # if stack has length and close bracket maps to last index of stacks open
            # dic[bracket] == stack[-1]
            if len(stack) > 0 and map_brackets[bracket] == stack[-1]:
                # pop the last index of stack
                stack.pop()
            # else the close bracket doesn't map to the open one
            else:
                return False
    
    # if stack is empty
    if not stack:
        return True

print(valid_brackets("()")) # True 
print(valid_brackets("()[]{}")) # True
print(valid_brackets("(]")) # False
print(valid_brackets(")(){])")) # False
print(valid_brackets("((){])(")) # False
print(valid_brackets("([{]})")) # False
