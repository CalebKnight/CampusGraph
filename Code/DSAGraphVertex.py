from DSALinkedList import DSALinkedList
class DSAGraphVertex:
    def __init__(self, label, value = None):
        self.label = label
        self.value = value
        self.links = DSALinkedList()
        self.visited = False
    def getLabel(self):
        return self.label
    def getValue(self):
        return self.value
    def getAdjacent(self):
        return self.links
    def addAdjacent(self, label):
        self.links.insertLast(label)
    def setLabel(self, label):
        self.label = label
    def setValue(self, value):
        self.value = value
    def setVisited(self):
        self.visited = True
    def clearVisited(self):
        self.visited = False
    def getVisited(self):
        return self.visited
    def toString(self):
        return str(self.label) + " " + str(self.value)
    
    
