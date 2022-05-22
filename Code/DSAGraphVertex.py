from DSALinkedList import DSALinkedList

# The structure and methods of this class are adapted from pseudocode from Curtin University, Lecture 6, (2022), pg. 53.
# No code algorithms have been explicitly copied from this source.
# Some of this code has been previously submitted in a practical by myself.

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
    
    
