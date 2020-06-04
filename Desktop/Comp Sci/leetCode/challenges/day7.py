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

def length(list):
    count = 0
    while list is not None:
        count += 1
        list = list.next
    return count

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
    temp1 = list1 if length(list1) > length(list2) else list2 #bigger list
    temp2 = list2 if length(list1) > length(list2) else list1
    count = length(temp1) - length(temp2)

    while count != 0:
        temp1 = temp1.next
        count -= 1 
    
    temp1 = temp1.next
    temp2 = temp2.next
    while temp1 is not None:
        if temp1.data != temp2.data:
            return False
        temp1 = temp1.next
        temp2 = temp2.next

    return True


# node1 = Node(6, None)
# node2 = Node(1, node1)
# node3 = Node(7, node2)

# node4 = Node(5, None)
# node5 = Node(7, node4)
# node6 = Node(1, node5)

node7 = Node(30, None)
node8 = Node(15, node7)
node9 = Node(9,node8)

node10 = Node(30, None)
node11 = Node(15, node10)
node12 = Node(10, node11)
node13 = Node(5, node12)


print(solve(node13, node9))