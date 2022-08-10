# -*- coding: utf-8 -*-
"""
Created on Aug 10 2022

Implementation of a Greedy algorithm for scheduling tasks with varying priorities
and duration. It minimizes weighted sum of completion times.
Implementation allows for choice of the minimization method: either on the basis 
of the difference (priority - duration) or ratio (priority/duration).

@author: D. S.
"""

import utils # Helper function to import tasks

#%% Define Scheduling Algorithm

def schedule_tasks(weights: list, lengths: list, method: str) -> list:
    """
    Runs a greedy algorithm to schedule tasks based on minimisation of weighted
    sum of completion times. Offers two minimisation functions (chosen via 'method' argument):
        1) 'Ratio' (priority/duration)
        2) 'Difference' (priority - duration).

    """

    schedule = []
    no_of_tasks = len(weights)
    
    if method == "Ratio":
        for i in range(no_of_tasks):
            schedule.append([weights[i], lengths[i], float(weights[i])/float(lengths[i])])
        schedule.sort(key = lambda x: x[2])
        schedule = schedule[:: -1]
            
    elif method == "Difference":
        for i in range(no_of_tasks):
            schedule.append([weights[i], lengths[i], float(weights[i]) - float(lengths[i])])
        # sort by score AND priority to settle ties
        schedule.sort(key = lambda x: (x[2],x[1]))
        schedule = schedule[:: -1]

    else:
        raise ValueError("Method Misspecified - has to be either Ratio or Difference")
        
    return schedule

def weighted_completion_times(schedule: list) -> int:
    """    Computes total weighted completion time from a schedule of tasks.    """
	
    comp_time = 0
    weighted_comp_time = 0
    for task in schedule:
        comp_time += task[1]
        weighted_comp_time += comp_time*task[0]

    return weighted_comp_time

#%% Define Main

def main(filename: str, method: str):
    
    w, l = utils.import_tasks(filename)
    schedule = schedule_tasks(w, l, method)

    total_time = weighted_completion_times(schedule)
    
    print(f'{method}: {total_time}')

#%% Run Main

if __name__ == '__main__':
    main('Sample_jobs.txt', 'Difference')
    main('Sample_jobs.txt', 'Ratio')
 