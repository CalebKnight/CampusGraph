
import numpy as np
from DSAGraphEdge import DSAGraphEdge
from DSAGraphVertex import DSAGraphVertex
from DSALinkedList import DSALinkedList
from DSAQueue import DSAQueue
from DSAStack import DSAStack
class DSAGraph:
    def __init__(self):
       self.verticesList = DSALinkedList()
       self.edges = DSALinkedList()
    def addVertex(self, label, value = None):
        newVertex = DSAGraphVertex(label, value)
        self.verticesList.insertLast(newVertex)
    def addEdge(self, fromVertex, toVertex, label, value):
        newEdge = DSAGraphEdge(fromVertex, toVertex, label, value)
        self.edges.insertLast(newEdge)
        # Linked list iterator returns value
        for vertex in self.verticesList:
            if(vertex.getLabel() == fromVertex and not (self.getVertex(toVertex) in vertex.getAdjacent())):
                vertex.addAdjacent(self.getVertex(toVertex))
            elif(vertex.getLabel() == toVertex and not (self.getVertex(fromVertex) in vertex.getAdjacent())):
                vertex.addAdjacent(self.getVertex(fromVertex))
        

    def hasVertex(self, label):
        for currentNode in self.verticesList:
            if(currentNode.getLabel() == label):
                return True
        return False
    def getVertexCount(self):
        return self.verticesList.getLength()
    def getEdgeCount(self):
        return self.edges.getLength()
    def getVertex(self, label):
        currentNode = self.verticesList.head
        for currentNode in self.verticesList:
            if(currentNode.getLabel() == label):
                return currentNode
        return None
    def getEdge(self, label):
        currentNode = self.edges.head
        for currentNode in self.edges:
            if(currentNode.getLabel() == label):
                return currentNode
        return None
    def getAdjacent(self, label):
        for currentNode in self.verticesList:
            if(currentNode.getLabel() == label):
                return currentNode.getAdjacent()
        return None
    
    def removeVertex(self, label):
        for vertex in self.verticesList:
            if(vertex.getLabel() == label):
                self.verticesList.remove(vertex)
        for edge in self.edges:
            if(label in edge.getLabel()):
                self.edges.remove(edge)
        
    def removeEdge(self, label):
        for currentNode in self.edges:
            if(currentNode.getLabel() == label):
                self.edges.remove(currentNode)
    
    def updateVertex(self, previousLabel, label):
        for vertex in self.verticesList:
            if(vertex.getLabel() == previousLabel):
                vertex.setLabel(label)
        for edge in self.edges:
            if(previousLabel == edge.getTo()):
                edge.setTo(self._updateVertexInEdge(label))
            elif(previousLabel == edge.getFrom()):
                edge.setFrom(self._updateVertexInEdge(label))
               
    def updateEdge(self, previousLabel, label, value):
        for edge in self.edges:
                if(edge.getLabel() == previousLabel):
                    edge.setLabel(label)
                    edge.setValue(value)
                    edge.setTo(self._updateVertexInEdge(label.split(",")[1]))
       
    def _updateVertexInEdge(self, label):
        for vertex in self.verticesList:
            if(vertex.getLabel() == label):
                vertex.setLabel(label)
                return vertex
            
    # def displayAsList(self):
    #     for currentNode in self.verticesList:
    #         print(currentNode.toString())
    #     for currentNode in self.edges:
    #         print(currentNode.getLabel())
    def displayAsMatrix(self):
        matrix = np.zeros((self.getVertexCount(), self.getVertexCount()))
        labels = np.zeros(self.getVertexCount(), dtype=object)
        for idx, val in enumerate(self.verticesList):
            labels[idx] = val.getLabel()
        for currentNode in self.edges:
            fromVertex = currentNode.getFrom()
            toVertex = currentNode.getTo()
            for i in range(self.getVertexCount()):
                for j in range(self.getVertexCount()):
                    if(labels[i] == fromVertex.getLabel() and labels[j] == toVertex.getLabel()):
                        matrix[i][j] += 1
                    elif(labels[i] == toVertex.getLabel() and labels[j] == fromVertex.getLabel()):
                        matrix[i][j] += 1
        print("\t\t", end="")
        for idx, i in enumerate(matrix):
            print(labels[idx], end=" ")
        print()
        for idx, i in enumerate(matrix):
            print(labels[idx], end="\t")
            print(i)
    
    def depthFirstSearch(self, label, target):
        self.clearVisited()
        T = DSAQueue()
        S = DSAStack()
        v = self.getVertex(label)
        v.setVisited()
        S.push(v)
        while(not S.isEmpty()):
            for w in v.getAdjacent():
                if(w.getVisited() == False):
                    if(w.getLabel() == target):
                        T.enqueue(self.getEdge(v.getLabel() + "," + w.getLabel()))
                    else:
                        T.enqueue(self.getEdge(v.getLabel() + "," + w.getLabel()))
                        w.setVisited()
                        S.push(w)
            v = S.pop()
        return T

    def clearVisited(self):
        for currentNode in self.verticesList:
            currentNode.clearVisited()
        
        

        