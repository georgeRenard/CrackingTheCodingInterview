import sys



def problem():
    """
    Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
    this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
    node never differ by more than one.
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

        return self.__is_BST(self.root)


    def __is_BST(self, current):

        if current is None:
            return True

        res = True

        if current.left is not None:
            res = res and  current.value >= current.left.value
            
        if current.right is not None:
            res = res and current.value <= current.right.value

        res = res and self.__is_BST(current.left)
        res = res and self.__is_BST(current.right)

        return res


    def __update_height(self, current):

        if current is None:
            return 0

        left = 0 if current.left is None else current.left.height
        right = 0 if current.right is None else current.right.height

        if abs(left - right) > 1:
            raise Exception("The tree is unbalanced")
        
        current.height = 1 + self.__update_height(current.left) + self.__update_height(current.right) 

        return current.height


    def is_balanced(self):
        
        if self.root is None:
            raise Exception("An empty tree can never be balanced")

        self.__update_height(self.root)

        return self.__is_balanced(self.root)


    # You could further optimize this by attaching the balance factor to the node directly and adjusting as needed
    # It would just happen to look like an AVL tree
    def __is_balanced(self, current):
        
        return abs(self.root.left.height - self.root.right.height) <= 1
    


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

    arr = [1, 2, 4, 12, 35, 41, 72, 102, 562]
    tree = BST.build_from_sorted_array(arr)
    tree.dump()
    print("The tree {0} BST".format("is" if tree.is_BST() else "is not")) 
    print("The tree {0} balanced".format("is" if tree.is_balanced() else "is not"))

