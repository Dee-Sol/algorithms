 # Overview

 ### Maximum Spacing k-Clustering Algorithm

 The implementation returns maximum spacing for a given number of clusters. It is based on a greedy clustering algorithm (variant of Kruskal's Minimum Spanning Tree algorithm). We greedily take the closest pair of separated points and fuse them into the same cluster, iteratively increasing the maximum spacing.
 
 ### Maximum k-Clustering Algorithm

 A variant of a clustering algorithm, which computes maximum number of k-clusters given a desired minimum spacing between vertices (implementation uses minimum distance of 3 units by default). In other words, all pairs of vertices with spacing of 2 or less fall within the same clusters.

 The implementation supports very large graphs via usage of Hamming distances (and subsequently bit-masks/bit-shifts) and the Union-Find data structure. These enhancements come at the expense of deviation from Kruskal's Minimum Spanning Tree algorithm. 

 ###### Note on Input Graph

 The second algorithm is built to support MUCH bigger graphs. However, the distances (i.e., edge costs) will have to be defined implicitly, rather than being provided as an explicit list.
 
 The input format is: [# of nodes] [# of bits for each node's label]
 
 [first bit of node 1] ... [last bit of node 1]
 
 [first bit of node 2] ... [last bit of node 2]
 
 ...
 
 For example, the third line of the sample input file *data_clustering_big.txt* "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 bits associated with node #2.

 The distance between two nodes *u* and *v* is defined as the Hamming distance - the number of differing bits - between the two nodes' labels. For example, the Hamming distance between the 24-bit label of node #2 above and the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 (since they differ in the 3rd, 7th, and 21st bits).