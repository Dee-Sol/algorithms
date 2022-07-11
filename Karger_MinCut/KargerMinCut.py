# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 2022

Implementation of the Min Cut algorithm by David Krager. 
The algorithm performs randomised contraction of edges until a multigraph of two vertices is produced.

@author: D. S.
"""

from copy import deepcopy # for cloning original input graph across trials
import random # for picking random vertices
import time
import numpy as np # for calculating performance stats
import utils # helper function for loading input graph

#%% Define Min Cut Algorithm

def contract_edge(adjacency_list: dict, node: int, tail_vertex: int, head_vertex: int) -> dict:
    """ Performs contraction of an edge by linking head vertex to tail vertex's edges across all adjacency list entries.
    
    Parameters
    ----------
    adjacency_list : dict
        GRAPH'S ADJACENCY LIST, WHERE key = VERTEX, value = LIST OF TAIL VERTICES HAVING AN EDGE WITH HEAD VERTEX.
    node : int
        TARGET VERTEX (NODE) KEY IN ADJACENCY LIST TO REPLACE CONTRACTED VERTEX WITH ADJACENT VERTEX VALUES.
    tail_vertex : int
        TAIL VERTEX TARGETED FOR CONTRACTION.
    head_vertex : int
        HEAD VERTEX WHICH THE TARGETED VERTEX IS BEING CONTRACTED INTO.

    Returns
    -------
        NOTHING. THIS IS AN IN-PLACE SUBROUTINE.
    """
     
    adjacency_list[node] = [head_vertex if n == tail_vertex else n for n in adjacency_list[node] if n != node]


def MinCut(adjacency_list: dict) -> dict:
    """ Minimum cut algorithm using an adjacency list.

    Parameters
    ----------
    adjacency_list : dict
         GRAPH'S ADJACENCY LIST, WHERE key = VERTEX, value = LIST OF TAIL VERTICES HAVING AN EDGE WITH HEAD VERTEX.

    Returns
    -------
    dict
        CONTRACTED MULTIGRAPH WITH ONLY TWO VERTICES.
    """

    while len(adjacency_list) > 2:
        # randomly select head vertex and corresponding tail vertex for contraction
        head_vertex = random.choice(list(adjacency_list))
        tail_vertex = random.choice(adjacency_list[head_vertex])

        # Contract edge into head vertex and remove edge from adjacency list
        edges_from_tail_vertex = [n for n in adjacency_list[tail_vertex] if n != head_vertex]
        adjacency_list[head_vertex] = [n for n in adjacency_list[head_vertex] if n != tail_vertex]
        adjacency_list[head_vertex] += edges_from_tail_vertex
        adjacency_list.pop(tail_vertex)

        # Perform contraction on target vertex with vertex in all adjacency list vertices that shared an edge with tail vertex
        for edge in list(set(edges_from_tail_vertex)):
            contract_edge(adjacency_list, edge, tail_vertex, head_vertex)

    return adjacency_list

#%% Define Main

def main(file_path: str, sims: int):
    
    input_graph = utils.load_graph(file_path)
        
    run_times = []
    results = []
    
    for i in range(sims):
        G = deepcopy(input_graph)
        start = time.time()
        results.append(MinCut(G))
        end = time.time()
        run_times.append(end - start)
    
    min_cuts = []
    
    for result in results:
        keys = list(result.keys())
        min_cuts.append(len(result[keys[0]]))   
     
    print('Min Cut: ' + str(min(min_cuts)))
    print('Number of trials before first occurence of Min Cut: ' + str(min_cuts.index(min(min_cuts))))
    print('~~~~~~~~~~~~~~~~~~~~~~~')
    print('Mean run time per iteration: ' + str(round(np.mean(run_times),6)))
    print('Min run time per iteration: ' + str(round(min(run_times), 6)))
    print('Max run time per iteration: ' + str(round(max(run_times), 6)))
    print('~~~~~~~~~~~~~~~~~~~~~~~')

#%% Run Main

if __name__ == '__main__':
    main('KargerMinCut.txt', 250)   
