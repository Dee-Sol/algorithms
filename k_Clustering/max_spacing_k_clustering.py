# -*- coding: utf-8 -*-
"""
Created on Aug 17 2022

Implementation of a greedy clustering algorithm (variant of Kruskal's Minimum 
Spanning Tree algorithm). We greedily take the closest pair of separated points 
and fuse them into the same cluster, iteratively increasing the maximum spacing.

The implementation returns maximum spacing for a given number of clusters. 

@author: D. S.
"""

import utils # Helper function for importing graphs

#%% Define Greedy Clustering Algorithm

def cluster_max_spacing(graph: list, k: int, graph_size: int) -> int:
    """
    Computes maximum distance between a given number of clusters. 

    Parameters
    ----------
    graph : list
        GRAPH IN EDGE LIST FORMAT.
    k : int
        NUMBER OF CLUSTERS IN INPUT GRAPH.
    graph_size : int
        TOTAL NUMBER OF VERTICES IN INPUT GRAPH.

    """
    
    clusters = []
    for i in range(1, graph_size+1):
        clusters.append({i})
    while(len(clusters) != k):
        edge = graph.pop(0)
        first_flag = False
        second_flag = False
        for i in range(len(clusters)): 
            if edge[0] in clusters[i]:
                first_index = i
                first_flag = True
            if edge[1] in clusters[i]:
                second_index = i
                second_flag = True
            if first_flag and second_flag:
                break
        if first_index != second_index:
            if first_index < second_index:
                clusters.append(clusters.pop(first_index).union(clusters.pop(second_index-1)))
            else:
                clusters.append(clusters.pop(first_index).union(clusters.pop(second_index))) 
    
    same_cluster = True
    while(same_cluster):
        edge = graph.pop(0)
        for j in range(k):
            if edge[0] in clusters[j] and edge[1] not in clusters[j]:
                spacing = edge[2]
                same_cluster = False
            
    return spacing

#%% Define Main
            
def main(filename, clusters: int):
    G, graph_size = utils.import_graph(filename)
    G.sort(key = lambda x : x[2])
    result = cluster_max_spacing(G, clusters, graph_size)
    print(f'Maximum Spacing for {clusters} Clusters: {result}')

#%% Run Main    
if __name__ == '__main__':
    main('data_clustering_small.txt', 4)
