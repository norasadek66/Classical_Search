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
    explored = []
    index=0
    frontier = []
    edge = 0
    to_be_checked_node = root_node
    #print('here', root_node.value)
    graph_result = Graph(node_list)
    #print (graph_result.nodes, "check")
    if root_node.value == search_value:
        node_list = [root_node]
        graph_result = Graph(node_list)
        return graph_result
    else:
        #graph_result.nodes=[root_node]
        #print graph_result.nodes[0].value, "first element"
        while True:
            if to_be_checked_node not in explored:
                explored.append(to_be_checked_node)
                #print to_be_checked_node.value, "following element"
                children = to_be_checked_node.children
                for child in children:
                    if child not in (frontier) and child not in (explored):
                        #print"child ", child.value
                        frontier.append(child)

                for key in frontier:
                    #print 'firsttt ', key.value
                    first_child = key
                    break
                if first_child.value == search_value:
                    #print "bingo", explored[1].value
                    explored.append(first_child)
                    keys_list = []
                    for key in explored:
                        #print key.value, "key values here"
                        keys_list.append(key)
                    #print len(keys_list), "length"
                    for i, key in enumerate(keys_list):
                        if i != (len(keys_list) - 1):
                            #print "following key ", key.value
                            graph_result.nodes.append(key)
                            for val in graph_result.nodes:
                                if val.value!=key.value:
                                    if key in val.children:

                                        #print key.value, val.value, "new edge"
                                        graph_result.add_edge(val,key)



                            #graph_result.add_edge(key, keys_list[i + 1])
                        else:
                            graph_result.nodes.append(key)
                            for val in graph_result.nodes:
                                if val.value != key.value:
                                    if key in val.children:
                                        #print key.value, val.value, "new edge"
                                        graph_result.add_edge(val, key)
                                        break
                    #temp = list(explored)


                    return graph_result
                else:

                    frontier.pop(0)
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
    Graph_Result= bfs_search(nodeS, 'A')
    #graph_result2 = bfs_search(nodeP, 'S')
    #print (graph_result2.nodes[1].value)
    for i in range(len(Graph_Result.nodes)):
        print Graph_Result .nodes[i].value











