#Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
class Node:
    def __init__(self, data, next):
        self.data = data #int 
        self.next = next #Node

def solution(lst, k):
    len = 0 
    temp = lst
    while temp is not None: #finds length of list 
        len += 1
        temp = temp.next
    
    i = 0
    count = len - k 
    while i != len: #goes through length of list
        if i == count: #if i is up to kth element
            return lst.data
        else:
            lst = lst.next
        i += 1

    return 0    

def main():
    lst = Node(3, None)
    lst2 = Node(2, lst)
    lst3 = Node(1, lst2)
    lst4 = Node(2, lst3)
    print(solution(lst4, 4))

main()