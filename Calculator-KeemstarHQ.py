import numpy as np
import ArrayStack
import ChainedHashTable
import DLList
import BinaryTree
import operator


class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def print_expression(self, s: str) -> str:
        t = ''
        operands = {}
        operators = {}
        
        if self.matched_expression(s) == True:
            for i in s:
                if self.dict.find(i) != None:
                    operands[i] = i
                else:
                    operators[i] = i
 
            for i in s:
                if i in operators:
                    t += i
                elif i in operands:
                    t += f"{self.dict.find(i)}"
            return t
        return False
        

    def matched_expression(self, s: str) -> bool:
        stack = ArrayStack.ArrayStack()
        for i in range(len(s)):
            char = s[i]

            if char == '(':
                stack.push(char)
            elif char == ')':
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()

        if stack.n == 0:
            return True
        else:
            return False

    def build_parse_tree(self, exp: str) -> str:
        t = BinaryTree.BinaryTree()
        u = t.Node('')
        t.r = u
        for token in exp:
            if u == None:
                u = t.Node('')
            if token == '(':
                u.insert_left()
                u = u.left
            elif token in ["+", "-", "/", "*"]:
                u.x = token
                u.insert_right()
                u = u.right
            elif token == ")":
                if u.parent != None:
                    u = u.parent
                
            elif token == "":
                pass
            else:
                u.x = token
                u = u.parent
                
        # print(t)
        return t
    

    def _evaluate(self, u):

        if u is None:
            return 0
        
        if u.left is None and u.right is None:
            return self.dict.find(u.x)
        
        leftSum = self._evaluate(u.left)
        rightSum = self._evaluate(u.right)
        
        if u.x == "+":
            # print(f"left: {u.left.x}")
            # print(f"u.x: {u.x}")
            # print(f"right: {u.right.x}")
            # print(leftSum + rightSum)
            return leftSum + rightSum
        elif u.x == "-":
            # print(f"left: {u.left.x}")
            # print(f"u.x: {u.x}")
            # print(f"right: {u.right.x}")
            # print(leftSum - rightSum)
            return leftSum - rightSum
        elif u.x == "*":
            # print(f"left: {u.left.x}")
            # print(f"u.x: {u.x}")
            # print(f"right: {u.right.x}")
            # print(leftSum * rightSum)
            return leftSum * rightSum
        else:
            # print(f"left: {u.left.x}")
            # print(f"u.x: {u.x}")
            # print(f"right: {u.right.x}")
            # print(leftSum / rightSum)
            return leftSum / rightSum
 
        
        

    def evaluate(self, exp):  
        try:
            parseTree = self.build_parse_tree(exp)
            return self._evaluate(parseTree.r)
        except:
            return 0
        




# c = Calculator()
# c.set_variable("a", 1.3)
# c.set_variable("b", 2.1)
# c.set_variable("c", 2.2)
# c.set_variable("d", 3.0)
# print(c.evaluate("((a*b)+(c*d))"))

