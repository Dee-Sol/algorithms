# -*- coding: utf-8 -*-
"""
Created on Aug 29 2022

Utility functions for implementation of Knapsack algorithm.

@author: D. S.
"""

from threading import currentThread
from time import time

def import_data(filename: str):
    """ Imports sample data from a text file. """
    
    with open(filename) as f:
        lines = f.readlines()
    size, n = map(int, lines[0].split())
    print(f'Knapsack size: {size}')
    print(f'Number of items: {n}')
    items = []
    for line in lines[1:]:
        items.append(tuple(map(int, line.split())))

    assert len(items) == n, 'Length of items does not match metadata.'
    
    return items, size

def thread_timer(target):
   """ 
   A wrapper function that returns execution time for individual threads. 
   
   """ 
   def wrapper(*args, **kwargs):
       start = time()
       print('Thread Started.')
       try:
           return target(*args, **kwargs)
       finally:
           end = time()
           print('Thread Ended.')
           currentThread().duration = end - start
   return wrapper
