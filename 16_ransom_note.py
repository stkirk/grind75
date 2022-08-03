# given two strings, ransomeNote and magazine
# if the ransomNote can be constructed using the letters from magazine
    # return True
    # if it can't, return False
# Constraint, each letter in the magazine can only be used once in ransomNote
# ransomNote and magazine are only lowercase english letters

def can_construct_note(ransomNote, magazine):
    # create a dictionary with all the letters from magazine and their letter count
    available_letters = {}
    for letter in magazine:
        available_letters[letter] = 1 + available_letters.get(letter, 0)
    # loop through ransomNote
    for letter in ransomNote:
        # is letter is not in magazine return false
        if letter not in available_letters:
            return False
        else:
            # decrement the count of available_letters[letter]
            available_letters[letter] -= 1
            if available_letters[letter] < 0:
                return False

    # out of loop all letters are available and in the right quantity
    return True

print(can_construct_note('a', 'b')) # False
print(can_construct_note('aa', 'ab')) # False
print(can_construct_note('aa', 'aab')) # True