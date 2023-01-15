import numpy as np
from Interfaces import Queue


def left(i: int):
    if i < 0:
        raise IndexError()
    return 2*i + 1


def right(i: int):
    if i < 0:
        raise IndexError()
    return 2*(i+1)


def parent(i: int):
    if i < 0:
        raise IndexError()
    return (i-1)//2


class BinaryHeap(Queue):
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) -> np.array:
        return np.zeros(n, np.object_)

    def resize(self):
        pass

    def add(self, x: object):
        pass

    def bubble_up(self, i):
        pass

    def remove(self):
        pass

    def trickle_down(self, i):
        pass

    def find_min(self):
        if n == 0:
            raise IndexError()
        return a[0]

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i < self.n-1:
                s += ","
        return s + "]"
