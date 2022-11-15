import random 
from Interfaces import Queue 
import ArrayQueue


class RandomQueue(Queue):
    def __init__(self):
        self.queue = ArrayQueue.ArrayQueue()

    def add(self, x: object):
        '''
            add: Add the value x to the Queue
            Inputs:
                x: Object type, i.e., any object
        '''
        self.queue.add(x)

    def remove(self) -> object:
        if self.queue.size() == 0:
            raise IndexError()

        y = random.randint(0, self.queue.size() - 1)
        temp = self.queue.a[self.queue.j]
        self.queue.a[self.queue.j] = self.queue.a[y]
        self.queue.a[y] = temp
        self.queue.remove()
    
    def size(self) -> int:
        return self.queue.size()


'''
q = RandomQueue()
q.add("a")
q.add("b")
q.add("c")
q.add("d")
q.remove()
print(q.queue)
'''
