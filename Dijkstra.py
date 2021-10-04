# Helper Code
from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()  # A set cannot contain duplicate nodes
        self.neighbours = defaultdict(
            list)  # Defaultdict is a child class of Dictionary that provides a default value for a key that does not exists.
        self.distances = {}  # Dictionary. An example record as ('A', 'B'): 6 shows the distance between 'A' to 'B' is 6 units

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neighbours[from_node].append(to_node)
        self.neighbours[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance  # lets make the graph undirected / bidirectional

    def print_graph(self):
        print("Set of Nodes are: ", self.nodes)
        print("Neighbours are: ", self.neighbours)
        print("Distances are: ", self.distances)





def dijkstra(graph, source):
    result={}
    result[source]=0
    unvisited=set()
    for node in graph.nodes:
        if node != source:
            unvisited.add(node)
    path={}
    # path contains most optimal previous node for every node in the graph
    min_distance = 0
    min_prev_node = ""
    i = 0
    for k,v in graph.distances.items():
        if k[0] == source:
            result[k[1]] = v


    # As long as unvisited is non-empty
    while unvisited:
        i = 0
        for k,v in result.items():
            if k != source and i == 0 and k in unvisited:
                min_distance = v
                min_prev_node = k
                i += 1
            elif k != source and i != 0 and k in unvisited:
                if v < min_distance:
                    min_distance = v
                    min_prev_node = k
                    path[min_prev_node] = source
                    result[min_prev_node] = min_distance
        neighbours_list = graph.neighbours[min_prev_node]
        distances_dict = graph.distances
        for neighbour in neighbours_list:
            if neighbour in unvisited:
                dist_for_neighbour = distances_dict[(min_prev_node, neighbour)] + min_distance
                if neighbour in result.keys():
                    if dist_for_neighbour < result[neighbour]:
                        result[neighbour] = dist_for_neighbour
                        path[neighbour] = min_prev_node
                else:
                    result[neighbour] = dist_for_neighbour
                    path[neighbour] = min_prev_node
        unvisited.remove(min_prev_node)
    return result
if __name__=="__main__":
    testGraph = Graph()
    for node in ['A', 'B', 'C', 'D', 'E']:
        testGraph.add_node(node)

    testGraph.add_edge('A', 'B', 3)
    testGraph.add_edge('A', 'D', 2)
    testGraph.add_edge('B', 'D', 4)
    testGraph.add_edge('B', 'E', 6)
    testGraph.add_edge('B', 'C', 1)
    testGraph.add_edge('C', 'E', 2)
    testGraph.add_edge('E', 'D', 1)

    print(dijkstra(testGraph, 'A'))  # {'A': 0, 'D': 2, 'B': 3, 'E': 3, 'C': 4}
    graph = Graph()
    for node in ['A', 'B', 'C']:
        graph.add_node(node)

    graph.add_edge('A', 'B', 5)
    graph.add_edge('B', 'C', 5)
    graph.add_edge('A', 'C', 10)

    print(dijkstra(graph, 'A'))