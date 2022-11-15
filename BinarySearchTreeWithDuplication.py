from BinarySearchTree import BinarySearchTree
from Interfaces import Set


class BinarySearchTreeWithDuplication(Set):

    def __init__(self, nil=None):
        self.binaryTree = BinarySearchTree()
        self.n = 0
        
    def size(self) -> int:
        return self.n 

    def find(self, x: object) -> object:
        pass

    def add(self, key : object, value : object) -> bool:
        pass    
    
    def remove(self, x : object) -> bool:
        pass

'''         
q = BinarySearchTreeWithKeyDuplication()
q.add(1, "a")
q.add(1, "b")
q.add(2, "c")
q.add(3, "d")
q.add(3, "e")
find(1)
find(2)
find(3)
'''