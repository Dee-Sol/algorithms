# -*- coding: utf-8 -*-
"""
Created on Jul 22 2022

Helper module for implementation of Djikstra's Shortest-Path algorithm.

@author: D. S.
"""

#%% Read into Adjacency List

def import_graph(filename: str) -> dict:
    """ imports a graph and formats it into an adjacency list. """
    
    adjlist = {}
    
    lines = open(filename).read().splitlines()
    
    for line in lines:
        
        data = line.split()
        v = int(data[0])
        adjlist[v] = []
        
        for tpl in data[1:]:
            
            t, w = [int(i) for i in tpl.split(',')]          
            adjlist[v].append((t, w))

    return adjlist
