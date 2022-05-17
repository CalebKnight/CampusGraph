class DSAGraphEdge:
    fromVertex = None
    toVertex = None
    label = None
    value = None
    def __init__(self, fromVertex, toVertex, label, value):
        self.fromVertex = fromVertex
        self.toVertex = toVertex
        self.label = label
        self.value = value
    def getLabel(self):
        return self.label
    def getValue(self):
        return self.value
    def getFrom(self):
        return self.fromVertex
    def getTo(self):
        return self.toVertex
    def setValue(self, value):
        self.value = value
    def setLabel(self, label):
        self.label = label
    def setFrom(self, fromVertex):
        self.fromVertex = fromVertex
    def setTo(self, toVertex):
        self.toVertex = toVertex

    def isDirected(self):
        if(self.fromVertex == self.toVertex):
            return False
        return True
    def toString(self):
        return str(self.fromVertex) + " " + str(self.toVertex) + " " + str(self.label) + " " + str(self.value)