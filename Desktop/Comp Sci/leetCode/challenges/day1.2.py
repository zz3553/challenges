# Given two strings, write a method to decide if one is a permutation of the other.


def solve(str1, str2):
    # str1 = sorted(str1)   easy solution by sorting both strings 
    # str2 = sorted(str2)
    # if str1 == str2: 
    #     return True
    # return False

    map = {}

    if len(str1) != len(str2): #base case
        return False

    for i in str1:
        if i not in map:
            map[i] = 1
        else:
            map[i] += 1
    
    for i in str2:
        if i in map and map[i] > 0:
            map[i] -= 1
        elif i in map and map[i] < 1:
            return False
        elif i not in map:
            return False
    
    return True

print(solve("hero", "rehr"))