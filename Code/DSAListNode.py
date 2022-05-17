
class DSAListNode:
    def __init__(self, value, next, tail):
        self.value = value
        self.next = next
        self.tail = tail
    def getValue(self):
        return self.value
    def setValue(self, value):
        self.value = value
    def getNext(self):
        return self.next
    def setNext(self, next):
        self.next = next
    def getTail(self):
        return self.tail
    def setTail(self, tail):
        self.tail = tail
    