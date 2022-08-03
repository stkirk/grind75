# Given two binary strings, a & b
# return their sum as a binary string
# only number 0 can contain a leading zero
def add_binary(a,b):
    return bin(int(a, 2) + int(b, 2))[2:]

print(add_binary("11", "1")) # "100"
print(add_binary("1010", "1011")) # "10101"
