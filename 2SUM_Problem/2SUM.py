# -*- coding: utf-8 -*-
"""
Created on Aug 2 2022

Implementation of a variant of the 2-SUM algorithm. Computes the number of 
target values t in the interval (default setting is [-10000,10000]) (inclusive) 
such that there are distinct numbers x,y in the input array that satisfy x+y=t. 

Implementation uses a hash table to speed up the search sub-routine.

@author: D. S.
"""

import time

#%% Define Import Array

def import_array(filename: str):
    """ Imports an array of integers as a list and a hash table. """

    hash_table = {}
    array = []
   
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n')
            v = int(line)
            hash_table[v] = False
            array.append(v)

    return array, hash_table

#%% Define 2-Sum Algorithm

def two_sum_loop(array: list, 
                 hash_table: dict, 
                 minimum = -10000, 
                 maximum = 10000) -> int:
    """ 
    Calculates number of target values t in the interval [minimum,maximum] (inclusive) 
    such that there are distinct numbers x,y in the input array that satisfy x+y=t.
    
    """

    array.sort()
    start = 0
    end = len(array) - 1
    found = hash_table
    
    # Define interval 
    if minimum < maximum:
        min = minimum
        max = maximum
    else:
        raise ValueError()
        
    # Set one pointer at the beginning of the sorted array and another at the end.
    while start < end:
        sum = array[start] + array[end]
        if sum < min:
            # advance start pointer closer to center of array
            start += 1
        elif sum > max:
            # advance end pointer closer to center of array
            end -= 1
        else:
            if array[start] != array[end]:
                found[sum] = True
            current_start = start
            current_end = end
			
            # Define termination conditions
            while True:
                start += 1
                sum = array[start] + array[end]
                if sum < min:
                    break
                elif sum > max:
                    break
                else:
                    if array[start] != array[end]:
                        found[sum] = True

            start = current_start

            while True:
                end -= 1
                sum = array[start] + array[end]
                if sum < min:
                    break
                elif sum > max:
                    break
                else:
                    if array[start] != array[end]:
                        found[sum] = True

            end = current_end
            start += 1
            end -= 1
			
    count = 0
    for element in found:
        if found[element]:
            count += 1

    return count

#%% Define Main

def main(filename: str, minimum: int, maximum: int):
    
    start = time.perf_counter()
    array, hash_table = import_array(filename)
    
    # Remove duplicates in the array
    # For dict is not necessary, as they don't contain duplicates
    array = list(set(array))
   
    result = two_sum_loop(array, hash_table, minimum, maximum)    

    end = time.perf_counter()
    
    print(f'Result: {result} \nCalculation Time: {end-start:.4} sec')

#%% Run Main    
if __name__ == '__main__':

	main('2sum_data.txt', -10000, 10000)
