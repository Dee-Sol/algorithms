# -*- coding: utf-8 -*-
"""
Created on Aug 29 2022

Implementation of the Knapsack algorithm which leverages off of the dynamic 
programming paradigm. 

The implementation was extended to apply the paradigm in two ways - either 
iteratively or recursively. While both perform equally well on smaller lists of 
items, the recursive approach scales up considerably better. 
Note that these computation time benefits come at the expense of larger stack 
size requirements as well as raising default recursion limits. 

@author: D. S.
"""

import numpy as np
import sys
import threading
import utils # helper utility functions

#%% Define Knapsack Algorithm

def knapsack(items, size, method: str):
    """
    Wrapper function for the Knapsack algorithm.
    Supports two computational methods: iterative or recursive.

    Parameters
    ----------
    items
        list of items, containing their value and weight.
    size : int
        Capacity of the Knapsack.
    method : str
        Computation method. OPTIONS: "iterative", "recursive".

    """
    n = len(items)
    
    if method == 'iterative':

        Arr = np.zeros((n, size))
        for i in range(1, n):
            v_i, w_i = items[i]
            for j in range(size):
                if w_i > j:
                    Arr[i][j] = Arr[i - 1, j]
                else:
                    Arr[i][j] = max(Arr[i - 1, j], Arr[i - 1, j - w_i] + v_i)
        
        result = Arr.max()    
        return result
    
    elif method == 'recursive':
        
        global A
        A = dict()
        
        # Make result a global variable to facilitate threading
        global result_recursion
        result_recursion = int()
        result_recursion = knapsack_recurs(n, size)
        
        return result_recursion
        
    else:
        raise ValueError('Method can be either "iterative" or "recursive".')

def knapsack_recurs(i: int, x):
    """ Recursive loop of the Knapsack Algorithm.
    
    Note that default maximum recursion depth and stack size may have to be 
    increased to accommodate larger input data.
    """

    if i == 0:
        return 0
    
    str_ix = str(i) + ":" + str(x)
    if str_ix in A:
        return A[str_ix]
    
    # Define Recursion
    v_i_prev, w_i_prev = items[i - 1]
    
    if w_i_prev > x:
        A[str_ix] = knapsack_recurs(i - 1, x)
    else:
        A[str_ix] = max(knapsack_recurs(i - 1, x),
                        v_i_prev + knapsack_recurs(i - 1, x - w_i_prev))
    return A[str_ix]

#%% Define Main

def main(filename: str, method: str):
    
    global items
    
    items, size = utils.import_data(filename)  
    
    if method == 'iterative':

        result = knapsack(items, size, method)
    
    elif method == 'recursive':

        threading.stack_size(32 * 1024 * 1024)  # 32MB stack
        sys.setrecursionlimit(2 ** 14)  # approx 16k recursions
        thread = threading.Thread(target=utils.thread_timer(knapsack), 
                                  args=(items, size, method))
        thread.start()
        thread.join()
        result = result_recursion
        print(f'Calculation Time ({method} method): {thread.duration:.5} sec')
    
    else:
        raise ValueError('Method can be either "iterative" or "recursive".')
        
    print(f'Max Value ({method} method): {result}')
    return result 

#%% Run Main

if __name__ == '__main__':
    result_small = main('knapsack_sample_small.txt', method = 'iterative')

    result_big = main('knapsack_sample_big.txt', method = 'recursive')
    
    assert result_small == 2493893
    assert result_big == 4243395
    
      