"""
Unit for Coursera Algoritmic Thinking Module 1, Graph
"""

EX_GRAPH0 = {
    0: set([1,2]),
    1: set([]),
    2: set([])
}

EX_GRAPH1 = {
    0: set([1,4,5]),
    1: set([2,6]),
    2: set([3]),
    3: set([0]),
    4: set([1]),
    5: set([2]),
    6: set([])
}

EX_GRAPH2 = {
    0: set([1,4,5]),
    1: set([2,6]),
    2: set([3,7]),
    3: set([7]),
    4: set([1]),
    5: set([2]),
    6: set([]),
    7: set([3]),
    8: set([1,2]),
    9: set([0,3,4,5,6,7])
}


def compute_in_degrees(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the in-degrees for the nodes in the graph.
    The function should return a dictionary with the same set of keys (nodes) as digraph whose corresponding values
    are the number of edges whose head matches a particular node.
    :param digraph:
    :return: dict()
    """
    result = dict()
    for key in digraph.keys():
        result[key] = result.get(key,0)
        nodes = digraph.get(key)
        if len(nodes) > 0:
            for node in nodes:
                result[node] = result.get(node, 0) + 1
    return result


def in_degree_distribution(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the unnormalized distribution of
    the in-degrees of the graph. The function should return a dictionary whose keys correspond to in-degrees of nodes
    in the graph. The value associated with each particular in-degree is the number of nodes with that in-degree.
    In-degrees with no corresponding nodes in the graph are not included in the dictionary.
    :param digraph:
    :return: dict()
    """
    tmp_dict = compute_in_degrees(digraph)
    result = dict()
    for key in tmp_dict.keys():
        result[tmp_dict[key]] = result.get(tmp_dict[key], 0) + 1
    return result


def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete
    directed graph with the specified number of nodes.
    :param num_nodes:integer
    :return: dict()
    """
    result = dict()
    if num_nodes > 0:
        for node in range(num_nodes):
            set_of_nodes = set()
            for edge in range(num_nodes):
                if node != edge:
                    set_of_nodes.add(edge)
            result[node] = set_of_nodes
    else:
        return result
    return result