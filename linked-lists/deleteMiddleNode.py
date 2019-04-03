import sys


def problem():
    """
        Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
        the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
        that node.
        EXAMPLE
            Input: The node c from the linked list a->b->c->d->e->f
            Result: Nothing is returned, but the new linked list looks like a->b->d->e->f 
    """
    pass



class LinkedList:
    
    def __init__(self):
    
        self.head = None
        self.tail = None
        self.count = 0


    def add(self, item):
        if item is None:
            raise Exception("You cann add a None object inside the list")

        self.count += 1

        if self.head is None and self.tail is None:
             self.head = self.Node(item)
             self.tail = self.head
             return


        new_node = self.Node(item)
        self.tail.next_node = new_node
        self.tail = new_node
 
    def remove_from_middle(self, node):
        
        if node == self.head or node == self.tail or self.count <= 2:
            raise Exception("You cannot remove the first or the last element from the list.") 

        p1 = self.head.next_node
        p2 = self.head.next_node.next_node

        if p1 == node:
            self.remove_node(self.head, p1)
            return

        while p2 != self.tail:
        
            if p2 == node:
                self.remove_node(p1, p2)

            p1 = p1.next_node
            p2 = p2.next_node


    def get_node(self, n):
         
        if n < 0 or n >= self.count:
            raise Exception("The index you have provided is out of bounds")
        
        i = 0
        current = self.head
        while i < n:
            i += 1 
            current = current.next_node

        return current


    def remove_node(self, parent, child):
        parent.next_node = child.next_node
        
    
    def print(self):

        items = []
        current = self.head

        while current is not None:
            items.append(current.item)        
            current = current.next_node

        print(items)

    class Node:
     
         def __init__(self, item, next_node = None):
             self.item = item
             self.next_node = next_node




if __name__ == '__main__':
    
    args = sys.argv[1:]
    linked_list = LinkedList()
    [linked_list.add(i) for i in range(10)]
    node = linked_list.get_node(5)
    print(node.item)
    linked_list.remove_from_middle(node)
    linked_list.print() 
    try:
        linked_list.remove_from_middle(linked_list.get_node(0))
    except:
        print("Successs")
