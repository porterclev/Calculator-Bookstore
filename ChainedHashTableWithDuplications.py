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
        pass
        
    def add(self, key : object, value : object) :
        pass


    def remove(self, key : int)  -> object:
        pass
    
    
    def __str__(self):
        return self.cht.__str__()




