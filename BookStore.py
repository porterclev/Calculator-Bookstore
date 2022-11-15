import algorithms
import Book
import SortableBook
import ArrayQueue
import ArrayList
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
import AdjacencyList
import time
import DLList
import MaxStack


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''
    def __init__(self):
        self.bookCatalog = DLList.DLList()
        self.shoppingCart = MaxStack.MaxStack()
        self.indexKey = ChainedHashTable.ChainedHashTable()
        self.indexSortedPrefix = BinarySearchTree.BinarySearchTree()
        self.bookSortedCatalog = ArrayList.ArrayList()
        self.similaGraph = AdjacencyList.AdjacencyList(0)

    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        with open(fileName,encoding='utf8') as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                b = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(b)
            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

        return self.bookCatalog.size()

    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the shopping cart the book with index i
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.push(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def addBookByKey(self, s: str):
        '''
        addBookByIndex: Inserts into the shopping cart the book with key s
        input: 
            s: key string    
        '''
        pass

    def addBookByPrefix(self, s: str):
        '''
        addBookByPrefix: Inserts into the shopping cart the book with prefix s
        input: 
            s: Prefix    
        '''
        # Validating the index. Otherwise it  crashes
        pass

    def pathLength(self, s1: str, s2: str):
        i = self.indexKey.find(s1)
        j = self.indexKey.find(s2)
        distance = self.similaGraph.distance(i, j)
        print(f"{s1} and {s2} are at distance {distance}")
        return distance

    def searchBookByInfix(self, infix: str) -> int:
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string 
        returns: 
            the number of books that contains infix in its title   
        '''
        numberOfBooks = 0
        for i in range(0, self.bookCatalog.size()):
            if infix in self.bookCatalog.get(i).title:
                if numberOfBooks == 50:
                    return numberOfBooks

                print(self.bookCatalog.get(i))
                numberOfBooks += 1
        return numberOfBooks

    def sortUsingMergeSort(self):
        algorithms.merge_sort(self.bookSortedCatalog)

    def sortUsingQuickSort(self):
        algorithms.quick_sort(self.bookSortedCatalog)

    def searchBookUsingBinarySearch(self, prefix: str):
        s = SortableBook.SortableBook(0, prefix, "", 0, None)
        j = algorithms.binary_search(self.bookSortedCatalog, self.bookSortedCatalog.size(), s)
        print(self.bookSortedCatalog[j])

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.pop()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")
            return u




