# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 12:33:03 2022

Recursive Algorithm for Karatsuba Multiplication

@author: D. S.
"""
#%% Import libraries

import numpy as np

#%% Define Algorithm

def Karatsuba(x,y):
    """
    Recursive algorithm for Karatsuba multiplication

    Parameters
    ----------
    x : int
    y : int

    """
    if len(str(x)) == 1 and len(str(y)) == 1:
        # Define base case      
       
        return int(x*y)
    else:
                # add digits if digits of x and y are not the same or
        # not equal to the exponential of 2
        len_max=max(len(str(x)),len(str(y)))
        log_len_max=np.log2(len_max)
        
        if np.floor(log_len_max)-log_len_max!=0:
            len_max=int(2**(np.ceil(log_len_max)))
        
        # Pad integers with zeros if of unequal or odd lengths   
        x = '0'*(len_max-len(str(x)))+str(x)
        y = '0'*(len_max-len(str(y)))+str(y)
        
    
        # Split integers
        m2 = int(len_max/2)
        
        a = int(x[:m2])
        b = int(x[m2:]) 
        
        c = int(y[:m2]) 
        d = int(y[m2:])
        
      
        # Recursively call Karatsuba function
        z_0 = Karatsuba(a,c)
        z_1 = Karatsuba(b,d)
        z_2 = Karatsuba(a+b,c+d)
        
        # compute multiplication using Gaussian trick
        return int((z_0*10**(2*m2))+((z_2-z_1-z_0)*10**m2)+(z_1))

#%% Run Algorithm

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627


print(Karatsuba(x, y))

