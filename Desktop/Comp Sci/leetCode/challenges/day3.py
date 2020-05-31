# Palindrome Permutation: Given a string, write a function to check if it 
# is a permutation of a palin- drome. 
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters. 
# The palindrome does not need to be limited to just dictionary words.
 
# EXAMPLE

# Input : Tact Coa
# Output: True -> ("taco cat", "atco eta", ... )

def solve(str):
    """
    if len is even -> palindrome will have each letter appear twice, odd -> one letter appears once
    order doesnt matter since they could re arranged 
    """
    map = {} #keeps track of coutns of letter 
    for i in str:
        if i not in map:
            map[i] = 1
        else:
            map[i] += 1

    ones = 0
    for i in map:
        if map[i] > 2:
            return False
        if map[i] == 1 and i != ' ':
            ones += 1

    if ones > 1:
        return False
    return True


tests = ['tact coa', 'abba', 'abbc']
for i in tests:
    print(solve(i))
