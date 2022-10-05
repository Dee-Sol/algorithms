# -*- coding: utf-8 -*-
"""
Created on Oct 4 2022

Implementation of the dynamic programming algorithm for the Travelling Salesman 
problem. Utilises bit-wise operations (Gosper's Hack) for faster iterations.
The algorithm can take input graphs in form of either Eucledian distances or 
as matrices of edge costs. 

@author: D. S.
"""

import time
import math
import utils

#%% Define Gospers Hack Class
# http://programmingforinsomniacs.blogspot.com/2018/03/gospers-hack-explained.html

class Gospers_Hack:
    def __init__(self, m, n ):  
    	self.m = m 
    	self.first = pow(2, m ) - 1
    	self.last = pow(2, n ) - pow(2, n-m )
        
    def __iter__(self):
    	self.x = self.first
    	return self
    
    def __next__(self):
    	xr = self.x
    	if (xr > self.last ):
        	raise StopIteration
    	x = self.x
    	s = x & (-x) 
    	r = s + x 
    	x = r | (((x ^ r) >> 2) // s) 
    	self.x = x
    	return xr


#%% Define Algorithm

def tsp_dynamic(C: list, n: int) -> float:
    ''' 
    Implementation of the dynamic programming algorithm for the Travelling
    Salesman problem.
    Utilises bit-wise operations (Gosper's Hack) for faster iterations.

    Parameters
    ----------
    C : list
        Two-dimensional array containing edge costs, 
        where C[i][j]=distance from Vi to Vj.
    n : int
        Number of vertices in the input graph.

    '''
        
    # Additional Notes:
    # Integer S represents a subset of vertices set V, so that the 
    # number of elements of the set S_ formed by the subset S is 2^(n-1)
    
    # B is the new (S,i) dictionary of the shortest path calculated by this loop. 
    # Here the length of S is m.  
    
    B = [ [0.0 for j in range(n)] for i in range(pow(2,n-1)) ]
    
    minV = math.inf
    
    # The first layer traverses the length of the subset, from 2 to n
    for m in range(2,n+1):
        
        # The second layer traverses all subsets of length m.
        print( 'm:',m)
        for S in Gospers_Hack(m-1,n-1):
            
            # The third layer traverses all the endpoints in the S set.
            for i in range(1,n):
    	        if S&(1<<(i-1)) != 0 :

    	            if m > 2:
    	                minV = math.inf
    	                for k in range(1,n):
    	        	        if S&(1<<(k-1)) != 0 and k != i: 
    	        	            S_ = S ^ (1<<(i-1))
    	        	            minV =  min( minV, B[S_][k]+C[k][i] )
    	        else :
    	            minV = C[0][i]
    	        
    	        B[S][i] = minV

    results = []
    S = pow(2,n-1) - 1
    
    for vertex in range(1,n):
        results.append(min(math.inf, B[S][vertex] + C[vertex][0]))
    
    shortest_dist = float(min(results))
    
    return shortest_dist

#%% Define Main

def main(filename: str):
    start_time = time.perf_counter()
    
    print('Import data...')
    G, size = utils.import_graph(filename)
    
    print('Compute edge costs...')
    C = utils.calc_edge_costs(G, size)
    
    print('Initiate algorithm...')
    shortest_dist = tsp_dynamic(C, size)

    print(f'Minimum cost of trip: {shortest_dist: .3}')
    print(f'Calculation time: {time.perf_counter() - start_time: .4} sec')
    
    return shortest_dist

    
#%% Run Main

if __name__ == '__main__':
#    result = main('Test Cases\tsp_data.txt') # 26442.73031
#    assert result == 26442.73031
    
    test_case1 = main('Test Cases\\tsp_test1.txt') # 12.36
    assert round(test_case1, 2) == 12.36
    
    test_case2 = main('Test Cases\\tsp_test2.txt') # 4.00
    assert test_case2 == 4.00
    
    test_case3 = main('Test Cases\\tsp_test3.txt') # 4.41
    assert round(test_case3, 2) == 4.41
