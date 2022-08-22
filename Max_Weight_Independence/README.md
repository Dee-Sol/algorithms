 ## Maximum-Weight Independent Set Algorithm

 The algorithm leverages off of principles of dynamic programming to compute maximum-weight independent set for a path graph, where independent set is defined as a set of non-adjacent vertices. More specifically, it uses solutions caching and a subsequent reconstruction procedure to solve a problem that would have been more complex otherwise. 

 #### Synopsis
 After generating the array A which holds the maximum weights for subsets of the path graph, we traversed A backwards to generate the actual maximum-weight independent set (MWIS) of the path graph, each time deciding whether or not to include a vertex in the MWIS depending on whether or not the previous entry in A is equal to (case 1) or less (case 2) than the current entry in A.

 #### Memorization Algorithm
 Linear computation time can be obtained by caching the solution of already solved subproblems ("memorization")
 - Let G_i be the first i nodes of the path w_1, w_2, ..., w_n
 - the caching can be done by building the graph bottom up and storing the results for G_i in an array A
    - A[0] = 0 (no nodes)
    - A[1] = w_1
    - for i in 2..n:
        - A[i] = max(A[i-1], A[i-2] + w_i)
        
 #### Reconstruction Algorithm
 - above algorithm calculates the total weight of the max-weight IS of a path graph, but not the IS itself
 - because the Array A contains all the solutions for the sub-problems it can be used to reconstruct the IS as follows:
    - process A from right to left
    - S = {}
    - if A[i-1] >= A[i-2] + w_i: i--
    - else add w_i to S and i -= 2

 ## Principles of Dynamic Programming
 
 This algorithm provides an example of how dynammic programming can be useful for problems where we can: 
 1. identify a small number of sub-problems, 
 2. quickly compute and correctly solve larger sub-problems given the solutions to smaller ones, and 
 3. quickly compute the final solution after solving all sub-problems. 

 In general, reasoning about the structure of the optimal solution is how we identify what the smaller sub-problems should be in dynamic programming.
 
 ## Sample Data

 The accompanying text file describes the weights of the vertices in a path graph (with the weights listed in the order in which vertices appear in the path). It has the following format:
 
 [number_of_vertices]
 
 [weight of first vertex]
 
 [weight of second vertex]
 
 ...
 
 For example, the third line of the file is "6395702," indicating that the weight of the second vertex of the graph is 6395702.