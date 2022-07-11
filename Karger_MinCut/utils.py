# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 2022

Helper functions for Karger's Min Cut algorithm

@author: D. S.
"""

def load_graph(file_path: str) -> dict:
    """ Loads graph in a form of an adjacency list.

    Parameters
    ----------
    file_path : str
        NAME OF THE FILE CONTAINING A GRAPH IN THE FORM OF AN ADJACENCY LIST.

    Returns
    -------
    dict
        GRAPH'S ADJACENCY LIST, WHERE key = VERTEX, value = LIST OF TAIL VERTECES HAVING AN EDGE WITH HEAD VERTEX.
    """
    
    input_graph = {}
    with open(file_path) as f:
        for line in f:
            line_values = [int(i) for i in line.split()]
            k = line_values[0]
            v = [i for i in line_values[1:] if i != k]
            v.sort()
            input_graph[k] = v
    
    return input_graph