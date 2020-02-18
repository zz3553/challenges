class Node:
    def __init__(self, data, next):
        self.data = data #int 
        self.next = next #Node

#returns 1 if successful, 0 if not
def deletionByData(lst, val):

    if lst.data == val:
        temp = lst.data
        lst = lst.next
        return 1

    temp = lst #traverse this 
    while ( temp.next is not None ):
        if temp.next.data == val:
            temp.next = temp.next.next
            return 1
        else:
            temp = temp.next

    return 0

#return 0 -> not deleted, 1 -> deleted
def deletionAtIndex(lst, index):

    if index == 0:
        lst = lst.next
        return 1

    count = 0
    temp = lst

    while ( count != index ):
        count += 1
        if ( count == index ):
            temp.next = temp.next.next
            return 1
        else:
            temp = temp.next
    return 0


#
def addAt(lst, index, val):
    count = 0 
    temp = lst
    while ( temp is not None ):
        count += 1
        if count == index:
            new = Node(val, temp.next)
            temp.next = new
            return 1
        else:
            temp = temp.next

    return 0

def add(lst, val):
    temp = lst
    while ( temp is not None ):
        temp = temp.next
        if temp.next is None:
            temp.next = Node(val, None)
            return 1
    
    return 0

def main():
    lst = Node(7, None)
    lst2 = Node(6, lst)
    # print(deletionAtIndex(lst2, 1))

    print(addAt(lst2, 1, 1))

    print(add(lst2, 3))


main()