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

    def __init__(self, head=None):
        
        self.head = head 
        self.tail = None
        self.count = 0


    def add(self, item):

        if item is None:
            raise Exception("You cannot add a None object inside the list")

        new_node = self.Node(item)
        self.count += 1 
        
        if self.head is None and self.tail is None:
            self.head = new_node 
            self.tail = self.head
            return

        self.tail.next_node = new_node
        new_node.prev_node = self.tail
        self.tail = new_node


    def add_first(self, item):
        
        if item is None:
            raise Exception("You cannot add a None object inside the list")


        new_node = self.Node(item)
        self.count += 1

        if self.head is None and self.tail is None:
            self.tail = new_node
            self.head = self.tail
            return
        
        self.head.prev_node = new_node
        new_node.next_node = self.head
        self.head = new_node
 

    def prnt(self):

        items = []
        current = self.head

        while current is not None:
            items.append(current.item)
            current = current.next_node
 
        print(items)


    def partition_at(self, x):
        self.__partition_runner_up(x)



    # This is the best first_solution I could come up with. I doubt that it is correct since I have that
    # strange feeling that I miss something big in the problem description
    # This algorithm is O(n+n) with no additional memory required
    # It is also an in-place version (That might be bad tbh)
    def __in_place_partition_without_order(self, x):
        
        # Createa a pointer to the tail
        # Here I can assume that I am not allowed to have that pointer cached already
        tail = self.head
        while tail.next_node is not None:
            tail = tail.next_node


        head = self.head

        while tail != head:

            if head.item < x:
                head = head.next_node
                continue
            
            if tail.item >= x:
                tail = tail.prev_node 
                continue        
            
            temp = head.item
            head.item = tail.item
            tail.item = temp
            head = head.next_node
            tail = tail.prev_node


    # This version of the algorithm is a little bit better than the previous. It runs in O(n) time with no
    # auxiliry memory required (besides the one you use for the deep copy)
    # We don't want to pass around node references - a reference should belong to only one data structure
    # The connector pointer could possible be garbage collected but it would not be worth it
    # Interesting, this seems to be a pretty optimal solution. This implies that I need to reduce the
    # number of pointers to one
    def __partition_optimized(self, x):
        
        head = None 
        tail = None 
        connector = self.Node(None)
        
        current = self.head
  
        
        # I should probably move this to the parent procedure
        if current is None:
            raise Exception("You cannot partition an empty list")

        while current is not None:

            value = current.item 
            new_node = self.Node(value)

            if value < x:

                if head is None:
                    head = new_node 
                    connector.prev_node = head
                else:
                    head.prev_node = new_node 
                    new_node.next_node = head 
                    head = new_node
                     
            else: 

                if tail is None:
                    tail = new_node 
                    connector.next_node = tail
                else:
                    tail.next_node = new_node
                    new_node.prev_node = tail
                    tail = new_node

            current = current.next_node
            

        connector.prev_node.next_node = connector.next_node
        connector.next_node.prev_node = connector.prev_node

        return head

   
    # This one is pretty fast, O(n) runtime with only 2 pointers
    # It seems that this is the most optimal solution
    def __partition_two_references(self,x):

        linked_list = LinkedList()

        current = self.head
        while current is not None:

            value = current.item
            linked_list.add_first(value) if value < x else linked_list.add(value)
            current = current.next_node
 
    
        return linked_list


    def __partition_runner_up(self, x):
    
        start = self.head
        runner_up = self.head.next_node

        while runner_up is not None:
            
            if start.item < x:
                start = start.next_node 

            if runner_up.item < x and runner_up != start:
                prev = runner_up.prev_node
                nxt = runner_up.next_node
                prev.next_node = nxt

                if nxt is not None:
                    nxt.prev_node = prev

                st_prev = start.prev_node 
                start.prev_node = runner_up
                 
                if st_prev is not None:
                    st_prev.next_node = runner_up

                runner_up.next_node = start
                runner_up.prev_node = st_prev 
                

            runner_up = runner_up.next_node


    class Node:
    
        def __init__(self, item, next_node=None, prev_node=None):
            self.item = item
            self.next_node = next_node
            self.prev_node = prev_node


if __name__ == '__main__':
    
    args = sys.argv[1:]
    
    elements = [3, 5, 8, 5, 10, 2, 1]
    partition_value = 5
    linked_list = LinkedList()   
    map(linked_list.add, elements) 
    linked_list.partition_at(partition_value)
    linked_list.prnt()
    
