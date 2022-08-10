# -*- coding: utf-8 -*-
"""
Created on Aug 10 2022

Helper functions for implementation of a scheduling algorithm.

@author: D. S.
"""

def import_tasks(filename: str):
    """ Imports a set of tasks from a txt file. """

    weights = []
    lengths = []
    
    with open(filename) as f:
        for line in f:
            line = line.strip('\n').split(' ')
            if len(line) == 2:
                weights.append(int(line[0]))
                lengths.append(int(line[1]))
            
    return weights, lengths