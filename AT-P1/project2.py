""" Unit for Homework2 Algiritnic thinking"""

import alg_module2_graphs

def bfs_visited(ugraph, start_node):
    """
    Takes the undirected graph ugraph and the node start_node 
    and returns the set consisting of all nodes that are 
    visited by a breadth-first search that starts 
    at start_node
    """
    queue = []
    chain = [start_node]
    visited = start_node
    queue.append(visited)
    while len(queue)>0:
        index = queue[0]
        queue.remove(index)
        for item in ugraph[index]:
            if item not in chain:
                chain.append(item,)
                queue.append(item)
    return set(chain)
   
def cc_visited(ugraph):
    """
    akes the undirected graph ugraph and returns 
    a list of sets, where each set consists of 
    all the nodes (and nothing else) 
    in a connected component, 
    and there is exactly one set in the 
    list for each connected component in ugraph 
    and nothing else.
    """
    remining_nodes = []
    for key in ugraph.keys():
        remining_nodes.append(key)
    con_components = []
    while len(remining_nodes) >0:
        node = remining_nodes[0]
        result = bfs_visited(ugraph, node)
        for item in result:
            remining_nodes.remove(item)
        con_components.append(result,)
    return (con_components)
    
    
def largest_cc_size(ugraph):
    """
    Takes the undirected graph ugraph and returns 
    the size (an integer) of the largest connected component in ugraph
    """   
    connected_list = cc_visited(ugraph)
    result = list()
    for item in connected_list:
        result.append(len(item))
    if len(result)>0:
        return max(result) 
    else:
        return 0
    
def compute_resilience(ugraph, attack_order):
    """
    Takes the undirected graph ugraph, a list of nodes attack_order 
    and iterates through the nodes in attack_order. For each node 
    in the list, the function removes the given node and its edges 
    from the graph and then computes the size of the 
    largest connected component for the resulting graph
    """
    result = []
    print 'ugraph', ugraph
    result.append(largest_cc_size(ugraph))
    for node in attack_order:
        print 'node', node
        if node in ugraph:
            ugraph.pop(node)
            for item in ugraph:
                print 'item, ', item
                if node in ugraph[item]:
                    tmp = ugraph[item]
                    print tmp, node
                    tmp.remove(node)
                    ugraph[item] = tmp
            result.append(largest_cc_size(ugraph),)        
            print ugraph         
    return result
    
print compute_resilience(alg_module2_graphs.GRAPH5, [1, 2])