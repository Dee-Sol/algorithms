# -*- coding: utf-8 -*-
"""
Created on Aug 22 2022

Use case of dynamic programming to compute maximum-weight independent set of 
a path graph. Independent set is defined as a set of non-adjacent vertices.

Implementation splits computation into two parts:
    1) Memoization algorithm, and 
    2) Reconstruction algorithm

@author: D. S.
"""

#%% Define Import Path

def import_path(filename: str) -> list:
    with open(filename) as f:
        lines = f.readlines()
        n_weights = int(lines[0])
        weights = [int(line) for line in lines[1:]]
    
    assert n_weights == len(weights), 'something went wrong'
    
    return weights

#%% Define Max Weight IS Algorithm

def max_weight_IS(path: list) -> set:
    ''' 
    Returns maximum-weight independent set for a path graph.
    Implementation uses dynamic programming approach and splits computation
    into two parts: 
    1) Memoization algorithm, and 2) Reconstruction algorithm.
    
    '''
    n_weights = len(path)
    
    # Memoization Algorithm:
    # Cache solutions to already solved subproblems   
    A = [0] * n_weights
    A[1] = path[0]
    for i in range(2, n_weights):
        A[i] = max(A[i - 1], A[i - 2] + path[i - 1])
    
    # Reconstruction Algorithm:
    # Array A contains all solutions for the sub-problems.
    # Use it to reconstruct the max-weight independent set.      
    
    i = len(A)
    IS = set()
    while i >= 1:
        if A[i - 1] >= A[i - 2] + path[i - 1]:
            i -= 1
        else:
            IS.add(path[i - 1])
            i -= 2
    return IS

def convert_diff_to_binary(path, ind_set: set, vertices_to_check: list) -> str:
    string = ''
    for i in vertices_to_check:
        if path[i - 1] in ind_set:
            string += '1'
            print(f'vertex {i} belongs to Set')
        else:
            string += '0'
            print(f'vertex {i} does not belong to Set')
    return string

#%% Define Main

def main(filename: str, vertices_to_check: list):
    weights = import_path(filename)
    IS = max_weight_IS(weights)
    result = convert_diff_to_binary(weights, IS, vertices_to_check)

    print(result)

#%% Run Main

if __name__ == '__main__':
    main('sample_data_mwis.txt', 
         [1, 2, 3, 4, 17, 117, 517, 997])
