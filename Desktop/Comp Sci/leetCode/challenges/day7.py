# Intersection: Given two (singly) linked lists, determine if the two lists intersect. 
# Return the inter- secting node. Note that the intersection is defined based on reference, 
# not value. That is, if the kth node of the first linked list is 
# the exact same node (by reference) as the jth node of the second linked list, then they 
# are intersecting.

from dataclasses import dataclass

@dataclass
class Node:
  def __init__(self, data, next): 
    self.data = data
    self.next = next

def solve(list1, list2):
    # temp = list2     this way is if theres only one intersecting nodes, but rest of list isn't the same
    # while list1 is not None:
    #     while temp is not None:
    #         if (list1.data == temp.data) and (list1.next.data == temp.next.data):
    #             return True
    #         temp = temp.next
    #     temp = list2
    #     list1 = list1.next
    # return False


node1 = Node(6, None)
node2 = Node(1, node1)
node3 = Node(7, node2)

node4 = Node(5, None)
node5 = Node(7, node4)
node6 = Node(1, node5)


print(solve(node3, node6))