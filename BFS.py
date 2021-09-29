class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)


def bfs_search(root_node, search_value):
    node_list = []
    explored = {}
    frontier = {}
    edge = 0
    to_be_checked_node = root_node
    print('here', root_node.value)
    graph_result = Graph(node_list)
    #print (graph_result.nodes, "check")
    if root_node.value == search_value:
        node_list = [root_node]
        graph_result = Graph(node_list)
        return graph_result
    else:
        while True:
            explored[to_be_checked_node] = edge
            children = to_be_checked_node.children
            edge += 1
            for child in children:
                if child not in list(frontier.keys()) and child not in list(explored.keys()):
                    frontier[child] = edge
                    for key in frontier.keys():
                        first_child = key
                        break


            if first_child.value == search_value:
                print('bingo')
                keys_list = list(explored)
                graph_result.nodes+=(keys_list)
                for i, key in enumerate(keys_list):
                    if i != (len(keys_list) - 1):
                        graph_result.add_edge(key, keys_list[i + 1])
                temp = list(explored)
                return graph_result
            else:
                #print(first_child, 'first child')
                #print ( frontier.get(first_child), "original first child")
                frontier.pop(first_child)
                #del frontier[first_child]
                to_be_checked_node = first_child








if __name__ == "__main__":
    nodeG = GraphNode('G')
    nodeR = GraphNode('R')
    nodeA = GraphNode('A')
    nodeP = GraphNode('P')
    nodeH = GraphNode('H')
    nodeS = GraphNode('S')
    graph1 = Graph([nodeS, nodeH, nodeG, nodeP, nodeR, nodeA])
    graph1.add_edge(nodeG, nodeR)
    graph1.add_edge(nodeA, nodeR)
    graph1.add_edge(nodeA, nodeG)
    graph1.add_edge(nodeR, nodeP)
    graph1.add_edge(nodeH, nodeG)
    graph1.add_edge(nodeH, nodeP)
    graph1.add_edge(nodeS, nodeR)
    #Graph_Result= bfs_search(nodeS, 'A')
    graph_result2 = bfs_search(nodeP, 'S')
    #print (Graph_Result.nodes[1].value)











