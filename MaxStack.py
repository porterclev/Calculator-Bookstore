from numpy.core.arrayprint import IntegerFormat
from Interfaces import Stack
import SLLStack


class MaxStack(Stack) :
    def __init__(self):
        self.stack = SLLStack.SLLStack()
        
    def max(self) ->object:
        '''
            Returns the max element
        '''
        try:
            if self.stack.head == None:
                raise Exception()
            
            cur = self.stack.head
            max = cur.x
            
            while cur:
                if max < cur.x:
                    max = cur.x
                cur = cur.next
            return max
        except Exception:
            print("empty list")
                
    
    def push(self, x : object) : 
        '''
            push: Insert an element in the tail of the stack 
            Inputs:
                x: Object type, i.e., any object
        '''
        new_node = self.stack.Node(x)
        if self.stack.n == 0:
            self.stack.head = new_node
        else:
            self.stack.tail.next = new_node
            
        self.stack.tail = new_node
        self.stack.n+=1

    def pop(self) -> object:
        '''
            pop: Remove the last element in the stack 
            Returns: the object of the tail if it is no empty
        '''
        try:
            if self.stack.head is None:
                raise Exception()
            
            p = self.stack.head
            x = self.stack.tail
        
            for i in range(self.stack.n - 2):
                p = p.next
                
            p.next = None
            self.stack.tail = p
            self.stack.n-=1
            return x.x
        
        except Exception:
            print("empty list")
    

    def size(self) -> int:
        return self.stack.size()

