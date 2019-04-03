import sys
from collections import deque


def problem():
    """
        Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
        beginning of the loop.
        DEFINITION
        Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
        as to make a loop in the linked list.
        EXAMPLE
            Input: A -> B -> C -> D -> E -> C [the same C as earlier]
            Output: C 
    """
    pass


def considerations():
    """
        You can't possibly use some sort of value specific cashing since we are working with pointers/references
        here. Therefore, some recursive, graph-like traversal should be involved. A circular linked list is just a 
        graph-like structure. 
        You cannot effectively use a length property. Trying to acquire the length of the circular linked-list would
        result in an infinite loop.
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
        self.tail.next_node = new_node
        self.tail = new_node



    # A hella easier way would be to attach a property "visited" to each node. That would allow us to find a loop
    # with extreme ease. I don't think that is allowed tho 
    # This one uses O(n) memory and O(n) runtime
    # The question is, can we avoid using a map or a set - in other words avoid using hashing
    # even though pointers can be looked at as plain integers
    def detect_loop(self):

        visited_edges = {}
         
        current = self.head
        while current is not None:

            if current not in visited_edges:
                visited_edges[current] = True
            else:
                return current

            current = current.next_node


        return None

    
    def get_node(self, i):

        if i < 0 or i >= self.count:
            raise Exception('Invalid index') 

        current = self.head

        j = 0
        while j < i:
            current = current.next_node
            j += 1 

        return current


    def insert(self, node, index = 0):
       
        if index < 0 or index >= self.count:
            raise Exception("Invalid index")
    
        i = 0
        current = self.head 
           
        while i < index - 1:
            current = current.next_node
         
        temp = current.next_node
        current.next_node = node
        node.next_node = temp


    def prnt(self): 
    
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
        
        
        def __repr__(self):

            return str(self.item)



def create_loop(linked_list, i, j):

    node = linked_list.get_node(i)
    node_2 = linked_list.get_node(j)
    node.next_node = node_2


if __name__ == '__main__':
    
    args = sys.argv[1:]
    linked_list = LinkedList() 
    linked_list.add("A")
    linked_list.add("B")
    linked_list.add("C")
    linked_list.add("D")
    linked_list.add("E")
    create_loop(linked_list, 4, 2)
    node = linked_list.detect_loop()
    print(node)
