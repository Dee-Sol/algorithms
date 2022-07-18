# -*- coding: utf-8 -*-
"""
Created on Jul 15 2022

Helper module for Kosaraju algorithm implementation.

@author: D. S.
"""

def import_graph(filename: str):
    """ 
    Imports a directed graph from a file and performs additional transformations. 
    Converts the graph from a list of head and tail vertices into an adjacency list.
    
    Returns necessary inputs for Kosaraju algorithm: original graph, 
    transposed graph, and total number of vertices.
    """
    
    adjlist = []
    adjlist_reversed = []
    
    with open(filename) as f:
        for line in f:
            head_v, tail_v = [int(i) for i in line.split()]
            max_v = max(head_v, tail_v)
            
            while len(adjlist) < max_v:
                adjlist.append([])
            while len(adjlist_reversed) < max_v:
                adjlist_reversed.append([])
                
            adjlist[head_v -1].append(tail_v -1)
            adjlist_reversed[tail_v -1].append(head_v -1)
    
    return adjlist, adjlist_reversed, max_v
