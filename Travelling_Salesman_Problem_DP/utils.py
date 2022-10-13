# -*- coding: utf-8 -*-
"""
Created on Oct 5 2022

Utility functions for implementation of a dynamic programming algorithm for 
the Travelling Salesman problem.

@author: D. S. 
"""

from os import path


def import_graph(filename: str):
    """ Imports sample data from a text file. """
    
    if '\\' in filename:
        script_dir = path.dirname(__file__)
        filename = path.join(script_dir, filename)

    with open(filename) as f:
        lines = f.readlines()
    
    n = int(lines[0])   
    print(f'Number of vertices: {n}')
    
    G = []    
    for line in lines[1:]:
        coordinate = [float(x) for x in line.split() ]
        G.append(tuple(coordinate))
    
    return G, n

def calc_edge_costs(Graph: list, size: int) -> list:
    """ Converts Eucledian distances to edge costs. It calculates distances 
    between all vertices (i.e. edge weights).
    
    Returns a two-dimensional array C, where C[i][j]=distance from Vi to Vj.
    
    """
    
    C = []
    
    C = [[0 for j in range(size)] for i in range(size) ]
    for i in range(size):
        for j in range(size):
            C[i][j] = pow(pow( Graph[i][0] - Graph[j][0], 2) + 
                          pow( Graph[i][1] - Graph[j][1], 2),
                          0.5)
    return C

