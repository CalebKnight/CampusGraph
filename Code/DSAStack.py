import numpy as np
from DSALinkedList import DSALinkedList 
from DSALinkedListIterator import DSALinkedListIterator
class DSAStack(DSALinkedListIterator): 
    def __init__(self):
        self.stack = DSALinkedList()
    def isEmpty(self):
        return(self.stack.isEmpty())
    def push(self, value):
        try:
            self.stack.insertLast(value)
        except:
            raise Exception("Cannot push to stack")
    def pop(self):
        try:
            return(self.stack.removeLast())
        except Exception as e:
            print(e)
            raise Exception("Cannot pop from stack")
    def top(self):
        if(self.stack.isEmpty() == False):
            return self.stack.peekLast()
        else:
            raise Exception("Stack is empty")
