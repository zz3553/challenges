class Node:
    def __init__(self, data, next):
        self.data = data #int 
        self.next = next #Node

def solution(partition, lst):
    new_list_same = Node
    new_list_less = Node
    new_list_more = Node

    temp = lst
    while temp is not None:
        if temp.data > partition:
            node = createNode(partition)
            addNode(new_list_more, node)
        if temp.data < partition:
            node = createNode(partition)
            addNode(new_list_less, node)
        if temp.data == partition:
            node = createNode(partition)
            addNode(new_list_same, node)
        temp = temp.next



def addNode(lst, node):
    lst.next = node

def createNode(data):
    return Node(data, None)


def main():
    partition = 5
    node1 = Node(1, None)
    node2 = Node(2, node1)
    node3 = Node(10, node2)
    node4 = Node(5, node3)
    node5 = Node(8, node4)
    node6 = Node(5, node5) 
    node7 = Node(3, node6) # 3->5->8->5->10->2->1->None
    solution(partition, node7)

main()