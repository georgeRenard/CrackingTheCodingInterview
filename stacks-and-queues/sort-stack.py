import sys


def problem():
    """
        Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
        an additional temporary stack, but you may not copy the elements into any other data structure
        (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty
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


    # This algorithm might not be the most optimal one since we are not allowed random access in the stack
    # We can only work with pop, peek and push with an aux stack-like buffer
    def sort_descending(self):
        # Creating a temporary stack-based buffer  
        buff = Stack()

        if self.count == 1:
            return

        current = self.head
        item = current.item

        while current.prev_node is not None:
            
            if item >= current.prev_node.item:
                buff.push(current.prev_node.item)
            else:
                buff.push(item)
                item = current.prev_node.item

            current = current.prev_node
            self.pop()
            

        current.item = item
        while not buff.isEmpty():
            # Find the next candidates for largest item

            current_item = buff.pop()

            if current_item > self.peek():
                # Do something
                self_head = self.head
                self_head_item = self_head.item

                while self_head_item < current_item:
                    self.pop()
                    buff.push(self_head_item)
                    self_head = self_head.prev_node
                    self_head_item = self_head.item

                self.push(current_item)
            else:
                self.push(current_item)

        
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



if __name__ == '__main__':
    args = sys.argv[1:]
    stack = Stack()
    stack.push(5)
    stack.push(8)
    stack.push(4)
    stack.push(3)
    stack.push(7)
    stack.push(9)
    stack.push(10)
    stack.push(6)
    stack.push(5)
    stack.push(2)
    stack.sort_descending()
    print([x for x in stack])
