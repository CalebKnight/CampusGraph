import numpy as np
from DSALinkedList import DSALinkedList
from DSALinkedListIterator import DSALinkedListIterator
class DSAQueue(DSALinkedListIterator):
    def __init__(self):
        self.queue = DSALinkedList()
        self.head = self.queue.head
    def isEmpty(self):
        return(self.queue.isEmpty()) 
    def peek(self):
        if(self.isEmpty() == False):
            return self.queue.peekFirst()
        else:
            raise Exception("Queue is empty")
    def enqueue(self, value):
        # Using DSALinkedList queue a value to a linked list
        return(self.queue.insertLast(value))
    def dequeue(self):
        if(self.isEmpty() == False):
            return self.queue.removeLast()
        else:
            raise Exception("Queue is empty")