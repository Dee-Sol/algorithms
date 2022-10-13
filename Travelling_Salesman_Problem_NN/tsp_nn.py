# -*- coding: utf-8 -*-
"""
Created on Oct 11 2022

Implementation of the "Nearest Neighbor" heuristic to solve the Travelling
Salesman Problem. The algorithm is extended to support multiple iterations,
each with randomly-selected starting point. It also includes a visualization
function for the shortest path.

Even with multiple passes, the heuristic results in a suboptimal solution. 
Nonetheless, the algorithm leads to a fairly good approximation, especially 
given how fast it is.

@author: D. S.
"""

import math
import random 
from os import path
from time import perf_counter
import plot_TSP as plt

#%% Define Algorithm

def read_data(filename: str):
    """ Read the cities data from a txt file. """
    
    if '\\' in filename:
        script_dir = path.dirname(__file__)
        filename = path.join(script_dir, filename)
    
    cities = {}
    with open(filename) as f:
        lines = f.readlines()
        n = int(lines[0])
        for line in lines[1:]:
            cities[int(line.split()[0])] = [float(line.split()[1]), float(line.split()[2])]
    
    print(f'Total number of cities: {n}')
    
    return cities, n


def distance(cities, i, j):
    """ 
    Compute the distance between cities i and j from their 2D Eucleadian distances.
    
    """
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)


def tsp_nn(cities, n: int, iterations = 1):
    """ 
    Compute the shortest distance for the TSP using the Nearest Neighbor 
    heuristic.
    
    The algorithm is extended to support multiple iterations, each with 
    randomly-selected starting point.
    
    """
        
    visited = [[random.randint(1, n)] for i in range(iterations)]
    dist = [int() for i in range(iterations)]
    
    for i in range(iterations):
                
        dst = 0
        while len(visited[i]) < n:
            unvisited = set(range(1, n + 1)) - set(visited[i])
            min_dst, j = min([(distance(cities, visited[i][-1], j), j) for j in unvisited])
            dst += min_dst
            visited[i].append(j)
        
        dist[i] = int(dst + distance(cities, visited[i][-1], 1))
    
    path_shortest = visited[min(range(len(dist)), key=dist.__getitem__)]
    dist_shortest = min(dist)
    
    return dist_shortest, path_shortest


#%% Define Main

def main(filename: str, passes: int):
    
    start_time = perf_counter()
    cities, n = read_data(filename)
    distance, path_TSP = tsp_nn(cities, n, passes)
    print(f'Total Distance: {distance}')
    print(f'Calculation Time for {passes} Iterations: {perf_counter() - start_time: .5} sec')
    plt.plotTSP(path_TSP, cities)
    
    return distance, path_TSP

#%% Run Main

if __name__ == '__main__':
    result_test, result_path = main('Datasets\\tsp_nn_101.txt', 25)
    assert result_test == 743
    
    #result = main('Datasets\\tsp_nn_large.txt', 1)
    #assert result == 1203406
    
    # test cases
    #result_test, result_path = main('Datasets\\tsp_nn_8k.txt', 10)
    #assert result_test == 623487 # 622937 for 10 iterations
        
    #result_test, result_path = main('Datasets\\tsp_nn_51.txt', 25)
    