# -*- coding: utf-8 -*-
"""
Created on Jul 22 2022

Implementation of Dijkstra's Shortest-Path algorithm using heaps data structure.

@author: D. S.
"""

import math # for inf method
import heapq # for heaps data structures
import utils # helper module for graph import


#%% Define Algorithm

def Dijkstra_SP(graph: dict, start = 1) -> dict:
    """ Dijkstra's Shortest-Path algorithm.
    
    Parameters
    ----------
    graph : dict
        Graph in the adjacency list format.
    start : int, optional
        Vertex of start. The default is 1.

    Returns
    -------
    A dict of shortest distances from the vertex of start to each vertex in the input graph.
    """
    distances = {}
    distances[start] = 0
    for vertex in graph:
        if vertex != start:
            distances[vertex] = math.inf
    to_check = [(start, 0)]
    while to_check:
        current_vertex, total = heapq.heappop(to_check)
        for neighbor, distance in graph[current_vertex]:
            new_total = total + distance
            if new_total < distances[neighbor]:
                distances[neighbor] = new_total
                heapq.heappush(to_check, (neighbor, new_total))
    return distances

#%% Define Main

def main(filename: str, destination: list, start_vertex = 1):
    G = utils.import_graph(filename)
    dist = Dijkstra_SP(G, start_vertex)
    
    print(f'~~~~~~~~~~~~~~~~~~~~~~~ \nShortest distance from vertex {start_vertex}:')
    
    for vertex in destination:
        print(f'To vertex {vertex}: {dist[vertex]}')

#%% Run Main

if __name__ == "__main__":

    destinations = [7,37,59,82,99,115,133,165,188,197]
    main('dijkstraData.txt', destinations)
