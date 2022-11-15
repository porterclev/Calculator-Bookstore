from Interfaces import Set
from DLList import DLList
import ChainedHashTable 

class ChainedHashTableWithDuplications(Set):
    def __init__(self) :
        self.chainHashTable = ChainedHashTable.ChainedHashTable()
        self.n = 0

    def size(self) -> int:
        return self.n
        
    def find(self, key : object) -> object :
        d = DLList()
        for i in range(self.chainHashTable.t[self.chainHashTable.hash(key)].size()):
            if self.chainHashTable.t[self.chainHashTable.hash(key)].get(i).key == key:
                d.append(self.chainHashTable.t[self.chainHashTable.hash(key)].get(i).value)
        return d
    
    def add(self, key : object, value : object) :
        if self.n == len(self.chainHashTable.t):
            self.chainHashTable.resize()
        
        self.chainHashTable.t[self.chainHashTable.hash(key)].append(self.chainHashTable.Node(key, value))
        self.n=+1
        
    def remove(self, key : int)  -> object:
        for i in range(self.chainHashTable.t[self.chainHashTable.hash(key)].size()):
            if self.chainHashTable.t[self.chainHashTable.hash(key)].get(i).key == key:
                self.chainHashTable.t[self.chainHashTable.hash(key)].remove(i)
                self.n-=1
                
                if 3 * self.n <= len(self.chainHashTable.t):
                    self.resize()
                return True
        return False
            
            
        
    
    def __str__(self):
        return self.cht.__str__()


# c = ChainedHashTableWithDuplications()
# c.add(1, "a")
# c.add(1, "b")
# c.add(2, "c")
# c.add(3, "d")
# c.add(3, "e")
# print(c.find(3))

