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
    # Declare and initialize result, unvisited, and path

    # As long as unvisited is non-empty
    while unvisited:

    # 1. Find the unvisited node having smallest known distance from the source node.

    # 2. For the current node, find all the unvisited neighbours. For this, you have calculate the distance of each unvisited neighbour.

    # 3. If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary, update the shortest distance in the result dictionary.

    # 4. If there is an update in the result dictionary, you need to update the path dictionary as well for the same key.

    # 5. Remove the current node from the unvisited set.

    return result