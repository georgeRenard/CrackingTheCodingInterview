import sys
from queue import Queue


def problem():
    """
    BST Sequences: A binary search tree was created by traversing through an array from left to right
    and inserting each element. Given a binary search tree with distinct elements, print all possible
    arrays that could have led to this tree.
    EXAMPLE
    Input:

        Root: 2
            Left: 1
            Right: 3

        Output: {2, 1, 3}, {2, 3, 1}
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

    
    def find_addition_sequences(self):

        if self.root is None:
            return []

        sequences = [] 

        self.__find_addition_sequences(self.root, sequences, [])
        self.__find_addition_sequences_inverse(self.root, sequences, [])
        self.__find_addition_sequences_bfs(sequences)
        self.__find_addition_sequences_bfs_reverse(sequences)

        return sequences 


    def __find_addition_sequences_bfs(self, sequences):

        q = Queue()

        q.enqueue(self.root)
        current_sequence = []

        while not q.empty():

            current = q.dequeue()

            current_sequence.append(current.value) 

            if current.left is not None:
                q.enqueue(current.left)
            if current.right is not None:
                q.enqueue(current.right)

        sequences.append(current_sequence)

    def __find_addition_sequences_bfs_reverse(self, sequences):

        q = Queue()

        q.enqueue(self.root)

        current_sequence = []

        while not q.empty():
        
            current = q.dequeue()

            current_sequence.append(current.value)

            if current.right is not None:
                q.enqueue(current.right)
            if current.left is not None:
                q.enqueue(current.left)

        sequences.append(current_sequence)


    def __find_addition_sequences(self, node, current, current_sequence):

        if node is None:
            return 

        current_sequence.append(node.value)

        self.__find_addition_sequences(node.left, current,  current_sequence)
        self.__find_addition_sequences(node.right, current, current_sequence)

        if node.left is None and node.right is None:
            current.append(current_sequence)


    def __find_addition_sequences_inverse(self, node, current, current_sequence):

        if node is None:
            return

        current_sequence.append(node.value)

        self.__find_addition_sequences(node.right, current, current_sequence)
        self.__find_addition_sequences(node.left, current, current_sequence)

        if node.left is None and node.right is None:
            current.append(current_sequence)


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



class TreeTester:

    @staticmethod
    def test_creation(tree, TreeClass, sequences):

        for sequence in sequences:

            current_tree = TreeClass()
            [current_tree.add(x) for x in sequence]

            if not TreeTester.compare_trees(tree, current_tree):
                return False 

        return True


    @staticmethod
    def compare_trees(left, right):
        return TreeTester.__DFS_compare(left.root, right.root)


    @staticmethod
    def __DFS_compare(left_current, right_current):

        if left_current is None and right_current is None:
            return True

        if left_current is None:
            return False
        
        if right_current is None:
            return False

        res = left_current.value == right_current.value

        return res and TreeTester.__DFS_compare(left_current.left, right_current.left) \
                   and TreeTester.__DFS_compare(left_current.right, right_current.right)


        

if __name__ == '__main__':
    args = sys.argv[1:]

    tree = Tree()

    tree.add(2)
    tree.add(1)
    tree.add(3)
    tree.add(-5)
    tree.add(6)

    tree.dump()

    tester = TreeTester()
    sequences = tree.find_addition_sequences()

    print(tester.test_creation(tree, Tree, sequences))

    print(sequences)
    
