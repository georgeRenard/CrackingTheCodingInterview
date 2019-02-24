import sys
import numpy


class Node():
   

    # If it is so important to remove all the duplicates we can do some tricky case optimizations
    # We can chain specifically duplicate nodes together and keep all the distinct items in a map
    # This way we can reduce the overall time to O(d) where d is the number of duplicates
    def __init__(self, item):
        self.item = item   
        self.next = None
        self.next_alike = None
        self.prev = None
        self.distinct_map = {item: self}
        self.count = 0
   
   
    def add(self, item):
        
        if item == None:
            raise Exception("You cannot add a 'None' value")

        current = self 

        while current.next is not None:
            current = current.next

        current.next = Node(item)
        self.count += 1
 

    def __add(self, node):
        
        current = self
        while current.next is not None:
            current = current.next
 
        current.next = node
        node.prev = current
        self.count += 1


    def add_memory_heavy(self, item):
    
        if item == None:
            raise Exception("You cannot add a 'None' value")
        
        node = Node(item) 
        
        if item in self.distinct_map:
            n = self.distinct_map[item]
            while n.next_alike is not None:
                n = n.next_alike     
            n.next_alike = node
        else:
            self.distinct_map[item] = node

        self.__add(node)

     
    # In my opinion, the best conceivable runtime is O(n), but in reality you could do some optimizations by adding more
    # pointers and even using more memory to do even better
    def remove_duplicates(self):
        self.__remove_duplicates_buffer_free()


    def __remove_duplicates_fast_memory_heavy(self):
        """
            This function will require a pointer backwards and it will be able to perform in O(d * duplicate_count) runtime where d is the 
            number of distinct elements in the map and in O(2n) additional memory
            We can speed up things by introducing a little bit more caching
        """
        for (item, start_node) in self.distinct_map.items():
            current = start_node.next_alike
            while current is not None:
                self.__remove_node(current)       
                current = current.next_alike  
            

    def __remove_duplicates_buffer_free(self):
     
        bit_vector = 0 

        current = self
         
        nodes_to_remove = []

        while current is not None:
            
            mask = 1 << current.item
            if mask & bit_vector == 0:
                bit_vector = bit_vector | mask
            else:
                nodes_to_remove.append(current)

            current = current.next
                       
        for node in nodes_to_remove:
            self.__remove_node(node)
        
        
        
    def __remove_duplicates_memory_heavy(self):
        """
            This function removes all duplicates from the singly-linked list in O(n) time and O(n) memory
        """
        m = {self.item: 1} 
        current = self.next
        prev = self
        nodes_to_remove = []

        while current is not None:

            if current.item not in m:
                m[current.item] = 1
            else:
                nodes_to_remove.append((prev, current))

            prev = current 
            current = current.next
        
        for i in range(len(nodes_to_remove) - 1):
            this = nodes_to_remove[i]
            nx = nodes_to_remove[i + 1]  
            if this[1] == nx[0]:
                nodes_to_remove[i + 1] = (this[0], nx[1]) 
                continue
                     
            self.__remove(this) 

        if len(nodes_to_remove) !=  0:
            self.__remove(nodes_to_remove[-1])
         


    def remove(self, item):

        parent = self.find_parent_node(item)

        if parent is None:
            raise Exception("Item {0} is not present in the list".format(item))


    def __remove(self, parent_child_pair):

        parent = parent_child_pair[0]
        child = parent_child_pair[1]

        parent.next = child.next
        self.count -= 1 

    def __remove_node(self, node):
        
        parent = node.prev
        nx = node.next
       
        parent.next = nx
        if nx is not None:
            nx.prev = parent


    def find_parent_node(self, item):
        pass

   
    def print(self):

        current = self
        items = []

        while current is not None:
            items.append(current.item)
            current = current.next
    
        return items

    

if __name__ == '__main__':
    
    args = sys.argv[1:]
    linked_list = Node(1)
    integers = [numpy.random.randint(50) for i in range(int(args[0]))]
    [linked_list.add_memory_heavy(item) for item in integers]
    integers.append(1)
    linked_list.remove_duplicates()

    s1 = set(integers)
    s2 = linked_list.print()

    s1 = sorted(s1)
    s2 = sorted(s2)
  
    print(s1)
    print(s2)
    for (l, r) in zip(s1, s2):
        if l != r:
            print("Sets are not equal")
            exit() 

    print("Congratulations... Sets are equal") 
        

