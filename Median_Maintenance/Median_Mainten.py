# -*- coding: utf-8 -*-
"""
Created on Jul 27 2022

Implementation of the Median Maintenance algorithm using heaps data structure.
Algorithm maintains the running median via two heaps - it breaks up the input array 
into a MIN heap and a MAX heap.

@author: D. S.
"""

import heapq 

#%% Define Data Import

def import_array(filename: str):
    """ Imports an array of integers. """
    
    array = []
    
    with open(filename) as f:
        for line in f:
            array.append(int(line.strip('\n')))
    
    return array
            
#%% Define Algorithm
  
def MedianMaintenance(x: int, min_Heap, max_Heap):
    ''' 
    Returns the median of a stream of numbers using heaps data structure. 
    
    Note that heapq implements Min Heaps. To implement Max Heap, input is
    multiplied by -1.
    '''
          
    if (len(min_Heap) == 0):
        heapq.heappush(min_Heap, -x)
    else:
        m = -min_Heap[0]
        if x > m:
            heapq.heappush(max_Heap, x)
            if len(max_Heap) > len(min_Heap):
                y = heapq.heappop(max_Heap)
                heapq.heappush(min_Heap, -y)
        else:
            heapq.heappush(min_Heap, -x)
            if len(min_Heap) - len(max_Heap) > 1:
                y = -heapq.heappop(min_Heap)
                heapq.heappush(max_Heap, y)
    
    return -min_Heap[0]
 
#%% Define Main
            
def main(filename: str):
    
    A = import_array(filename)
         
    medians = []
    min_Heap = []
    max_Heap = []
    
    for x in A:
        median = MedianMaintenance(x, min_Heap, max_Heap)
        medians.append(median)

    print(f'Last 4 Digits of the Sum of Running Medians: { sum(medians) % 10000 }')
   
#%% Run Main

if __name__ == '__main__':
    main('MedianData.txt')
