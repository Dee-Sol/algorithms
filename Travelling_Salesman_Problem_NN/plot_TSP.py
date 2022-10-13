# -*- coding: utf-8 -*-
"""
Created on Oct 12 2022

Visualisation function for the implementation of the Travelling Salesman Problem
algorithm.

@author: D. S.
"""

import matplotlib.pyplot as plt

def plotTSP(TSP_path: list, coordinates: dict) -> None:
    '''
    Plots path for the Travelling Salesman Problem.

    Parameters
    ----------
    TSP_path : list
        Solution to the TSP.
    coordinates : tuple
        Coordinates of cities, stored as 2D Eucleadean distances.

    '''

    # Transform the TSP path into a list of ordered coordinates

    x = []; y = []
    for i in TSP_path:
        x.append(coordinates[i][0])
        y.append(coordinates[i][1])

    plt.scatter(x, y, s=10, color='r')
    
    # Set a scale for the arrow heads
    a_scale = float(max(x))/float(100)

    # Draw the TSP path
    plt.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]), head_width = a_scale,
            color ='c', length_includes_head=True)
    
    for i in range(0, len(x)-1):
        plt.arrow(x[i], y[i], (x[i+1] - x[i]), (y[i+1] - y[i]), head_width = a_scale,
                color = 'c', length_includes_head = True)

    # Adjust axis
    plt.xlim(min(x)*-0.5, max(x)*1.1)
    plt.ylim(min(y)*-0.5, max(y)*1.1)
    plt.axis('off')
    
    plt.show()