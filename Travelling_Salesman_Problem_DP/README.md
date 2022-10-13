 # Travelling Salesman Problem
 
 ### Problem Statement
 
 The Travelling Salesman Problem (also called the TSP) asks the following question: *"Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?"* It is an NP-hard problem in combinatorial optimization, important in theoretical computer science and operations research.

 ### Solution
 
 Numerous algorithms have been proposed to tackle the TSP, ranging greatly in computational time and solution accuracy. The slowest approach (i.e. the brute-force algorithm) runs in O(n!) time while guaranteeing an optimal solution.

 This algorithm leverages off dynamic programming principles (top-down recursion and memoization) to solve the TSP. Its running time is considerably better (although still exponential) - for a set of size n, we consider n-2 subsets, each of size n-1, such that all subsets don’t have nth in them. There are at most O(n x 2^n) sub-problems, and each one takes linear time to solve. The total running time is therefore O(n^2 x 2^n). 

 That being said, as an additional optimisation, the implementation utilises bit-wise operations (Gosper's Hack) for faster iterations via bitmasks.

 ### Overview of the Dynamic Programming Solution

 Let the given set of vertices be {1, 2, 3, 4,….n}. Let us consider 1 as starting and ending point of output. For every other vertex I (other than 1), we find the minimum cost path with 1 as the starting point, I as the ending point, and all vertices appearing exactly once. Let the cost of this path cost (i), and the cost of the corresponding Cycle would cost (i) + dist(i, 1) where dist(i, 1) is the distance from I to 1. Finally, we return the minimum of all [cost(i) + dist(i, 1)] values. This looks simple so far. 

 Now the question is, how to get cost(i)? To calculate the cost(i) using Dynamic Programming, we need to have some recursive relation in terms of sub-problems. 
 
 Let us define a term C(S, i) as the cost of the minimum cost path visiting each vertex in set S exactly once, starting at 1 and ending at i. We start with all subsets of size 2 and calculate C(S, i) for all subsets where S is the subset, then we calculate C(S, i) for all subsets S of size 3 and so on. Note that 1 must be present in every subset.

 ``` 
	If size of S is 2, then S must be {1, i},
 		C(S, i) = dist(1, i) 
	Else if size of S is greater than 2.
 		C(S, i) = min { C(S-{i}, j) + dis(j, i)} where j belongs to S, j != i and j != 1.
 ```

 For additional performance gains, we can use the bitmasks to represent the remaining nodes in our subset.
 
 ### Gosper's Hack (Bitmasks)

 Gosper’s Hack iterates through all n-bit values that have k bits set to 1, from lowest to highest. It is an efficient way of taking a number and getting the next number with the same number of bits set. Below is the code, written in C:
 
 ```
	int set = (1 << k) - 1;
	int limit = (1 << n);
	while (set < limit) {
    		doStuff(set);

    		// Gosper's hack:
    		int c = set & -set;
    		int r = set + c;
    		set = (((r^set) >>> 2) / c) | r;
	}
 ```
 
 ### Note on Sample Data
 
 The implementation can take input graphs in form of either Eucledian distances or as matrices of edge costs. Test cases in this repository are presented in the Eucledian distances format.
 As such, the first line indicates the number of cities. Each city is a point in the plane, and each subsequent line indicates the x- and y-coordinates of a single city.  
 The distance between two cities is defined as the Euclidean distance - that is, two cities at locations *(x,y)* and *(z,w)* have distance \sqrt{(x-z)^2 + (y-w)^2} between them.   
