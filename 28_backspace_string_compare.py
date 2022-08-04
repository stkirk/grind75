'''
Given 2 strings, s and t:
    - if they are both equal when typed into an empty text editor
        # return True
    - '#' is a backspace character
'''
# edge case: typing backspace when editor stack is empty

def backspace_string_compare(s,t):
    # init stacks for both strings to represent text field of the editor
    s_text = []
    t_text = []
    # loop through chars in s:
    for char in s:
        # if char == "#":
        if char == "#":
            if s_text:
                s_text.pop()
            else:
                continue
        else:
            # append char
            s_text.append(char)
    # loop through chars in t:
    for char in t:
        # if char == "#":
        if char == "#":
            if t_text:
                t_text.pop()
            else:
                continue
        else:
            # append char
            t_text.append(char)
    
    return s_text == t_text

print(backspace_string_compare("ab#c", "ad#c")) # True
print(backspace_string_compare("ab##", "c#d#")) # True
print(backspace_string_compare("a#c", "b")) # False
print(backspace_string_compare("#a#####b", "bb#")) # True
