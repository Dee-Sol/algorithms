# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 17:20:33 2022

Implementation of Collaborative Filtering using a Recursive Algorithm
that Counts Number of Inversions in an Array.

@author: D. S.
"""
  
#%% Define Algorithm

def CountInv(A, count=0):
    """
    Recursive Algorithm for Collaborative Filtering

    Parameters
    ----------
    A : Array
        Unsorted Input Array.
    count : Integer, optional
        Count of Invesions. The default is 0.

    Returns
    -------
    Array
        Sorted Input Array.
    Integer
        Count of Inversions.

    """
    
    # Base Case of Recursion
    if len(A) == 1:
        return A, 0 
    
    # Non-Base Case 
    m2 = int(len(A)/2)
    a = A[:m2]
    b = A[m2:]
    
    left, count_l = CountInv(a, count)
    right, count_r = CountInv(b, count)
    
    # Initiate Merge-Sort, while counting number of split inversions
    # Note: from coding standpoint, we only look for split inversions.
    i = 0 # index of left side of array
    j = 0 # index of right side of array
    k = 0 # index of original array
            
    # Note: The number of split inversions = number of remaining items in [a] after this point
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            A[k] = a[i]
            i+=1

        else:
        # the `else` condition is where we find split inversions: when a[i] > b[j]
            A[k] = b[j]
            j+=1
            # Increment count of split inversions
            count += len(a) - i 
        k+=1
    
    # deal with remaining items in left array if longer than [b]
    while i < len(a):
        A[k] = a[i]
        i+=1
        k+=1
    
    # deal with remaining items in right array if longer than [a]
    while j < len(b):
        A[k] = b[j]
        j+=1
        k+=1
    
    # split inversions + left inversions + right inversions
    return A, (count + count_l + count_r)
 
#%% Load Sample Array

array = []
with open("IntegerArray.txt") as f:
    for line in f:
        array.append(int(line.strip('\n')))

#%% Calculate Number of Inversions in Sample Array

print(CountInv(array))
