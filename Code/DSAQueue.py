import numpy as np
from DSALinkedList import DSALinkedList
from DSALinkedListIterator import DSALinkedListIterator
class DSAQueue(DSALinkedListIterator):
    def __init__(self):
        self.queue = DSALinkedList()
    def isEmpty(self):
        return(self.queue.isEmpty()) 
    # Using DSALinkedList get the first value from a linked list
    def peek(self):
        if(self.isEmpty() == False):
            return self.queue.peekFirst()
        else:
            raise Exception("Queue is empty")
    # Using DSALinkedList queue a value to a linked list
    def enqueue(self, value):
        return(self.queue.insertLast(value))
    # Using DSALinkedList dequeue a value from a linked list
    def dequeue(self):
        if(self.isEmpty() == False):
            return self.queue.removeLast()
        else:
            raise Exception("Queue is empty")