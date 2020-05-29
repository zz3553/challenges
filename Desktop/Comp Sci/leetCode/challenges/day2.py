# URLify: Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold 
# the additional characters, and that you are given the "true" length of 
# the string. (Note: If implementing in Java, please use a character array 
# so that you can perform this operation in place.)


# EXAMPLE
# Input: "Mr 3ohn Smith, 13 
# Output: "Mr%203ohn%20Smith"

STR = '%20' #replace space with this 

def solve(str, size):
    # str = str.split()   solution with splitting into list 
    # for i in range(len(str)):
    #     if i != len(str)-1 and str[i] != STR: #not end of list
    #         str.insert(i+1, STR)

    # return str

    res = ''
    for i in range(len(str)):
        if i < size-1 and str[i] == ' ' and str[i+1] != ' ':
            res += STR
        elif i < size and str[i] != ' ':
            res += str[i]
    return res

str = "    Mr John    Smith   "
length = len(str)
print(solve(str, length))


