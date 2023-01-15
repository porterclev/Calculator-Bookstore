from Interfaces import Set
from DLList import DLList
import numpy as np


class ChainedHashTable(Set):
    class Node():
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, dtype=DLList):
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2**self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=np.object_)
        for i in range(n):
            t[i] = self.dtype()
        return t

    def hash(self, key: int) -> int:
        return (self.z * hash(key)) % (2**self.w) >> (self.w - self.d)

    def size(self) -> int:
        return self.n

    def find(self, key: object) -> object:
        l = self.t[self.hash(key)]
        for i in range(len(l)):
            # print(f"l[{i}]: {l[i].value}")
            # print(f"l[{i}]: {l[i].key}")
            # print(f"key: {key}")
            if l[i].key == key:
                return l[i].value
        return None

        # for y in self.t[self.hash(key)]:
        # print(f"y.value: {y.value}")
        # print(f"y.key: {y.key}")
        # print(f"key: {key}")
        #     if key == y.key:
        #         return y.value
        # return None

    def add(self, key: object, value: object):
        if self.find(key) != None:
            return False

        if self.n + 1 > len(self.t):
            self.resize()

        u = self.Node(key, value)
        # print(f"adding ({u.key},{u.value}) at {self.hash(key)} using key: {key}")

        self.t[self.hash(key)].append(u)
        self.n += 1
        return True

    def remove(self, key: int) -> object:
        # l = self.t[self.hash(key)]

        # for y in l:
        #     if y.key == key:
        #         l.remove(y.key)
        #         # print(f"removing ({y.key},{y.value})")
        #         self.n-=1

        #         if 3 * self.n < len(self.t):
        #             self.resize()

        #         return y
        # return None
        for i in range(self.t[self.hash(key)].size()):

            if self.t[self.hash(key)].get(i).key == key:

                self.t[self.hash(key)].remove(i)
                self.n -= 1

                if 3 * self.n < len(self.t):
                    self.resize()
                return True
        return False

    def resize(self):
        # print("called resize")
        if self.n == len(self.t):
            # print("+")
            self.d += 1
        else:
            # print("-")
            self.d -= 1

        a = self.alloc_table(2**self.d)
        for j in range(len(self.t)):
            for i in range(self.t[j].size()):
                # a[self.hash(self.t[j].get(i).key)].add(self.t[j].get(i).key, self.t[j].get(i))
                a[self.hash(self.t[j].get(i).key)].append(self.t[j].get(i))
        self.t = a

    def __str__(self):
        s = "["
        for i in range(len(self.t)):
            for j in range(len(self.t[i])):
                k = self.t[i][j]
                s += str(k.key)
                s += ":"
                s += str(k.value)
                s += ";"
        return s + "]"

# cht = ChainedHashTable()
# cht.add(1, "first")
# cht.add(2, "second")
# cht.add(3, "fourth")
# print(cht.size())
# print(cht.find(3))
# cht.remove(3)
# print(cht.size())
# print(cht.find(3))
# cht.add(3,"third")
# cht.add(4,"fourth")
# cht.add(5,"fifth")
# print(cht.size())
# print(cht.find(3))
