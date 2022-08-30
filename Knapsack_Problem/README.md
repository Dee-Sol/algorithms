 # Knapsack Algorithm
 
 ### Problem Statement
 
 The Knapsack Problem is as follows. We are given *n* number of items with weights *w_i* and values *v_i*, as well as the capacity of the knapsack *W*. We are asked to find a subset *S* of the items that maximizes sum(*v_i*), subject to sum(*w_i*) <= *W*

 ### Solution
 
 This implementation solves the Knapsack Problem using the Dynamic Programming principles. In fact, the implementation was extended to apply the paradigm in two ways - either iteratively or recursively. While both perform equally well on smaller lists of items, the recursive approach scales up considerably better. This is because the iterative method checks all capacities at each iteration, while the recursive one checks only those that are achievable by combining item sizes. Note, however, that the computation time benefits come at the expense of larger stack size requirements as well as raising default recursion limits. 
 Sample data of different sizes is included in the repository to test computational time of both methods.

 ### Dynamic Programming Algorithm
 
 - V_(i,x): Value of the best solution that only uses the first i items and has a total size <= x
 - For each i in {1, .., n} and any x there are two cases, from which we take the bigger value
	- V_(i-1, x) --> last item i excluded
	- v_i + V_(i-1, x-w_i) --> last item included
 - The Knapsack problem can be solved by calculating a 2D-matrix of shape (n, W):
	- Initialize A[0,:] = 0
	- for i in {1,2,...,n}
		- for x in {0,1,...,W}
			- A[i,x] = max(A[i-1,x], A[i-1, x-w_i] + v_i)
			- if w_i > W we are forced to use the first case
 

 ### Note on Sample Data

 This file describes a knapsack instance, and it has the following format:

[knapsack_size][number_of_items]

[value_1] [weight_1]

[value_2] [weight_2]

...

 For example, the third line of the file is "50074 659", indicating that the second item has value 50074 and size 659, respectively.