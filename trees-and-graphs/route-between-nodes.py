import sys




def problem():
    """
    Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
    route between two nodes.
    """
    pass



def considerations():
    """
    For now I will try not to use any hashing of the nodes since we don't know whether we will get only unique
    values or if we are allowed to generate unique Id's for each graph node.
    """
    pass


class Graph:


    def __init__(self):
        self.vertices = [] 
        self.count = 0

    
    # Add edge adds an edge from a to b and creates the a/b nodes if the don't exist
    def addedge(self, a, b):

        a_node = None
        b_node = None

        for v in self.vertices:
            if v.value == a:
                a_node = v

            if v.value == b:
                b_node = v


        if a_node is None:
            a_node = self.GraphNode(a)
            self.vertices.append(a_node)
            self.count += 1

        if b_node is None:
            b_node = self.GraphNode(b)
            self.vertices.append(b_node)
            self.count += 1

        a_node.children.append(b_node)


    def path_exists(self, src, dest):

        src_node = None

        for v in self.vertices:
            if v.value == src:
                src_node = v

        res = self.__path_exists(src_node, dest)
        
        for v in self.vertices:
            v.visited = False

        return res


    def __path_exists(self, current, dest):

        if current.visited:
            return False

        current.visited = True

        if current.value == dest:
            return True

        res = False

        for child in current.children:
            res = res or self.__path_exists(child, dest)

        return res


    class GraphNode:

        def __init__(self, value):
            self.visited = False
            self.value = value
            self.children = [] 


    class GraphIterator:
        
        def __init__(self):
            pass

        def __next__(self):
            pass



if __name__ == '__main__':
    args = sys.argv[1:]

    g = Graph()
    g.addedge(0, 1)
    g.addedge(0, 4)
    g.addedge(0, 5)
    g.addedge(1, 4)
    g.addedge(1, 3)
    g.addedge(2, 1)
    g.addedge(3, 2)
    g.addedge(3, 4)

    print(g.path_exists(1, 2))

