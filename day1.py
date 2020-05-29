# Is Unique: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

def solve(str):
    data = []
    for i in str:
        if i in data:
            return False
        data.append(i)
    return True


print(solve("helo"))

