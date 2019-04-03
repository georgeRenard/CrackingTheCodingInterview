import sys


def problem():
    """
        Intersection: Given two (singly) linked lists, determine if the two lists intersect. 
        Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth
        node of the first linked list is the exact same node (by reference) as the jth node of the second
        linked list, then they are intersecting. 
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

 
    def insert_at(self, node, i):
        """
            We can speed up this function by determining whether the index is closer to the end or to the begining
            but since this is not a doubly-linked list we should pretty much be satisfied with the current implementation
        """
         
        if i < 0 or i >= self.count: 
            raise Exception("The index you provided as an argument is out of bounds.")
 
        j = 0
        current = self.head

        while j < i - 1:
            current = current.next_node
            j += 1
       
        nxt = current.next_node 
        current.next_node = node
        node.next_node = nxt
             
        
    def get_node(self, i):
        
        if i < 0 or i >= self.count:
            raise Exception("The index you provided as an argument is out of bounds.")
        
        j = 0
        current = self.head
        while j < i:
            current = current.next_node 
            j += 1  
 
        return current


    def find_intersection(self, other_list):
    
        #return self.__find_intersection_brute_force(other_list) 
        return self.__find_intersection_fast(other_list)

    
    def __find_intersection_fast(self, other_list):
        """
            This function uses some caching to perform the intersection check way faster
        """   

        # If we build the set procedurally, we can have reduce the one time memory requirement to O(1), however, we still
        # increase the overall memory requirement of the data structure by O(n)
        s = set()
        current = self.head
        other_current = other_list.head


        while other_current is not None:
            s.add(other_current)
            other_current = other_current.next_node
        

        while current is not None:
            
            if current in s:
                return current
        
            current = current.next_node
        
        return None        
   
 
    def __find_intersection_brute_force(self, other_list):
        """
            This implementation of the intersection check is the most naive one and it runs in O(n^2). The only upside is that
            it requires no caching (no additional memory)
        """
        
        current = self.head

        while current is not None:
 
            other_current = other_list.head
            while other_current is not None:
                if current == other_current:
                    return current           
                other_current = other_current.next_node
            
            current = current.next_node

        return None


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
    other_linked_list = LinkedList()
    node = LinkedList.Node(-5)
    [linked_list.add(i) for i in range(10000)]
    [other_linked_list.add(i) for i in range(10000)] 
    linked_list.insert_at(node, 7250)
    other_linked_list.insert_at(node, 1053)
    result = other_linked_list.find_intersection(linked_list)

    print(result == node)    
