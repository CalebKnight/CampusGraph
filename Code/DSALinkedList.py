from DSAListNode import DSAListNode
from DSALinkedListIterator import DSALinkedListIterator

# This class has been sourced from a practical submission by myself (Caleb Knight), Practical 4, (2022).
class DSALinkedList(DSALinkedListIterator): 
    def __init__(self):
        self.head = None
        self.tail = None
    # Checks if list is empty
    # Would prefer to use two return statements however this violates the coding standard.
    def isEmpty(self):
        empty = False
        if(self.head == None):
            empty = True
        else:
            empty = False
        return empty

    # Inserts a value at the start of the linked list. 
    # Useful for queues specifically the enqueue method.
    def insertFirst(self, value): 
        newNd = DSAListNode(value, None, None)
        if(self.isEmpty() == True):
            self.head = newNd
            self.tail = newNd
        elif(self.head == self.tail):
            newNd.setNext(self.head)
            self.tail = self.head
            self.head = newNd
        else:
            newNd.setNext(self.head)
            self.head = newNd
    # Inserts a value at the end of the linked list.
    # Useful for stacks specifically the push method.
    def insertLast(self, value): 
        newNd = DSAListNode(value, None, None)
        if(self.isEmpty() == True):
            self.head = newNd
            self.tail = newNd
        elif(self.head == self.tail):
            newNd.setTail(self.head)
            self.head.setNext(newNd)
            self.tail = newNd
        else:
            currentNode = self.head
            while(currentNode.getNext() != None):
                currentNode = currentNode.getNext()
            currentNode.setNext(newNd)
            newNd.setTail(currentNode)
            self.tail = newNd
    # Gets first value in a linked list. 
    def peekFirst(self): 
        if(self.isEmpty() == True):
            raise Exception("List is empty")
        else:
            return self.head.getValue()
    # Gets last value in a linked list. 
    def peekLast(self): 
        if(self.isEmpty() == True):
            raise Exception("List is empty")
        else:
            currentNode = self.head
            while(currentNode.getNext() != None):
                currentNode = currentNode.getNext()
            return currentNode.getValue()
    # Takes the first value in a linked list makes a copy and removes it. 
    # Useful for queues specifically the dequeue method.
    def removeFirst(self):
        if(self.isEmpty() == True):
            raise Exception("List is empty")
        else:
            currentNode = self.head
            currentNode.setTail(None)
            self.head = currentNode.getNext()
            return currentNode.getValue()
    # Takes the last value in a linked list makes a copy and removes it.
    # Useful for stacks specifically the pop method.
    def removeLast(self):
        if(self.isEmpty() == True):
            raise Exception("List is empty")
        elif(self.head == self.tail):
            copy = self.head
            self.head = None
            self.tail = None
        else:
            copy = self.tail
            self.tail = self.tail.getTail()
            self.tail.setNext(None)
        return copy.getValue()
            
        
    
    # This method is used to remove values in the middle of a linked list. 
    # It is useful for removing nodes in a graph.
    # Can likely replace the other remove methods however keeping them makes the code for queues and stacks more readable and efficient.
    def remove(self, value):
        if(self.isEmpty() == True):
            raise Exception("List is empty")
        if self.head == self.tail:
            if self.head.getValue() == value:
                self.head = None
                self.tail = None
        elif self.head.getValue() == value:
            self.head = self.head.getNext()
            self.head.setTail(None)
        elif self.tail.getValue() == value:
            self.tail = self.tail.getTail()
            self.tail.setNext(None)
        else:
            currentNode = self.head
            while currentNode.getNext() != None:
                if currentNode.getNext().getValue() == value:
                    currentNode.setNext(currentNode.getNext().getNext())
                    currentNode.getNext().setTail(currentNode)
                    return
                currentNode = currentNode.getNext()
            raise Exception("Value not found")
        
    # Loop through a linked list and count how many values are inside. 
    # Could be kept track of through a class field of count as an alternative.
    def getLength(self):
        i = 0
        if(self.isEmpty() == True):
            pass
        else:
            for currentNode in self:
                i+=1
        return i
    

    
            


        
    