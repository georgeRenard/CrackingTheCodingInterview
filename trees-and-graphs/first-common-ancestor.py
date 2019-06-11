import sys



def problem():
    """
    First Common Ancestor: Design an algorithm and write code to find the first common ancestor
    of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
    necessarily a binary search tree
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


    def lowest_common_ancestor(self, left, right):

        if self.root is None:
            raise Exception("You cannot find a lowest common ancestor in an empty tree")


        # Considering that this tree is not a binary search tree, the potential runtime here is O(2n) where n is the
        # number of elements inside the tree. Which means that this solution is pretty much "naive"
        lnode = self.__find_by_value(self.root, left)
        rnode = self.__find_by_value(self.root, right)

        if lnode is None or rnode is None:
            raise Exception("One or both of the values that were passed into the function are not present inside the tree")

        return self.__lowest_common_ancestor_naive(lnonde, rnode)


    def __lowest_common_ancestor_naive(self, left, right):





    def __find_by_value(self, current, value):

        if current is None:
            return None

        if current.value == value:
            return current

        node = self.__find_by_value(current.left, value)

        if node is None:
            node = self.__find_by_value(current.right, value)

        return node


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


        def __str__(self):
            return "BSTNode({0})".format(self.value)



if __name__ == '__main__':
    args = sys.argv[1:]

    tree = BST()

    BSTNode = BST.BSTNode

    tree.root = BSTNode(5)
    tree.root.left = BSTNode(13)
    tree.root.right = BSTNode(16)
    tree.root.left.left = BSTNode(9)
    tree.root.left.right = BSTNode(10)
    
