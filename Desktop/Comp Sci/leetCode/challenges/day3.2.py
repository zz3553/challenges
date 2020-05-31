# One Away: There are three types of edits that can be performed on strings: 
# insert a character, remove a character, or replace a character. 
# Given two strings, write a function to check if they are one edit (or zero edits) away.

# EXAMPLE
# pale, pie -> false        
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false
# pale, pales -> true

import string

def solve(str, str2):
    if str == str2: return True #if theyre the same 

    str = str.lower()
    str2 = str2.lower()
    str = list(str)
    for  i in range(len(str)+1):  # inserting character 
        str2 = list(str2)
        for x in range(len(str2)):
            str.insert(i, str2[x])
            if "".join(str) == "".join(str2):
                return True
            str.pop(i)

    for i in range(len(str)):  # removing character 
        popped = str.pop(i)
        if "".join(str) == str2:
            return True
        str.insert(i, popped)

    for i in range(len(str)): #swapping 
        popped = str.pop(i)
        str2 = list(str2)
        for x in range(len(str2)):
            str.insert(i, str2[x])
            if "".join(str) == "".join(str2):
                return True
            str.pop(i)
        str.insert(i, popped)
    



            

print(solve('sfdsf', 'afdsf'))
