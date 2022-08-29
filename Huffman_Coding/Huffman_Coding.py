# -*- coding: utf-8 -*-
"""
Created on Aug 22 2022

Implementation of Huffman Coding - a greedy algorithm which generates binary 
prefix-free encoding for a given set of characters.

Optimal computation time of the Huffman tree is achieved by using heaps data 
structure as well as a bespoke variant of binary search trees.

@author: D. S.
"""

#%% Define Algorithm

from heapq import heappop, heappush, heapify

class Node(object):
    def __init__(self, left_node=None, right_node=None, weight=None):
        self.left_node = left_node
        self.right_node = right_node
        self.weight = 0
        # Running sum of weights of leaves
        self.weight = weight or left_node.weight + right_node.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return str(self.weight)


def import_data(filename: str):
    """ 
    Imports symbols for Huffman coding and converts them into a Node object.
    
    """

    with open(filename) as f:
        lines = f.readlines()
        n_symbols = int(lines[0])
        print(f'{n_symbols} symbols')
        weights = [int(line) for line in lines[1:]]
    
    # create leaf-nodes from the weights
    nodes = [Node(None, None, weight) for weight in weights]
    assert len(nodes) == n_symbols, 'something went wrong'
    
    return nodes


def huffman(nodes):
    """ 
    Constructs a Huffman binary tree for a given set of weights. 
    The implementation uses heaps data structure and the Node object.
    
    Loops through input weights, each time merging together two nodes with 
    smallest weights. 
    
    Note the importance of Node's subroutine in calculating the 
    running sum of leaves' weights.
    
    """
    while len(nodes) > 1:

        heapify(nodes)
        heappush(nodes, Node(heappop(nodes), heappop(nodes)))
    
    return nodes
    
def get_depth(node: object, minmax: str) -> int:
    """ Calculates minimum or maximum depth of a Huffman binary tree. """
    
    if node.left_node:
        depth_left = 1 + get_depth(node.left_node, minmax)
    else:
        depth_left = 0
    if node.right_node:
        depth_right = 1 + get_depth(node.right_node, minmax)
    else:
        depth_right = 0

    return minmax(depth_left, depth_right)

#%% Define Main

def main(filename: str):
    nodes = import_data(filename)
    nodes = huffman(nodes)
    Huffman_Tree = nodes[0]
    max_depth = get_depth(Huffman_Tree, max)
    min_depth = get_depth(Huffman_Tree, min)
    print('min. depth', min_depth)
    print('max. depth', max_depth)
    assert min_depth == 9
    assert max_depth == 19

#%% Run Main

if __name__ == '__main__':
    main('sample_huffman_data.txt')
