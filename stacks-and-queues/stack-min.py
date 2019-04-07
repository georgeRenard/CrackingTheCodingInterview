import sys


def problem():
    """
    How would you design a stack which, in addition to push and pop, has a function min
    which returns the minimum element? Push, pop and min should all operate in 0(1) time. 
    """
    pass 



class Stack:

    def __init__(self):
        self.head = None
        self.min_head = None
        self.min_tail = None
        self.count = 0 


    # I was able to reduce the runtime of the min operation to O(1) but that cost me increase in the push operation
    # I honestly cannot think of another memory tradeof for everything to run in O(1) (At the moment at least)
    # This push implementation runs in O(min(abs(hi - i), abs(lo - i))) where hi is the current highest element and
    # lo is the current minimum element
    # For that purpose, I had to introduce two new pointers
    # I will be thinking about further imporovements through the increase of memory usage
    def push(self, item):

        if item is None:
            raise Exception("Cannot add a value of None to the stack")

        self.count += 1
        new_node = self.Node(item)
        
        if self.head is None:
            self.head = new_node
            self.min_head = self.head
            self.min_tail = self.head
            return
            
        self.head.next_node = new_node
        new_node.prev_node = self.head
        self.head = new_node

        if item <= self.min_head.item:
            self.min_head.prev_min = new_node
            new_node.next_min = self.min_head
            self.min_head = new_node
        elif item >= self.min_tail.item:
            self.min_tail.next_min = new_node
            new_node.prev_min = self.min_tail
            self.min_tail = new_node
        else:
            # The value is in between
            current_min = self.min_head
            while item > current_min.item:
                current_min = current_min.next_min
                
            new_node.next_min = current_min
            new_node.prev_min = current_min.prev_min
            current_min.prev_min.next_min = new_node
            current_min.prev_min = new_node


    # The pop operation is pretty straightforward and it will probably remain the same way throughout
    # It works in O(1) for sure
    def pop(self):
        
        if self.head is None:
            raise Exception("You cannot remove elements from an empty stack")

        self.count -= 1

        prev = self.head.prev_min
        nxt = self.head.next_min

        if prev is not None:
            prev.next_min = nxt

        if nxt is not None:
            nxt.prev_min = prev

        if self.head == self.min_head:
            self.min_head = self.min_head.next_min

        new_head = self.head.prev_node
        new_head.next_node = None
        element = self.head.item
        self.head = new_head

        return element


    def min(self):

        if self.count == 0:
            raise Exception("You cannot remove elements from an emtpy stack")
        
        min_node = self.min_head
        element = min_node.item

        self.min_head = self.min_head.next_min
        prev = min_node.prev_node
        nxt = min_node.next_node

        if prev is not None:
            prev.next_node = nxt
            
        if nxt is not None:
            nxt.prev_node = prev

        self.count -= 1
        return element


    def dump(self):
        current = self.head
        while current is not None:
            print(current.item)
            current = current.prev_node


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
            self.prev_min = None
            self.next_min = None

        def __repr__(self):
            return "Node Object - Value: {0}".format(self.item)



if __name__ == '__main__':
    args = sys.argv[1:]

    stack = Stack()

    stack.push(5)
    stack.push(6)
    stack.push(2)
    stack.push(1)
    stack.push(17)
    stack.push(11)
    stack.push(10)
    stack.push(18)
    stack.push(12)
    stack.push(2)
    stack.push(1)
    stack.dump()
    stack.pop()
    stack.pop()
    stack.pop()
    print(sorted([x for x in stack]))
    print([stack.min() for i in range(8)])
