import sys



def problem():
    """
    Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
    binary search tree. You may assume that each node has a link to its parent. 
    """
    pass



class BST:


    def __init__(self):
        self.count = 0
        self.root = None


    def add(self, value):

        if value is None:
            raise Exception("You cannot add a None value to the tree")

        self.root = self.__add(self.root, None,  value)
        self.count += 1


    def __add(self, current_node, parent_node, value):


        if current_node is None:
            return self.BSTNode(value, parent=parent_node)

        if value <= current_node.value:
            current_node.left = self.__add(current_node.left, current_node, value)
        else:
            current_node.right = self.__add(current_node.right, current_node, value)


        return current_node
    

    def find_successor(self, value):

        if self.root is None:
            raise Exception("You cannot find a successor in an empty tree")

        node = self.__find_by_value(self.root, value)

        if node is None:
            raise Exception("No such element can be found in the tree structure")

        return self.__find_successor(node).value


    def __find_successor(self, node):

        current = node
        

        if current.right is not None:
            return self.__find_leftmost(current.right)

        if current.parent.value >= node.value:
            return current.parent

        else:
            while current.parent is not None:

                if current.parent.value > node.value:
                    return current.parent

                current = current.parent

       
        return self.BSTNode(None)
    
    def __find_leftmost(self, current):

        if current.left is None:
            return current


        return self.__find_leftmost(current.left)


    def __find_by_value(self, current, value):

        if current is None:
            return None

        if current.value > value:
            return self.__find_by_value(current.left, value)

        elif current.value < value:
            return self.__find_by_value(current.right, value)


        return current


    def dump(self):

        if self.root is None:
            raise Exception("Cannot dump an empty tree")
        
        self.__dump(self.root)


    def __dump(self, current, indent = 0):

        if current is None:
            return

        print("{0}{1}".format(" " * indent, current.value))
        
        self.__dump(current.left, indent + 2)
        self.__dump(current.right, indent + 2)
        

    def __repr__(self):
        return self.root.__repr__() 


    class BSTNode:

        def __init__(self, value, parent=None):
            self.value = value
            self.left = None 
            self.right = None 
            self.parent = parent 



if __name__ == '__main__':
    args = sys.argv[1:]

    tree = BST()

    tree.add(20)
    tree.add(8)
    tree.add(22)
    tree.add(4)
    tree.add(12)
    tree.add(10)
    tree.add(14)

    print(tree.find_successor(8))
    print(tree.find_successor(10))
    print(tree.find_successor(12))
    print(tree.find_successor(14))
    print(tree.find_successor(22))
    print(tree.find_successor(20))

    

