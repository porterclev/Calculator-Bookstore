import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import AdjacencyList
import AdjacencyMatrix
import BookStore


class  Lab7(unittest.TestCase) :
    
    def test_graph(self) :
        points = 0.5
        q = AdjacencyMatrix.AdjacencyMatrix(4)
        try:
            q.remove_edge(1, 2)
            q.has_edge(2,3)
            q.add_edge(0,1) 
            q.add_edge(1,2)
            q.add_edge(2,3) 
            q.add_edge(3,0)
            q.add_edge(0,2)
            
            self.assertAlmostEqual(q.has_edge(0,1), True)
            self.assertAlmostEqual(q.has_edge(1,3), False) 
            print("AdjacencyMatrix in_edges(2)", q.in_edges(2))
            print("AdjacencyMatrix out_edges(0)", q.out_edges(0))
            points += 0.5
           
        except:
            print("AdjacencyMatrix is not correct")
        
        
        q = AdjacencyList.AdjacencyList(4)
        try:
            q.remove_edge(1, 2)
            q.has_edge(2,3)
            q.add_edge(0,1) 
            q.add_edge(1,2)
            q.add_edge(2,3) 
            q.add_edge(3,0)
            q.add_edge(0,2)
            self.assertAlmostEqual(q.has_edge(0,1), True)
            self.assertAlmostEqual(q.has_edge(1,3), False) 
            print("AdjacencyList in_edges(2)", q.in_edges(2))
            print("AdjacencyList out_edges(0)", q.out_edges(0))
            points += 0.5
            print("BFS(0)")
            q.bfs(0)
            print("DFS(0)")
            q.dfs(0)
            points += 0.5
        except:
            print("AdjacencyList is not correct")
        
    
        print(f"Graph: {points} Points")

     
    def test_BookStore(self) :
        points = 0.5
        #try:
        
        try:
            a = BookStore.BookStore()
            a.loadCatalog("../books.txt")
            a.searchBookByInfix("The Art of Machine Piecing")
            a.searchBookByInfix("The Best of Howard Jones")
            points += 0.5
            self.assertAlmostEqual(a.pathLength("0807842591", "1557509646"), 3948)
            self.assertAlmostEqual(a.pathLength("B00005M2DR", "B00005M2DZ"), 1)
           
            points += 1
        except:
            print("BookStore is not correct")
        finally:
            print(f"BookStore: {points} Points")
    
    