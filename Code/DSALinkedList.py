from DSAListNode import DSAListNode
from DSALinkedListIterator import DSALinkedListIterator
class DSALinkedList(DSALinkedListIterator): 
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        if(self.head == None):
            return True
        else:
            return False
    def isFull(): 
        pass
        # Not sure why you would need this as lists can be as big as needed
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
    def peekFirst(self): 
        if(self.isEmpty() == True):
            raise Exception("List is empty")
        else:
            return self.head.getValue()
    def peekLast(self): 
        if(self.isEmpty() == True):
            raise Exception("List is empty")
        else:
            currentNode = self.head
            while(currentNode.getNext() != None):
                currentNode = currentNode.getNext()
            return currentNode.getValue()
    def removeFirst(self):
        if(self.isEmpty() == True):
            raise Exception("List is empty")
        else:
            currentNode = self.head
            currentNode.setTail(None)
            self.head = currentNode.getNext()
            return currentNode.getValue()
    def removeLast(self):
        if(self.isEmpty() == True):
            raise Exception("List is empty")
        elif(self.head == self.tail):
            copy = self.head
            self.head = None
            self.tail = None
            return copy.getValue()
        else:
            copy = self.tail
            self.tail = self.tail.getTail()
            self.tail.setNext(None)
            return copy.getValue()
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
        
            
                    
    def getLength(self):
        if(self.isEmpty() == True):
            return 0
        else:
            i = 0
            for currentNode in self:
                i+=1
        
        return i
    

    
            


        
    