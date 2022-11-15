import numpy as np
from Interfaces import Stack


class ArrayStack(Stack):
    """
        ArrayStack: Implementation of the Stack interface based on Arrays.
        All the @abstractemthods should be implemented.
        An instance of ArrayStack has access to all the methods in ArrayStack and
        all the methods of the base class (Stack). When executing a method, it executes
        the method of ArrayStack, if it does not exists, it executes the method in the
        Base class (Stack).
        For example,
        s = ArrayStack()
        print(s)
        print(len(s))
    """
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) -> np.array:
        return np.zeros(n, np.object)
    
    def resize(self):
        b = self.new_array(max(1, 2 * self.n))
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b

    def get(self, i: int) -> np.object:  # Modify
        if i < 0 | i > self.n - 1:
            raise IndexError()
        else:
            return self.a[i]
    
    def set(self, i: int, x: np.object) -> object:  # Modify
        if i < 0 or i > self.n - 1:
            raise IndexError()
        else:
            y = self.a[i]
            self.a[i] = x
            return y
    
    def add(self, i: int, x: np.object):  # Modify
        try:
            if i < 0 or i > self.n + 1:
                raise Exception
            else:
                if self.n == len(self.a):
                    self.resize()

                for j in range(self.n, i, -1):
                    self.a[j] = self.a[j - 1]

                self.a[i] = x
                self.n += 1
        except Exception:
            raise IndexError()

    def remove(self, i: int) -> np.object:  # Modify
        try:
            if i < 0 or i > self.n - 1:
                raise Exception
            else:
                y = self.a[i]

                for j in range(i, self.n - 1):
                    self.a[j] = self.a[j + 1]

                self.n -= 1

                if len(self.a) >= self.n * 3:
                    self.resize()

                return y
        except Exception:
            raise IndexError()

    def push(self, x: np.object):
        self.add(self.n, x)
    
    def pop(self) -> np.object:
        return self.remove(self.n-1)

    def size(self):
        return self.n
        
    def __str__(self) -> str:
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i]
            if i < self.n-1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator += 1
        else:
            raise StopIteration()
        return x


'''
s = ArrayStack()
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)
print(s.get(0))
print(s)

s.add(1, 4)
print(s)

s.add(4, 3)
print(s)

print(s)
print(s.get(0))
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)

# s.remove(1)
# s.add(9, 2)
# s.set(9, 2)
# print(s.get(20))

s = ArrayStack()
s.push(1)
s.push(2)
print(s.pop(), "= 2")
s.push(3)
print(s.pop(), "= 3")
s.push(4)
s.push(5)
print(s.pop(), "= 5")
print(s.pop(), "= 4")
print(s.pop(), "= 1")
'''
