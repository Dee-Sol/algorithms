# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 2022

Helper Function to Check if Output Array Has Been Sorted

@author: D.S.
"""

def is_sorted(lst) -> bool:
  for i in range(len(lst) - 1):
    if lst[i] > lst[i+1]:
      return False
  return True