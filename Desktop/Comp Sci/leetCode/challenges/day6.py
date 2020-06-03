# Part 1 - palindrome for a stirng

def solveSTRING(str):
    if len(str) == 0:
        return True
    
    if str[0] != str[len(str)-1]:
        return False
    
    else:
        return solve(str[1:len(str)-1])

print(solveSTRING('hello world '))

# Palindrome: Implement a function to check if a linked list is a palindrome.

from dataclasses import dataclass

@dataclass
class Node:
  def __init__(self, data, next): 
    self.data = data
    self.next = next


def solve(node):
    return False
