import sys


def problem():
    """
        Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
        before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
        to be after the elements less than x (see below). The partition element x can appear anywhere in the
        "right partition"; it does not need to appear between the left and right partitions.
        EXAMPLE
            Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
            Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8 
    """
    pass


class LinkedList:

    def __init__(self):
        
        self.head = None
        self.tail = None
        self.count = 0


    def add(self, item):
        if item is None:
            raise Exception("You cannot add a None object inside the list")

        self.count += 1
        
        if self.head is None and self.tail is None:
            self.head = self.Node(item)
            self.tail = self.head
            return

        new_node = self.Node(item)
        new_node.prev_node = self.tail
        self.tail.next_node = new_node
        self.tail = new_node


    # This solution assumes integers as a data type
    # This algorithm runs in O(n + n/2) where n is the count of the elements
    # It requires no additional memory (caching)
    # I have no idea why people do a recursive algorithm when this one is pretty much easy to implement
    def is_palindrome(self):

        sm = 0 
        tail = self.head
        half = self.count // 2
        
        while tail.next_node is not None:
            tail = tail.next_node

        head = self.head
        for i in range(half):

            if head.item != tail.item:
                return False

            head = head.next_node
            tail = tail.prev_node 

        if self.count % 2 == 0:
            return True
        
        return head.next_node.item == tail.next_node.item 

    def prnt(self): 
    
        items = []
        current = self.head

        while current is not None:
            items.append(current.item)
            current = current.next_node

        print(items)            


    class Node:
    
        def __init__(self, item, next_node = None, prev_node = None):
            self.item = item
            self.next_node = next_node
            self.prev_node = prev_node


if __name__ == '__main__':
    
    args = sys.argv[1:]
    linked_list = LinkedList()

    linked_list.add(1)
    linked_list.add(2) 
    linked_list.add(3)
    linked_list.add(2)
    linked_list.add(1)
    print(linked_list.is_palindrome())
