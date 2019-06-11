import sys



def problem():
    """
    Validate BST: Implement a function to check if a binary tree is a binary search tree. 
    """
    pass



class BST:


    def __init__(self):
        self.count = 0
        self.root = None


    @staticmethod
    def build_from_sorted_array(arr):

        root = BST.__build_from_sorted_array(arr)

        bst = BST()
        bst.root = root
        
        return bst

    @staticmethod
    def __build_from_sorted_array(arr):

        size = len(arr)

        if size == 1:
            return BST.BSTNode(arr[0])
        
        if size == 0:
            return 

        median_index = size // 2

        left = arr[0: median_index]
        right = arr[median_index + 1 : ]

        root_val = arr[median_index]
        root = BST.BSTNode(root_val)

        left_subtree_root = BST.__build_from_sorted_array(left)
        right_subtree_root = BST.__build_from_sorted_array(right)

        root.left = left_subtree_root
        root.right = right_subtree_root

        return root 
            

    def is_BST(self):
        
        if self.root is None:
            raise Exception("You have got yourself an empty tree")

        return self.__is_BST(self.root, None, None)


    def __is_BST(self, current, current_min, current_max):


        if current is None:
            return True

        res = True

        if current_min is not None:
            res = res and current.value > current_min

        if current_max is not None:
            res = res and current.value <= current_max

        print(current.value)
        print("Min: {0}, Max: {1}".format(current_min, current_max))

        res = res and self.__is_BST(current.left, current_min, current.value) 

        res = res and self.__is_BST(current.right, current.value, current_max)
        
        return res


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

        def __init__(self, value):
            self.value = value
            self.left = None 
            self.right = None 
            self.height = 0




if __name__ == '__main__':
    args = sys.argv[1:]

    # arr = [1, 2, 4, 12, 35, 41, 72, 102, 562]
    # tree = BST.build_from_sorted_array(arr)
    # tree.dump()
    tree = BST()

    tree.root = BST.BSTNode(7)
    tree.root.left = BST.BSTNode(3)
    tree.root.left.right = BST.BSTNode(5)
    tree.root.left.left = BST.BSTNode(1)
    tree.root.right = BST.BSTNode(9)
    tree.root.right.right = BST.BSTNode(14)
    tree.root.right.left = BST.BSTNode(8)

    tree.dump()
    print("The tree {0} BST".format("is" if tree.is_BST() else "is not")) 

