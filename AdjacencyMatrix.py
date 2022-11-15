"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack

class AdjacencyMatrix(object):
    def __init__(self, n):
        self.n = n
        self.a = np.zeros([n, n], np.bool_)
                
    def add_edge(self, i, j):
        pass
        
    def remove_edge(self, i, j):
        pass
        
    def has_edge(self, i, j):
        pass

    def out_edges(self, i):
        pass
        
    def in_edges(self, i):
        pass
        
    def in_degree(self, i):
        pass
        
    def out_degree(self, i):
        pass

    def size(self) -> int :
        return self.n
                  
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            for j in range(0, self.n):
                if self.has_edge(i,j):
                    s += f"{i,j}"
        return s

'''
g = AdjacencyMatrix(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 4)
g.add_edge(4, 5)

print(g.dfs(0,1))

'''
