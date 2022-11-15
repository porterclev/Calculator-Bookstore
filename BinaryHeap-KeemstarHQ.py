import numpy as np
from numpy.core.records import array
from ArrayQueue import ArrayQueue
from Interfaces import Queue



def left(i : int):
    if i< 0: raise IndexError()
    return 2*i + 1

def right(i: int):
    if i< 0: raise IndexError()
    return 2*(i+1)

def parent(i : int):
    if i< 0: raise IndexError()
    return (i-1)//2

class BinaryHeap(Queue):
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0
        self.j = 0

    def new_array(self, n: int) ->np.array:
        return np.zeros(n, np.object)

    def resize(self):
        b = self.new_array(max(1, 2 * self.n))
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b

    def add(self, x : object):
        if len(self.a) < self.n + 1:
            self.resize()
            
        self.a[self.n] = x
        self.n+=1
        self.bubble_up(self.n - 1)
        
        return True

    def bubble_up(self, i):
        p = parent(i)
        while i > 0 and self.a[i] < self.a[p]:
            self.a[i], self.a[p] = self.a[p], self.a[i]
            i = p
            p = parent(i)

    def remove(self):
        x = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.n-=1
        self.trickle_down(0)
        if 3 * self.n < len(self.a):
            self.resize()
        return x

    def trickle_down(self, i):
        while i >= 0:
            self.j = -1
            r = right(i)
            if r < self.n and self.a[r] < self.a[i]:
                l = left(i)
                if self.a[l] < self.a[r]:
                    self.j = l
                else:
                    self.j = r
            else:
                l = left(i)
                if l < self.n and self.a[l] < self.a[i]:
                    self.j = l
                    
            if self.j >= 0:
                self.a[self.j], self.a[i] = self.a[i], self.a[self.j]
            i = self.j

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i  < self.n-1:
                s += ","
        return s + "]"

# h = BinaryHeap()
# h.add(2)
# h.add(1)
# h.add(5)
# print(h.size())
# print(h.remove())
# h.add(4)
# h.add(1)
# h.add(3)
# print(h.size())
# print(h.remove())
# print(h.remove())
# print(h.remove())
# print(h.remove())
# print(h.remove())

