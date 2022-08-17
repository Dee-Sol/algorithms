# -*- coding: utf-8 -*-
"""
Created on Aug 17 2022

Utility functions for implementation of greedy clustering algorithms.

@author: D. S.
"""

def import_graph(filename: str):
    """ 
    Imports a graph with edge costs. Returns an edge list and a size of the graph.
    
    """
    
    G = []
    with open(filename) as f:
        graph_size = int(f.readline())
        for line in f:
            edge = list(map(int,(line[:-1]).split()))
            G.append(edge)
    
    return G, graph_size

def import_graph_bits(filename: str):
    """ Imports large graphs with edge costs stored as Hamming distance. """
    
    with open(filename, "r") as f:
        lines = f.readlines()

    graph_size, n_bits = map(int, lines[0].split())
    print(f'{graph_size} vertices')
    print(f'{n_bits} bits per vertex')
    
    numbers = [int(''.join(line.split()), 2) for line in lines[1:]]
    nodes = {}
    for node, num in enumerate(numbers):
        if num not in nodes:
            nodes[num] = set()
        nodes[num].add(node)
    
    return nodes, graph_size, n_bits