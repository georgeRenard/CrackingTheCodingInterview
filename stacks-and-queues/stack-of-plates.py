import sys


def problem():
    """
        Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
        Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
        threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
        composed of several stacks and should create a new stack once the previous one exceeds capacity.
        SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
        (that is, pop () should return the same values as it would if there were just a single stack).
        FOLLOW UP
        
        Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack. 
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

        self.count -= 1

        if self.count == 0:
            element = self.head.item 
            self.head = None
            self.count = 0
            return element

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

    def __repr__(self):
        return "Stack({0})".format([x for x in self])
        

    class StackIterator:
        

        def __init__(self, head, count):
            self.current = head
            self.count = count
            self.ind = 0

        def __next__(self):
            
            if self.ind >= self.count:
                raise StopIteration()

            self.ind += 1
            if self.current is None:
                return None
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


class SetOfStacks:


    def __init__(self, size):
        self.size = size
        self.count = 0
        self.arr = [Stack()]
        self.head = 0

    
    def push(self, item):

        if self.arr[self.head].count + 1 > self.size:
            self.head += 1
            self.arr.append(Stack())

        self.count += 1
        
        self.arr[self.head].push(item)
    

    def pop(self):
        
        if self.arr[self.head].isEmpty():
            del self.arr[self.head]
            self.head -= 1

        
        if self.head == 0 and self.arr[self.head].isEmpty():
            raise Exception("You cannot remove an item from an empty stack")

        element = self.arr[self.head].pop()
        self.count -= 1
        
        return element

    
    def peek(self):

        if self.count == 0:
            raise Exception("You cannot peek into an emtpy stack")

        return self.arr[self.head].peek()


    # We can do this with nodes, but using the already created stack class is way easier
    # Also, using a data structure that allows access by idex is the fastest way to implement this functionality
    # Point: An array-based stack would be way better here because of the random access
    def pop_at(self, index):
     
        if self.count <= index or index < 0:
            raise Exception("Cannot pop an item at an invalid index {0}".format(index))
    
        stack_ind = index // self.size
        internal_ind = index - (self.size * stack_ind) + 1 
        stack = self.arr[stack_ind]
        stack_head = stack.head

        steps = stack.count - internal_ind

        for i in range(steps):
            # Move head
            if stack_head is None:
                return None

            stack_head = stack_head.prev_node

        if stack_head is None:
            return None
                
        prev = stack_head.prev_node
        nxt = stack_head.next_node

        if prev is not None:
            prev.next_node = nxt
        
        if nxt is not None:
            nxt.prev_node = prev

        stack.count -= 1

        items = Stack() 

        head = self.head
        while head > stack_ind:

            while not self.arr[head].isEmpty():
                items.push(self.arr[head].pop())
            head -= 1

        while self.head > stack_ind:
            del self.arr[self.head]
            self.count -= self.size
            self.head -= 1
    
        while not items.isEmpty():
            self.push(items.pop())
            
        return stack_head.item


if __name__ == '__main__':
    args = sys.argv[1:]
    s = SetOfStacks(4)
    [s.push(i) for i in range(42)]
    print([s.pop_at(i) for i in [1, 30, 12, 7, 28]])
