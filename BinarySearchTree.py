from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self, nil=None):
        super().__init__()
        self.n = 0
        self.nil = nil
        
    def clear(self):
        self.r = self.nil
        self.n = 0

    def new_node(self, x):
        u = BinaryTree.Node(x)
        u.left = u.right = u.parent = self.nil
        return u
    
        
    def find_last(self, x : object) -> BinaryTree.Node:
        pass
        
    def add_child(self, p : BinaryTree.Node, u : BinaryTree.Node) -> bool:
        pass

    def find_eq(self, x : object) -> object:
        pass
    
    def find(self, x: object) -> object:
        pass
        
    def add(self, key : object, value : object) -> bool:
       pass
        
    def add_node(self, u : BinaryTree.Node) -> bool:
        pass
    
    def splice(self, u: BinaryTree.Node):
        pass

    def remove_node(self, u : BinaryTree.Node):
        pass

    def remove(self, x : object) -> bool:
        pass
             
    def __iter__(self):
        u = self.first_node()
        while u != self.nil:
            yield u.x
            u = self.next_node(u)


'''         
q = BinarySearchTree()
q.add(3, "third")
q.add(2, "second")
q.add(1, "first")
print(q.find(2.5))
q.remove(3)
print(q.find(3))
q.add(3, "third")
q.add(5, "fifth")
q.add(4, "fourth")
print(q.find_eq(3.4))
print(q.find(3.4))
print("In order")
q.in_order()
print("Pre oder")
q.pre_order()
print("Pos order")
q.pos_order()
'''