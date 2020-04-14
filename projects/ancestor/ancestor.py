
from graph import *
def earliest_ancestor(ancestors, starting_node):
    # Instantiating a graph to populate with the edges provided
    g = Graph()
    # Adding vertices for either number in the tuples provided
    for item in ancestors:
        g.add_vertex(item[0])
        g.add_vertex(item[1])
    # Adding edges, reversing the order so I can do a depth first search
    for item in ancestors:
        g.add_edge(item[1], item[0])

    final_paths = []
    ### THIS section copied from dft 
    # create a queue and enqueue a starting index
    ss = Stack()
    ss.push([starting_node])
    # create a set of traversed vertices
    visited = set()
    # while queue is not empty
    while ss.size() > 0:
        # dequeue/pop the first vertex
        path = ss.pop()
        # if not visited
        if path[-1] not in visited:
            # DO THE THING!!!
            ###
            # mark as visited
            visited.add(path[-1])
            # push all neighbors
            if g.get_neighbors(path[-1]) == set():
                final_paths.append(path)
            for next_vert in g.get_neighbors(path[-1]):
                new_path = list(path)
                new_path.append(next_vert)
                ss.push(new_path)
    print(final_paths)
    if len(final_paths[0]) == 1:
        return -1
    lengths = []
    oldest_ancestors = []
    for item in final_paths:
        lengths.append(len(item))
    for item in final_paths:
        if len(item) == max(lengths):
            oldest_ancestors.append(item[-1])
    return min(oldest_ancestors)
       