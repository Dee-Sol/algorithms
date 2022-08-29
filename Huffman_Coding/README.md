 # Huffman Coding
 
 ### Overview
 Huffman Coding is a greedy algorithm that uses binary trees to generate binary prefix-free encoding for a given set of characters. The binary tree returned by the algorithm minimizes the average encoding length by giving the symbols that are more frequent, which can be represented by node weights, shorter encodings. As such, the goal is to generate variable-length encodings in which no code is a prefix of another (i.e. "prefix-free"). Huffman coding is a fundamental type of lossless compression (e.g. mp3)

 The implementation uses heaps data structure as well as a bespoke implementation of binary trees to optimize computation time.

 ### Note on Sample Data

 The *Sample_huffman_data.txt* file contains sample input data to test the algorithm implementation. It has the following format:

[number_of_symbols]

[weight of symbol #1]

[weight of symbol #2]

...

 For example, the third line of the file is "6852892," indicating that the weight of the second symbol of the alphabet is 6852892. (The sample data uses weights instead of frequencies)


