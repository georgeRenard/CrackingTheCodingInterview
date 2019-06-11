import sys


def problem():
    """
    Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
    projects, where the second project is dependent on the first project). All of a project's dependencies
    must be built before the project is. Find a build order that will allow the projects to be built. If there
    is no valid build order, return an error.
    EXAMPLE
    Input:
        projects: a, b, c, d, e, f
        dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
    Output: f, e, a, b, d, c
    """
    pass




class Graph:


    def __init__(self):

        self.vertices = {} 
        self.edges = {}

    
    def add_edge(self, proj, dependency):

        if proj is None or dependency is None:
            raise Exception("You cannot add a None value as a vertex")

        if proj not in self.vertices:
            self.vertices[proj] = [0, 0]

        if dependency not in self.vertices:
            self.vertices[dependency] = [0, 0]


        self.vertices[proj][1] += 1
        self.vertices[dependency][0] += 1
        
        if proj not in self.edges:
            self.edges[proj] = set()

        self.edges[proj].add(dependency)


    def add_vertex(self, vertex):

        if vertex is None:
            raise Exception("You cannot add a vertex with value of None")

        if vertex in self.vertices:
            raise Exception("You cannot add duplicate vertices")

        self.vertices[vertex] = (0, 0)


    def build_projects(self):

        visited = {x: False for x in vertices.keys()}
        
        output_buffer = []

        self.__build_projects(start, visited, output_buffer)

        return output_buffer



    def __build_projects(self, vertex, visited, output_buffer):

        if visited[vertex]
        

        for vert in self.edges[vertex]:
            self.__build_projects(vert, visited, output_buffer)

    

    def __repr__(self):
        return self.vertices.__repr__()
            


if __name__ == '__main__':
    args = sys.argv[1:]
    g = Graph()
    g.add_vertex("e")
    g.add_edge("a", "d")
    g.add_edge("f", "b")
    g.add_edge("b", "d")
    g.add_edge("f", "a")
    g.add_edge("d", "c")
    print(g)
