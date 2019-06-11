


class Stack:


    def __init__(self):
        self.head = None
        self.count = 0


    def size(self):
        return self.count


    def push(self, item):

        new_node = self.StackNode(item)
        self.count += 1

        if item is None:
            raise Exception("You cannot push a None value into the Stack")

        if self.head is None:
            self.head = new_node 
            return

        new_node.next_node = self.head
        self.head = new_node


    def pop(self):

        if self.head is None:
            raise Exception("You cannot remove an elemtn from an empty Stack")

        element = self.head.value
        nw = self.head.next
        self.head = self.head.next_node
        self.count -= 1

        return element 


    def peek(self):

        if self.head is None:
            raise Exception("Cannot peek into an empty stack")

        return self.head.value

    
    def __iter__(self):
        return self.StackIterator(self.head, self.count)


    def __repr__(self):
        return [x for x in self].__repr__()


    class StackNode:

        def __init__(self, value):
            self.next_node = None
            self.value = value

    
        def __repr__(self):
            return "StackElement({0})".format(self.value)


    class StackIterator:

        def __init__(self, head, size):

            self.current_index = 0
            self.current = head
            self.size = size


        def __next__(self):

            if self.current_index >= self.size:
                raise StopIteration()
            
            el = self.current.value
            self.current = self.current.next_node
            self.current_index += 1
            return el


