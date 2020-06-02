# Sum Lists: You have two numbers represented by a linked list, 
# where each node contains a single digit. The digits are stored in 
# reverse order, such that the 1's digit is at the head of the list. 
# Write a function that adds the two numbers and returns the sum as a linked list.

# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2). Thatis,617 + 295. Output: 2 -> 1 -> 9.That is, 912.

# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem. EXAMPLE
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295. Output: 9 -> 1 -> 2.That is, 912.

from dataclasses import dataclass

@dataclass
class Node:
  def __init__(self, data, next): 
    self.data = data
    self.next = next

def solve(list1, list2):
    sum = 0
    tens = 0
    while list1 is not None:
        sum += list1.data * (10**tens)
        tens+=1
        list1 = list1.next
    
    tens = 0
    while list2 is not None:
        sum += list2.data * (10**tens)
        tens+=1
        list2 = list2.next

    someNode = Node(sum%10, None)
    sum = sum // 10
    a = sum % 10
    while sum is not 0:
        someNode.next = Node(sum%10, None)
        someNode.next = someNode.next.next
        sum = sum // 10

    return someNode

def helper(node, val):
    if val//10 == 0 and val %10 != 0:
        node2 = Node(node.data, Node(val, None))
        return node2
    return



node1 = Node(6, None)
node2 = Node(1, node1)
node3 = Node(7, node2)
print(solve(node3, node3))