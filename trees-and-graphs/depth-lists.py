import sys


def problem():
    """
    List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
    at each depth (e.g., if you have a tree with depth D, you'll have D linked lists). 
    """
    pass

class LinkedList:

    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None


    def isEmpty(self):
        return self.count == 0


    def add_last(self, value):

        new_node = self.LinkedListNode(value)
        self.count += 1
        
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.nxt = new_node
        new_node.prev = self.tail
        self.tail = new_node


    def remove_first(self):

        if self.head is None:
            raise Exception("You cannot remove from an empty list")

        if self.count == 1:
            el = self.head.value
            self.head = None
            self.tail = None
            self.count = 0
            return el

        element = self.head.value

        n = self.head.nxt
        n.prev = None
        self.head = n
        self.count -= 1

        return element


    def __repr__(self):

        ls = []

        current = self.head

        while current is not None:
            ls.append(current.value)
            current = current.nxt

        return ls.__repr__() 


    class LinkedListNode:

        def __init__(self, value):
            self.value = value
            self.nxt = None
            self.prev = None

        def __repr__(self):
            return str(self.value)


class BST:

    def __init__(self):
        self.count = 0
        self.root = None


    def add(self, value):

        if value is None:
            raise Exception("You cannot add a None value into the BST")

        self.count += 1
        self.root = self.__add(self.root, value)


    def __add(self, current, value):

        if current is None:
            return self.BSTNode(value)

        if current.value > value:
            current.left = self.__add(current.left, value)
        elif current.value <= value:
            current.right = self.__add(current.right, value)


        return current
        

    def extract_depth_lists(self):

        if self.root is None:
            raise Exception("You cannot extract depth lists from an empty tree structure")

        depth_map = [] 

        self.__extract_depth_lists(self.root, depth_map) 

        return depth_map 


    def __extract_depth_lists(self, current, depth_map, depth = 0):
        
        if current is None:
            return

        lst = None

        try:
            lst = depth_map[depth]
        except:
            depth_map.append(LinkedList())
            lst = depth_map[depth]

        lst.add_last(current.value)

        self.__extract_depth_lists(current.left, depth_map, depth + 1)
        self.__extract_depth_lists(current.right, depth_map, depth + 1)


    def extract_depth_lists_BFS(self):

        if self.root is None:
            raise Exception("You cannot extract depth lists from an empty tree structure")

        root = self.root

        depth = 0
        depth_map = []
        nodes = LinkedList()

        nodes.add_last((depth,root))

        while not nodes.isEmpty():
            
            (depth, current) = nodes.remove_first()
            lst = None

            try:
                lst = depth_map[depth]
            except:
                depth_map.append(LinkedList())
                lst = depth_map[depth]

            lst.add_last(current.value)

            if current.left is not None:
                nodes.add_last((depth + 1, current.left))

            if current.right is not None:
                nodes.add_last((depth + 1, current.right))

        return depth_map


    def dump(self):

        if self.root is None:
            raise Exception("You cannot dump an empty tree")

        self.__dump(self.root)


    def __dump(self, current, indent = 0):

        if current is None:
            return

        print("{0}{1}".format(" " * indent, current.value))
        self.__dump(current.left, indent + 2)
        self.__dump(current.right, indent + 2)


    class BSTNode:

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None


if __name__ == '__main__':
    args = sys.argv[1:]

    b = BST()

    b.add(5)
    b.add(7)
    b.add(3)
    b.add(12)
    b.add(11)
    b.add(24)
    b.add(51)
    b.add(1)
    b.add(-5)
    b.add(2)
    b.add(18)
    b.add(-3)

    b.dump()
    lst = b.extract_depth_lists_BFS()

    for ls in lst:
        print(ls)
