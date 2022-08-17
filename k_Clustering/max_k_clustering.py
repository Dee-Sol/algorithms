# -*- coding: utf-8 -*-
"""
Created on Aug 17 2022

Variant of a clustering algorithm, which computes maximum number of clusters
given a desired minimum spacing between vertices (implementation uses minimum
distance of 3 units by default). In other words, all pairs of vertices with 
spacing of 2 or less fall within the same clusters.

Implementation supports very large graphs via usage of Hamming distances (and 
subsequently bit-masks/bit-shifts) and the Union-Find data structure.
These enhancements come at the expense of deviation from Kruskal's Minimum 
Spanning Tree algorithm. 

@author: D. S.
"""

from networkx.utils import UnionFind
from itertools import combinations
import utils # helper function for importing graphs
import time

#%% Define Algorithm

def max_k_clusters_for_min_spacing(nodes: dict, 
                                   graph_size: int, 
                                   n_bits: int) -> int:
    
    # Create Union-Find object
    uf = UnionFind(range(graph_size))
    
    # Create bit-masks for Hamming distance of 1 using bit-shifts
    # (i.e. by shifting the 1-bit iteratively by 24 positions. This will result
    # in 24 bit-masks with the 1-bit at different positions, corresponding to 24 integers (powers of 2).
    distances = [1 << i for i in range(n_bits)]
    # Create a bit-mask with two 1-bits at distinct positions (=a bit-mask for Hamming distance of 2)
    # Use ^ for XOR (Exclusive OR) operator
    distances += [(1 << ix_1) ^ (1 << ix_2) for (ix_1, ix_2) in combinations(range(n_bits), 2)]
    # Add value 0 (i.e. a bit-mask for Hamming distance of 0)
    distances.append(0)
    
    # Iterate over the keys of the map (=the node values, key1) and XOR each 
    # key with the distance. If the resulting number is also a key in the map (key2), 
    # union all nodes from map[key1] and map[key2] using the union()-function.
    for distance in distances:
        for number in nodes.keys():
            if (number ^ distance) in nodes:
                for node_from in nodes[number]:
                    for node_to in nodes[number ^ distance]:
                        uf.union(node_from, node_to)
    
    # Count the number of clusters.
    n_clusters = len(list(uf.to_sets()))
    
    return n_clusters

#%% Define Main

def main(filename: str):
    
    start = time.perf_counter()
    
    nodes, n_nodes, n_bits = utils.import_graph_bits(filename)

    result = max_k_clusters_for_min_spacing(nodes, n_nodes, n_bits)
    
    end = time.perf_counter()
    print(f'Maximum Clusters Possible: {result}')
    
    print(f'Elapsed time: {end - start:.3} sec')
    assert result == 6118

#%% Run Main

if __name__ == "__main__":
    main('data_clustering_big.txt')
