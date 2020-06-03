# Part 1 - palindrome for a stirng

def solveSTRING(str):
    if len(str) == 0:
        return True
    
    if str[0] != str[len(str)-1]:
        return False
    
    else:
        return solve(str[1:len(str)-1])

#print(solveSTRING('hello world '))

# Palindrome: Implement a function to check if a linked list is a palindrome.

from dataclasses import dataclass

@dataclass
class Node:
  def __init__(self, data, next): 
    self.data = data
    self.next = next


def length(node) -> int: 
    count = 0
    while node is not None:
        count += 1
        node = node.next
    return count 

def solve(node):
    temp = node
    lst = []
    index = 0
    while temp is not None:
        lst.insert(0,temp.data)
        temp = temp.next

    while node is not None:
        if lst[index] != node.data:
            return False
        index += 1
        node = node.next
    return True

node1 = Node(6, None)
node2 = Node(1, node1)
node3 = Node(6, node2)

print(solve(node3))