class Node:
    def __init__(self, data, next):
        self.data = data #int 
        self.next = next #Node


#deletes middle node
def solution(node):

    node = node.next #set current to next
    return node

def main():
    lst = Node(3, None)
    lst2 = Node(2, lst)
    lst3 = Node(1, lst2)
    lst4 = Node(2, lst3)
    lst2 = solution(lst2)
    print(lst2.data)

main()