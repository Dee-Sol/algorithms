# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 2022

Implementation of QuickSort algorithm using three different methods of 
pivot element selection

@author: D. S.
"""
#%% Import Libraries

import math # used for math.floor
import statistics # used to calculate median.
import utils # helper function for main to check if list sorted.

#%% Define Cases for Pivot Selection Methods

class PivotCase:
    """ 
    Facilates choice of an approach to calculating the pivot element. 
    
    Attributes
    ----------
    A : list
        Unsorted list of numbers.
    left, right : int
        list indices, made available to facilitate recursive calls of the function.
    
    Methods
    ----------
    ChoosePivot(case = ""):
        Calculates index of pivot element based on chosen approach. 
        Options: 'First_Element', 'Last_Element', 'Median_Element'. 
    """
    def __init__(self, A: list, left: int, right: int):
        """ Initiates PivotCase class with necessary attributes. """
        self.A = A
        self.left = left
        self.right = right
    
    def ChoosePivot(self, case: str) -> int:
        """
        Returns index of pivot element, depending on chosen partitioning approach. 
        
        Parameters
        ----------
        case : str
            Options: 'First_Element', 'Last_Element', 'Median_Element'.
        """
        default = "Invalid Case"
        return getattr(self, case, lambda: default)()   
    
    def First_Element(self):
        return self.left
    
    def Last_Element(self):
        return self.right - 1
      
    def Median_Element(self):
        return self.median_pivot(self.A, self.left, self.right)
    
    def median_pivot(self, A, left, right):
        """
        'Median of Three' pivot heuristic takes the first, middle and last elements 
        of an input list.
        
        For an odd length list, middle is defined as usual.
        For an even length list, middle picks the left of the two middle elements.
        
        Then chooses the median of those first, middle, last.
        """
        first = left
        mid = math.floor((left + right - 0.5) // 2)
        last = right - 1
        
        # First, middle and last elements need to be distinct
        
        if right == left + 2 or right == left + 1:
            return left
        
        d = {
            A[first]: first,
            A[mid]: mid,
            A[last]: last
            }
        
        med_val = int(statistics.median(d.keys()))
        median_idx = d[med_val]
        
        return median_idx


#%% Define Algorithm

def QuickSort(A: list, left: int, right: int, pivot_case: str) -> list:
    """
    Implementation of QuickSort sorting algorithm. Allows for different approaches
    to selecting the pivot element for recursive partitioning. 
    
    Parameters
    ----------
    A : list
        Unsorted list of numbers.
    left, right : int
        list indices, made available to facilitate recursive calls of the function.
    pivot_case : str
        Approach for choosing pivot point. Options: 'First_Element', 'Last_Element', 'Median_Element'.
        See class PivotCase() for more information.

    Returns
    -------
    A : list
        Sorted list.
    """
    
    # Terminate recursion if indices violate constraint
    if left >= right:
        return
    
    # Define pivot point
    p = PivotCase(A, left, right).ChoosePivot(pivot_case)
    
    # Prepare array for partition subroutine by swapping pivot and first element.
    A[p], A[left] = A[left], A[p] 
    
    # Partition() partitions the list into [ <p, p, >p ].
    # Note that <p is not sorted. >p is also not sorted.
    new_piv = partition(A, left, right)
    
    # Recursively run QuickSort on partitioned array
    QuickSort(A, left, new_piv, pivot_case)
    QuickSort(A, new_piv + 1, right, pivot_case)
    
    return A


def partition(A: list, left: int, right: int) -> None:
    """
    A subroutine which partitions A around a pivot index.
    Mutates the original list and does not return anything.
    
    Inputs
    -------
    The left and right endpoints of the partition. left <= right. 
    
    Example
    -------
    partition(A = [0, 1, 2, 5, 3, 4], left = 3, right = 5) would only partition 
    [5, 3, 4]
    """
    
    pivot = left
    i = left + 1
    partition.count += (right - left - 1 if right > left else 0)
    for j in range(left + 1, right):
        if A[j] < A[pivot]:
            A[j], A[i] = A[i], A[j]
            i += 1

    A[pivot], A[i - 1] = A[i - 1], A[pivot]
    return i - 1        

    
#%% Load Sample Array

array = []

with open("Input_array_QuickSort.txt") as f:
    for line in f:
        array.append(int(line.strip('\n')))

#%% Run Main 

def main(A: list, pivot_case: str):

    partition.count = 0
    QuickSort(A, 0, len(A), pivot_case)
    did_it_work = utils.is_sorted(A)
    
    print(f"To sort an array of size {len(A)}, we made {partition.count} comparisons. \nWe used the {pivot_case} as our pivot.\nIs our list sorted?: {did_it_work}")
    return partition.count, A

# Test Pivot Selection Approaches

# main(array, 'First_Element')
# main(array, 'Last_Element')
main(array, 'Median_Element')
                
