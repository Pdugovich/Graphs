"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {} # This is our adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # add the edge to both
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: VERTEX NOT FOUND")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None
            # Might want to raise an exception here, but we don't


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue and enqueue a starting index
        qq = Queue()
        qq.enqueue([starting_vertex])
        # create a set of traversed vertices
        visited = set()
        # while queue is not empty
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a queue and enqueue a starting index
        ss = Stack()
        ss.push([starting_vertex])
        # create a set of traversed vertices
        visited = set()
        # while queue is not empty
        while ss.size() > 0:
            # dequeue/pop the first vertex
            path = ss.pop()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    ss.push(new_path)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # Check if the "starting_vertex" is in the visited list
        # Note what "Starts" will change with the recursion
        if starting_vertex not in visited:
            # add that node to the list of visited nodes
            visited.add(starting_vertex)
            # print the node
            print(starting_vertex)
            # Put each of the adjescent nodes through the 
            # function. It will ignore the ones that have been visted
            for adj in self.get_neighbors(starting_vertex):
                # Voila!
                self.dft_recursive(adj, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Copied the traversal, except I included a
        # if statement. If the last item in the path
        # is the destination, then return the path!
        # otherwise, continue on
        
        # create a queue and enqueue a starting index
        qq = Queue()
        qq.enqueue([starting_vertex])
        # create a set of traversed vertices
        visited = set()
        # while queue is not empty
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] == destination_vertex:
                return path
            else:
                # DO THE THING!!!
                #print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Copied the traversal, except I included a
        # if statement. If the last item in the path
        # is the destination, then return the path!
        # otherwise, continue on

        # create a queue and enqueue a starting index
        ss = Stack()
        ss.push([starting_vertex])
        # create a set of traversed vertices
        visited = set()
        # while queue is not empty
        while ss.size() > 0:
            # dequeue/pop the first vertex
            path = ss.pop()
            # if not visited
            if path[-1] == destination_vertex:
                return path
            else:
                # DO THE THING!!!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    ss.push(new_path)


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path = []):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Check if the "starting_vertex" is in the visited list
        # Note what "Starts" will change with the recursion
        if starting_vertex not in visited:
            # add that node to the list of visited nodes
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            if starting_vertex == destination_vertex:
                return path_copy
            
            for adj in self.get_neighbors(starting_vertex):
                # Voila!
                final_path = self.dfs_recursive(adj, destination_vertex, visited, path_copy)
                if final_path is not None:
                    return final_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
