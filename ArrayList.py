import numpy as np
from Interfaces import List


class ArrayList(List):
    def __init__(self):
        self.n = 0
        self.j = 0
        self.a = self.new_array(1)
        
    def new_array(self, n: int) -> np.array:
        return np.zeros(n, np.object)
    
    def resize(self):  # Modify
        b = self.new_array(max(1, 2 * self.n))

        for k in range(self.n):
            b[k] = self.a[(self.j + k) % len(self.a)]

        self.a = b
        self.j = 0

    def get(self, i: int) -> object:  # Modify
        if i < 0 | i > self.n - 1:
            raise IndexError()
        else:
            return self.a[(self.j + i) % len(self.a)]

    def set(self, i: int, x: object) -> object:  # Modify
        if i < 0 or i > self.n - 1:
            raise IndexError()
        else:
            y = self.a[(self.j + i) % len(self.a)]
            self.a[(self.j + i) % len(self.a)] = x
            return y

    def append(self, x: object):
        self.add(self.n, x)
        
    def add(self, i: int, x: object):  # Modify
        try:
            if i < 0 or i > self.n:
                raise Exception()

            if self.n == len(self.a):
                self.resize()

            if i < self.n/2:
                self.j = (self.j - 1) % len(self.a)

                for k in range(0, i):
                    self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k + 1) % len(self.a)]
            else:
                for k in range(self.n, i, -1):
                    self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k - 1) % len(self.a)]

            self.a[(self.j + i) % len(self.a)] = x
            self.n += 1
        except Exception:
            raise IndexError()
    
    def remove(self, i: int) -> object:  # Modify
        try:
            if i < 0 or i >= self.n:
                raise Exception()

            x = self.a[(self.j + i) % len(self.a)]

            if i < self.n/2:
                for k in range(i, 0, -1):
                    self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k - 1) % len(self.a)]

                self.j = (self.j + 1) % len(self.a)
            else:
                for k in range(i, self.n - 1):
                    self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k + 1) % len(self.a)]

            self.n -= 1

            if len(self.a) >= 3 * self.n:
                self.resize()

            return x
        except Exception:
            raise IndexError()

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i < self.n-1:
                s += ","
        s += f"] {self.n} : {self.j}"
        return s

    def __getitem__(self, i) -> object:
        """
            __getitem__: Returns the item in the position i in array format, i.e., l[i]
            where l is a list instance
            Input:
                i: positive integer less than n
            Return: the item at index i
        """
        if isinstance(i, slice):
            return [self.get(i) for i in range(i.start, i.stop)]
        else:
            return self.get(i)

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[(self.iterator + self.j) % len(self.a)]
            self.iterator += 1
        else:
            raise StopIteration()
        return x


'''
arraylist = ArrayList()
arraylist.add(0, 4)
print(arraylist)
arraylist.add(0, 1)
print(arraylist)
arraylist.add(1, 3)
print(arraylist)
arraylist.add(1, 2)
print(arraylist)
arraylist.add(4, 5)
print(arraylist)
arraylist.add(5, 6)
print(arraylist)

arraylist.remove(5)
print(arraylist)
arraylist.remove(2)
print(arraylist)
arraylist.remove(2)
print(arraylist)
# arraylist.remove(100)
# arraylist.add(20, 4)
# print(arraylist)
'''
