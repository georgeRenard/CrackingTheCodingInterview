import sys
from time import time

from termcolor import colored



def problem():
    """
        Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list. 
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


    def kth_to_last(self, k):
        """
            This function is the brute force version of the kth to last problem. It runs in O(k) where k is the kth last element
            in the linked list and O(1) additional memory
        """

        i = (self.count - 1) - k 

        if i < 0:
            raise Exception("Invalid argument. The number of items in the list is less than {0}".format(k))

        current = self.head
        
        j = 0
        while j < i:
            current = current.next_node
            j += 1

        return current.next_node.item 


    def kth_to_last_runner_up(self, k):
        """
            This function runs in O(k/2) where k is the kth last element in the linked list and O(1) additional memory
        """

        index = (self.count - 1) - k   
        # print("{0} - {1} = {2}".format(self.count - 1, k, index))

        if index < 0:
            raise Exception("Invalid argument. The number of items in the list is less than {0}".format(k))

        loops = index // 2 

        current = self.head
 
        j = 0
        while j < loops:
            current = current.next_node.next_node 
            j += 1

        if k % 2 == 0:
            current = current.next_node

        return current.next_node.item

 
    class Node:
    
        def __init__(self, item, next_node = None):
            self.item = item
            self.next_node = next_node 


# I am too lazy for this sh*t
def performance_test(elements_count):
    
    start = time()
    linked_list = LinkedList()
    [linked_list.add(i) for i in range(elements_count)]
    end = time()

    print(colored("Building the list took {0:2f}".format(end - start), 'green'))
    
    start = time()
    linked_list.kth_to_last_runner_up(5) 
    end = time()
    print('\n')
    print(colored("The kth last element implemented with a runner up runs in {0:2f} ms".format(end - start), 'green')) 

    start = time()
    linked_list.kth_to_last(5)
    end = time()
    print('\n')
    print(colored("The kth last element brute force runs in {0:2f} ms".format(end - start), 'green')) 
    

if __name__ == '__main__':

    args = sys.argv[1:]
    #performance_test(10000000)
    linked_list = LinkedList()
    [linked_list.add(i) for i in range(10000)]
    print(linked_list.kth_to_last_runner_up(5))
    print(linked_list.kth_to_last_runner_up(6))
    print(linked_list.kth_to_last_runner_up(7))
    print(linked_list.kth_to_last_runner_up(11)) 

