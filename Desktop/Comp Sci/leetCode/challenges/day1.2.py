# Given two strings, write a method to decide if one is a permutation of the other.


def solve(str1, str2):
    str1 = sorted(str1)
    str2 = sorted(str2)
    if str1 == str2: 
        return True
    return False

print(solve("rac", "car"))