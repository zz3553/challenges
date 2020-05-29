# Is Unique: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

def solve(str):
    # data = []  1rst solution with data structure
    # for i in str:
    #     if i in data:
    #         return False
    #     data.append(i)
    # return True

    for i in range(len(str)):
        for x in range(i+1, len(str)):
            if str[i] == str[x]:
                return False

    return True

print(solve("dsfsdd"))

