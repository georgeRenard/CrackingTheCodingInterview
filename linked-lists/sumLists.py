import sys


def problem():
    """
    Sum Lists: You have two numbers represented by a linked list, where each node contains a single
    digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
    function that adds the two numbers and returns the sum as a linked list.
    EXAMPLE
        Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
        Output: 2 -> 1 -> 9. That is, 912.
        FOLLOW UP

        Suppose the digits are stored in forward order. Repeat the above problem.
        EXAMPLE
            Input:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
            Output: 9 -> 1 -> 2. That is, 912. 

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


    def add_first(self, item):
        
        if item is None:
            raise Exception("You cannot add a None object inside the list")
        
        self.count += 1
        new_node = self.Node(item)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = self.head
            return

        new_node = self.Node(item)
        self.head.prev_node = new_node
        new_node.next_node = self.head
        self.head = new_node


    def sum_lists_reversed(self, other):
        
        # If tail pointer is allowed - it is the same as the algo below   
        # Otherwise we have to obtain it 
        result = LinkedList()
 
        tail = self.head
        while tail.next_node is not None:
            tail = tail.next_node
            
        other_tail = other.head
        while other_tail.next_node is not None:
            other_tail = other_tail.next_node


        left = tail
        right = other_tail
        rem = 0

        while left is not None and right is not None: 
            
            sm = left.item + right.item + rem 
            
            digit = (sm % 10)
            rem = sm // 10

            result.add_first(digit)
            left = left.prev_node
            right = right.prev_node             
        

        if left is not None:
            while left is not None:
                left = left.prev_node
                result.add(left.item)

        if right is not None:
            while right is not None:
                right = right.prev_node
                result.add(right.item)


        return result


    # Here we assume that the list is of integers (unlike in previous problems where duck typing is used)
    # The reason is that the problem is inherent to integer addition 
    def sum_lists(self, other):

        result = LinkedList()

        left = self.head
        right = other.head
 
        rem = 0
        while left is not None and right is not None:

            sm = left.item + right.item + rem

            digit = (sm % 10)
            rem = sm // 10 

            result.add(digit)
            left = left.next_node
            right = right.next_node

                         
        if left is not None:
            while left is not None:
                left = left.next_node 
                result.add(left.item)


        if right is not None:
            while right is not None:
                right = right.next_node
                result.add(right.item)


        return result


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
    other_linked_list = LinkedList()
    linked_list.add(6)
    linked_list.add(1)
    linked_list.add(7)

    other_linked_list.add(2)
    other_linked_list.add(9)
    other_linked_list.add(5)
   
    res = linked_list.sum_lists_reversed(other_linked_list)
    res.prnt()
