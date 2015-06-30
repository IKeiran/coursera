"""
Provided code for Application portion of Module 2
"""

# general imports
import urllib2
import random
import time
import math

#CodeSkulptor import
import simpleplot
import codeskulptor
codeskulptor.set_timeout(60)

# Desktop imports
#import matplotlib.pyplot as plt


############################################
# Provided code

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    
def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order
    


##########################################################
# Code for loading computer network graph

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

# my code below:

def random_order(ugraph):
    """
    Take an undirected graph 
    Return: list of nodes in random order
    """
    key_list = list()
    for key in ugraph.keys():
        key_list.append(key)
    random.shuffle(key_list)
    return key_list

def get_edge_count(ugraph):
    from user40_09XbeJbeI2_0 import cc_visited
    connection_list = cc_visited(ugraph)
    count = 0
    for item in connection_list:
        count += len(item)
    return count

def make_ugraph(num_nodes, num_edges):
    """
    Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete
    directed graph with the specified number of nodes.
    :param num_nodes:integer
    :return: dict()
    """
    result = dict()
    for key in range(num_nodes):
        result[key]=()
    added_edges = 0
    set_of_nodes = set()
    if num_nodes > 0:
        while added_edges < num_edges:
            edge = random.randrange(num_nodes)
            node = random.randrange(num_nodes)
            set_of_nodes = result.get(node)
            if (edge not in set_of_nodes) and (node != edge):
                added_edges += 1
                result[node] += (edge,)
                result[edge] += (node,)              
        for key in result:
            result[key] = set(result.get(key))            
    else:
        return result
    return result

example_cn = load_graph(NETWORK_URL)
print example_cn 
node_list_cn = random_order(example_cn)
print node_list_cn

node_count = len(node_list_cn)
num_edges = get_edge_count(example_cn)
print num_edges
er_graph = make_ugraph (node_count, num_edges)
print er_graph





