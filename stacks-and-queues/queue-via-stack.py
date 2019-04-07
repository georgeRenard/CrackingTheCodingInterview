import sys


def problem():
    """
        Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks. 
    """
    pass 



class Stack:

    def __init__(self):
        self.head = None
        self.min_head = None
        self.min_tail = None
        self.count = 0 


    def push(self, item):

        if item is None:
            raise Exception("Cannot add a value of None to the stack")

        self.count += 1
        new_node = self.Node(item)
        
        if self.head is None:
            self.head = new_node
            return
            
        self.head.next_node = new_node
        new_node.prev_node = self.head
        self.head = new_node


    def pop(self):
        
        if self.head is None:
            raise Exception("You cannot remove elements from an empty stack")

        if self.count == 1:
            element = self.head.item 
            self.head = None
            self.count = 0
            return element

        self.count -= 1
        new_head = self.head.prev_node
        new_head.next_node = None
        element = self.head.item
        self.head = new_head

        return element


    def peek(self):

        if self.head is None:
            raise Exception("Cannot retrieve an item from an empty stack")

        return self.head.item


    def dump(self):
        current = self.head
        while current is not None:
            print(current.item)
            current = current.prev_node


    def isEmpty(self):
        return self.count == 0


    def __iter__(self):
        return self.StackIterator(self.head, self.count)
        

    class StackIterator:
        

        def __init__(self, head, count):
            self.current = head
            self.count = count
            self.ind = 0

        def __next__(self):
            
            if self.ind >= self.count:
                raise StopIteration()

            self.ind += 1
            element = self.current.item
            self.current = self.current.prev_node
            return element


    class Node:

        def __init__(self, item, next_node = None, prev_node = None):
            self.item = item
            self.next_node = next_node
            self.prev_node = prev_node


        def __repr__(self):
            return "Node Object - Value: {0}".format(self.item)



class Queue:

    def __init__(self):
        # Initialize the stacks and the count 
        self.count = 0
        self.stack_1 = Stack()
        self.stack_2 = Stack()


    # The runtime complexity of this procedure is O(1) with O(n) memory required
    def enqueue(self, item):
        self.stack_1.push(item)
        self.count += 1


    # The runtime of this function is O(n) at first, but gets better with more elements present. 
    # E.g if we call it with 500 elements in the first stack. The runtime will be O(n) but the next
    # 500 dequeue operations are free - O(1)
    # Therefore, this function has runtime of O(1) amortized 
    def dequeue(self):

        if self.stack_2.isEmpty():

            while not self.stack_1.isEmpty():
                self.stack_2.push(self.stack_1.pop())

        return self.stack_2.pop()



    def isEmpty(self):
        pass


if __name__ == '__main__':
    args = sys.argv[1:]
    q = Queue()
    [q.enqueue(i) for i in range(50)]
    print([q.dequeue() for i in range(50)])
