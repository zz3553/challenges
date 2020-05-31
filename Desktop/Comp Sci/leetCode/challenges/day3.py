# Palindrome Permutation: Given a string, write a function to check if it 
# is a permutation of a palin- drome. 
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters. 
# The palindrome does not need to be limited to just dictionary words.
 
# EXAMPLE

# Input : Tact Coa
# Output: True -> ("taco cat", "atco eta", ... )

def solve(str):
    map = {}
    for i in str:
        if i not in map:
            map[i] = 1
        else:
            map[i] += 1

    for i in map:
        if map[i] > 2:
            return False

    return True

print(solve("tact coa"))
