# Given a string - s
# Return true if its a palindrome, false if not
# its a palindrome if after making it lowercase and removing all alphanumeric chars it reads the same backwards and forwards

def is_palindrome(s):
    # remove all non letter chars
    # convert to all lowercase
    alpha_str = ''.join([char.lower() for char in s if char.isalnum()])
    # save reversed version of converted string as a variable
    rev_alpha = alpha_str[::-1]
    # if reversed string and converted string are equal, return True
    if alpha_str == rev_alpha:
        return True
    # else return false
    else:
        return False

print(is_palindrome("A man, a plan, a canal: Panama")) # True
print(is_palindrome("race a car")) # False
print(is_palindrome(" ")) # True