# -*- coding: utf-8 -*-
"""
Created on Aug 10 2022

Implementation of Prim's minimum spanning tree (MST) algorithm. The implementation 
computes the total cost of a MST for an undirected graph. An MST is a subset of 
all edges that includes every vertex, where the total cost of all the edges in 
the tree is minimized. 

The algorithm operates by building this tree one vertex at a time, from an 
arbitrary starting vertex, at each step adding the cheapest possible connection 
from the tree to another vertex.

The implementation uses the heap data structure, which is used to store unprocessed
vertices. 

@author: D. S.
"""

from heapq import heapify, heappop
import time

#%% Define MST Algorithm

class Edge(object):
    def __init__(self, u, v, c):
        self.u = u
        self.v = v
        self.c = c

    def __lt__(self, other):
        return self.c < other.c

    def __repr__(self):
        return f'({self.u})--{self.c}--({self.v})'

    def __hash__(self):
        return hash((self.u, self.v, self.c))

def import_edges(filename: str):
    with open(filename) as f:
        lines = f.readlines()
        n_vertices, n_edges = map(int, lines[0].split())
    
        edges = []
        for line in lines[1:]:
            head, tail, cost = map(int, line.split())
            edges.append(Edge(head, tail, cost))
    
    return edges, n_vertices
        

def Min_Span_Tree(edges, graph_size: int) -> int:
    """
    Implementation of Prim's minimum spanning tree (MST) algorithm. 
    Returns the total cost of a MST for an undirected graph.
    
    """
    X = {1}
    Tree = set()
    mst_cost = 0
    while len(X) != graph_size:
        remaining_edges = [e for e in edges if (e.u in X) ^ (e.v in X)]
        heapify(remaining_edges)
        e = heappop(remaining_edges)
        X.add(e.u)
        X.add(e.v)
        Tree.add(e)
        mst_cost += e.c
    
    return mst_cost

#%% Define Main

def main(filename: str):
    start = time.perf_counter()
    
    G, graph_size = import_edges(filename)
    
    result = Min_Span_Tree(G, graph_size)
    
    end = time.perf_counter()
    print(f'Cost of MST: {result} \nCalculation Time: {end-start:.3}')

#%% Run Main
if __name__ == '__main__':
    main('Sample_edges.txt')
