# -*- coding: utf-8 -*-
"""
Created on Jul 15 2022

Implementation of Kosaraju algorithm, which computes strongly connected components
of a directed graph. Implementation consists of two passes of the Depth-First Search
algorithm. First pass is performed on the transposed version of a graph, to calculate
DFS finishing times for each vertex. Second DFS pass uses the finishing times 
as order of execution to compute strongly connected components. 

While the original algorithm is recursive, this implementation is iterative.

@author: D. S.
"""

import time # For calculating basic performance stats
import utils # Helper function for importing graphs

#%% Define Algorithm (Iterative)

def DFS_first_pass(Grev: list, n: int) -> list:
    """ 
    Performs first pass of Depth-First Search algorithm, calculating 
    finishing times for each vector. 
    """
    
    explored = [False for i in range(n)]
    stack = []
    f = [0 for i in range(n)]
    t = 0
   
    for i in range(n-1, -1, -1):
   		if not explored[i]:
   			explored[i] = True
   			stack.append(i)
   
   		while stack:
   			done = True
   			v = stack[-1]
   			for w in Grev[v]:
   				if not explored[w]:
   					explored[w] = True
   					stack.append(w)
   					done = False
   					break
   			if done:
   				f[v] = t
   				t += 1
   				stack.pop()
    
    return f


def DFS_second_pass(G: list, start_node: int):
    """ 
    Computes a Depth-First Search path for a given vertex, while keeping 
    track of already visited vertices.  
    """
    
    stack = [start_node]
    global discovered
    discovered[start_node] = True

    dfs_path = []

    while len(stack) > 0:
        v = stack.pop(len(stack) - 1)
        dfs_path.append(v)
        if len(G[v]) != 0:
            for w in G[v]:
                if discovered[w] == False:
                    discovered[w] = True
                    stack.append(w)

    return dfs_path

def kosaraju_SCC(G: list, f: list):
    """ 
    Computes strongly connected components of a directed graph using 
    finishing times from a preliminary Depth-First Search pass on the reversed graph.    
    """
    
    n = len(f)

    temp_G = [[] for i in range(n)]
    new_G = temp_G.copy()

    for i in range(n):
        for j in range(len(G[i])):
            x = G[i][j]
            temp_G[i].append(f[x])
    
    for i in range(n):
        new_G[f[i]] = temp_G[i]

    global discovered
    discovered = [False for i in range(n)]

    all_scc = []
    
    for i in range(n-1, -1, -1):
        if not discovered[i]:
            all_scc.append(len(DFS_second_pass(new_G, i)))

    all_scc.sort(reverse = True)

    return all_scc


#%% Define Main

def main(filename: str):
    """ 
    Calculates five largest strongly connected components of a directed graph. 
    """
    
    start = time.perf_counter()
    G, G_rev, n = utils.import_graph(filename)
    f = DFS_first_pass(G_rev, n)

    scc = kosaraju_SCC(G, f)
    end = time.perf_counter()
    print('Sizes of five largest strongly connected components:', scc[:5], sep=('\n'))
    print('~~~~~~~~~~~~~~~~~~~~~~~')
    print("Total Runtime: " + str(round(end-start, 3)) + " seconds.")

#%% Run Main

if __name__ == '__main__':
    main('SCCgraph.txt')

