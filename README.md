# Algorithms
 *Implementation of Various Algorithms using Python*

 ### Collaborative Filtering

 Implementation of Collaborative Filtering using Merge-Sort algorithm. As part of implementation, the sorting algorithm counts the number of inversions in an array.

 ### Dijkstra's Shortest-Path
 
 Implementation of Dijkstra's Shortest-Path algorithm using heaps data structure. Calculates shortest distance from a given vertex of an undirected weighted graph to any other vertex. 

 ### k-Clustering Algorithms
 
 Two implementations of clustering algorithms (for more detail, see ReadMe in respective folder). The first one is a variant of Kruskal's Minimum Spanning Tree algorithm. 

 The second one is intended for much larger graphs, as it uses: 1) Hamming distances to leverage off of bit-masks, and 2) the Union-Find data structure.

 ### Karatsuba Multiplication
 
 Recursive algorithm for computation of product of two large integers (e.g. 64-bit) using Karatsuba multiplication method.

 ### Karger's Minimum Cut Algorithm
 
 A randomized algorithm that computes a minimum cut of an undirected graph. It performs randomized contraction of edges until a multigraph of two vertices is produced. Implementation allows for measurement of basic performance statistics across iterations.

 ### Kosaraju's Algorithm 
 
 Implementation of Kosaraju's algorithm, which computes strongly connected components of a directed graph. Implementation consists of two passes of the Depth-First Search algorithm. While the original algorithm is recursive, this implementation is iterative.

 ### Maximum-Weight Independent Set
 
 The algorithm leverages off of principles of dynamic programming to compute maximum-weight independent set for a path graph, where independent set is defined as a set of non-adjacent vertices. The implementation splits computation into two parts: 1) Memoization algorithm, and 2) Reconstruction algorithm. For more detail, see ReadMe in respective folder.

 ### Median Maintenance

 Implementation of the Median Maintenance algorithm using "heaps" data structure. The algorithm maintains a running median of an input array by breaking it up into a MIN heap and a MAX heap.

 ### Prim's Minimum Spanning Tree

 Implementation of Prim's Minimum Spanning Tree (MST) algorithm. An MST is a subset of all edges that includes every vertex of a weighted undirected graph, where the total weight of all the edges in the tree is minimized. The implementation uses the heap data structure, which is used to store unprocessed vertices. 

 ### Scheduling Algorithm

 A simple greedy algorithm for scheduling tasks with varying priorities and durations. The algorithm minimizes weighted sum of completion times and allows for a choice of the minimization method - either on the basis of a task's ratio (priority/duration) or its relative difference (priority - duration).

 ### QuickSort Algorithm

 Implementation of QuickSort algorithm. It allows for a choice of the pivot element, including implementation of Randomized QuickSort (Median-of-Three pivoting). Implementation allows for comparison of relative performance across approaches to recursive partitioning by keeping track of the number of element swaps needed to sort the array.

 ### 2-Sum Algorithm

 A variant of the 2-Sum algorithm. The implementation computes the number of target values t within a definable interval, such that there are distinct numbers x, y in the input array that satisfy x+y=t. Implementation uses a hash table to speed up the search sub-routine.
