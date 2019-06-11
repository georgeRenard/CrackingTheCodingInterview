

class Queue:


    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0


    def size(self):
        return self.count


    def empty(self):
        return self.count == 0


    def enqueue(self, item):

        new_node = self.QueueNode(item)
        self.count += 1

        if item is None:
            raise Exception("You cannot push a None value into the Queue")

        if self.head is None and self.tail is None:
            self.tail = new_node
            self.head = new_node 
            return


        self.tail.next_node = new_node
        self.tail = new_node

    def dequeue(self):

        if self.head is None:
            raise Exception("You cannot remove an element from an empty Queue")

        element = self.head.value
        nw = self.head.next_node
        self.head = nw 
        self.count -= 1

        if self.count == 0:
            self.tail = None
            self.head = None

        return element 


    def peek(self):

        if self.head is None:
            raise Exception("Cannot peek into an empty queue")

        return self.head.value

    
    def __iter__(self):
        return self.QueueIterator(self.head, self.count)


    def __repr__(self):
        return [x for x in self].__repr__()


    class QueueNode:

        def __init__(self, value):
            self.next_node = None
            self.value = value

    
        def __repr__(self):
            return "QueueElement({0})".format(self.value)


    class QueueIterator:

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


