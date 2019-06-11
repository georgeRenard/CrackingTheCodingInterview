import sys
from queue import Queue


def problem():
    """
    Paths with Sum: You are given a binary tree in which each node contains an integer value (which
    might be positive or negative). Design an algorithm to count the number of paths that sum to a
    given value. The path does not need to start or end at the root or a leaf, but it must go downwards
    (traveling only from parent nodes to child nodes).
    """
    pass


class Tree:


    def __init__(self):
        self.root = None
        self.count = 0


    def add(self, item):

        self.root = self.__add(self.root, item)
        self.count += 1


    def __add(self, current, item):

        if current is None:
            return self.TreeNode(item)

        
        if current.value >= item:
            current.left = self.__add(current.left, item)
        else:
            current.right = self.__add(current.right, item)


        return current


    def paths_with_sum(self, sm):
        """

            !Returns an empty collection on empty tree!

        """

        if self.root is None:
            return []

        buf = []

        return buf

    """
        
        find_path_left_subtree
        find_path_right_subtree

    """


    # This solution is correct but does not return an optimal solution to the problem
    # It misses an important requirement that not every path is from the root
    def __paths_with_sum(self, current, sm, buf, temp_buf, current_sum):

        if current is None:
            return

        current_sum += current.value
        temp_buf.append(current)

        if current_sum == sm:
            buf.append(temp_buf)
            

        self.__paths_with_sum(current.left, sm, buf, temp_buf[:], current_sum)

        self.__paths_with_sum(current.right, sm, buf, temp_buf[:], current_sum)



    def dump(self):

        self.__dump(self.root)

    
    def __dump(self, current, indent = 0):

        if current is None:
            return

        print("{0}{1}".format(indent * " ", current.value))

        self.__dump(current.left, indent + 2)

        self.__dump(current.right, indent + 2)




    class TreeNode:

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None


        def __repr__(self):
            return "Node({0})".format(self.value)



if __name__ == '__main__':
    args = sys.argv[1:]

    tree = Tree()

    tree.add(13)
    tree.add(3)
    tree.add(14)
    tree.add(1)
    tree.add(7)
    tree.add(18)
    tree.add(12)
    tree.add(2)
    tree.add(10)
    tree.dump()
    
    print(tree.paths_with_sum(45))
    
