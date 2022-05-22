import numpy as np
from DSALinkedList import DSALinkedList 
from DSALinkedListIterator import DSALinkedListIterator
# This class has been sourced from a practical submission by myself (Caleb Knight), Practical 4, (2022).
class DSAStack(DSALinkedListIterator): 
    def __init__(self):
        self.stack = DSALinkedList()
    def isEmpty(self):
        return(self.stack.isEmpty())
    # Using DSALinkedList push a value to the end of a linked list
    def push(self, value):
        try:
            self.stack.insertLast(value)
        except:
            raise Exception("Cannot push to stack")
    # Using DSALinkedList pop a value from the end of a linked list
    def pop(self):
        try:
            return(self.stack.removeLast())
        except Exception as e:
            print(e)
            raise Exception("Cannot pop from stack")
    # Using DSALinkedList get the last value from a linked list
    def top(self):
        if(self.stack.isEmpty() == False):
            return self.stack.peekLast()
        else:
            raise Exception("Stack is empty")
