
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
    # Add vertex is simply inserting the vertex at the ends of verticeList
    # In this implementation of a graph vertices have very little information stored and so this can be done easily.
    # Value is optional.
    def addVertex(self, label, value = None):
        newVertex = DSAGraphVertex(label, value)
        self.verticesList.insertLast(newVertex)

    # The edge is more complicated than a vertex as it stores information about linkage and requires editing of existing vertices when added.
    # This is done by using the fromVertex and toVertex labels to find the vertices and then adding these vertices to an adjacency list by looping through existing vertices.
    # In order to determine if vertices need to be added with the edge the list needs to be looped through to find out if the vertices exist already. 
    # A less user friendly approach could be to force the adding of vertices then allowing edges to be added once they exist.
    def addEdge(self, fromVertex, toVertex, label, value):
        newEdge = DSAGraphEdge(fromVertex, toVertex, label, value)
        self.edges.insertLast(newEdge)
        fromVertexFound = False
        toVertexFound = False
        for vertex in self.verticesList:
            if(vertex.getLabel() == fromVertex):
                fromVertexFound = True
            if(vertex.getLabel() == toVertex):
                toVertexFound = True
        if(not fromVertexFound):
            self.addVertex(fromVertex)
        if(not toVertexFound):
            self.addVertex(toVertex)
        for vertex in self.verticesList:
            if(vertex.getLabel() == fromVertex and not (self.getVertex(toVertex) in vertex.getAdjacent())):
                vertex.addAdjacent(self.getVertex(toVertex))
            elif(vertex.getLabel() == toVertex and not (self.getVertex(fromVertex) in vertex.getAdjacent())):
                vertex.addAdjacent(self.getVertex(fromVertex))
        
    # Checks if the graph contains a vertex with a matching label to the input and returns true if it does.
    def hasVertex(self, label):
        for currentNode in self.verticesList:
            if(currentNode.getLabel() == label):
                return True
        return False
    # Gets an integer count of verticesList by using getLength() from a linked list.
    def getVertexCount(self):
        return self.verticesList.getLength()
    # Gets an integer count of edges by using getLength() from a linked list.
    def getEdgeCount(self):
        return self.edges.getLength()
    # Gets node object from the verticesList linked list if it has a matching label.
    # None is returned if it is not found to ensure the function that might call this knows that it does not exist.
    def getVertex(self, label):
        currentNode = self.verticesList.head
        for currentNode in self.verticesList:
            if(currentNode.getLabel() == label):
                return currentNode
        return None
    # Gets node object from the edges linked list if it has a matching label.
    # None is returned if it is not found to ensure the function that might call this knows that it does not exist.
    def getEdge(self, label):
        currentNode = self.edges.head
        for currentNode in self.edges:
            if(currentNode.getLabel() == label):
                return currentNode
        return None
    # Returns linked list stored in vertex for adjacent vertices to the inputted vertice.
    # Edges do not have an adjacent function as it is not required for their functionality.
    # None is returned if it is not found to ensure the function that might call this knows that it does not exist.
    def getAdjacent(self, label):
        for currentNode in self.verticesList:
            if(currentNode.getLabel() == label):
                return currentNode.getAdjacent()
        return None
    
    # Remove vertex with matching label from verticesList then search through edges to make sure an edge doesn't contain a vertex with the same label.
    # If the edge does remove it as it points to nothing now.
    def removeVertex(self, label):
        for vertex in self.verticesList:
            if(vertex.getLabel() == label):
                self.verticesList.remove(vertex)
        for edge in self.edges:
            if(label in edge.getLabel()):
                self.edges.remove(edge)

    # Remove the edge from the edges list using linked list functionality. 
    # Doesn't need to alter the vertices as the edge can be removed from the vertices adjacency list.
    def removeEdge(self, label):
        for currentNode in self.edges:
            if(currentNode.getLabel() == label):
                self.edges.remove(currentNode)
        for currentNode in self.verticesList:
            for vertice in currentNode.getAdjacent():
                if( vertice.getLabel() in label):
                    # Should be a function in the vertex class to remove the edge from the adjacency list.
                    # This implementation also works.
                    currentNode.getAdjacent().remove(vertice)
                
    # Update a given vertex with a new label.
    # Could have additional functionality to update a value but for this program it is unnecessary.
    # Also need to loop through edges to make sure that if they contain the previous label it is replaced.
    def updateVertex(self, previousLabel, label):
        for vertex in self.verticesList:
            if(vertex.getLabel() == previousLabel):
                vertex.setLabel(label)
        for edge in self.edges:
            if(previousLabel == edge.getTo()):
                edge.setTo(self._updateVertexInEdge(label))
            elif(previousLabel == edge.getFrom()):
                edge.setFrom(self._updateVertexInEdge(label))
    
    # Update the label in an edge and it's value.
    # Calls helper function updateVertexInEdge to handle updating any vertexes that contain the previous labels.
    def updateEdge(self, previousLabel, label, value):
        for edge in self.edges:
                if(edge.getLabel() == previousLabel):
                    edge.setLabel(label)
                    edge.setValue(value)
                    edge.setTo(self._updateVertexInEdge(label.split(",")[1]))
    
    # Helper function to update the label in a vertex from a change in an edge or vertex.
    def _updateVertexInEdge(self, label):
        for vertex in self.verticesList:
            if(vertex.getLabel() == label):
                vertex.setLabel(label)
                return vertex
    # Displays a list representation of a graph with vertices and their connections.  
    def displayAsList(self):
        for currentNode in self.verticesList:
            adjacent = currentNode.getAdjacent()
            print(adjacent.peekFirst().getLabel(), end="\t<-\t")
            print(currentNode.getLabel(), end="")
            print("\t->\t" + adjacent.peekLast().getLabel() + "\n")
           
    # Displays the graph as a matrix of vertices*vertices size. A number of 1 indicates it is directed, 2 indicates it is bi-directional and 0 indicates it is not connected.
    # The algorithm has efficiency problems as it loops through the entirety of edges and then performs a double for loop. 
    # Big O notation above n^2
    # For the purposes of this program it does not necessarily need to be efficient as the graphs utilised are generally small enough to not cause problems.
    # The exception to this is when vertices begin reaching into the 100s were it gets too slow to be utilised properly.
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
                    if(labels[i] == fromVertex and labels[j] == toVertex):
                        matrix[i][j] += 1
                    elif(labels[i] == toVertex and labels[j] == fromVertex):
                        matrix[i][j] += 1
        print("\t\t", end="")
        for idx, i in enumerate(matrix):
            print(labels[idx], end=" ")
        print()
        for idx, i in enumerate(matrix):
            print(labels[idx], end="\t")
            print(i)

    # Searches through a graph to find a path between two vertices. 
    # This implementation also adds branches leading towards the target and may go further. 
    # The output is sanitised elsewhere to find an actual path.
    def depthFirstSearch(self, label, target):
        self.clearVisited()
        T = DSAQueue()
        S = DSAStack()
        v = self.getVertex(label)
        if v != None:
            v.setVisited()
            S.push(v)
            while(not S.isEmpty()):
                for w in v.getAdjacent():
                    if(w.getVisited() == False):
                        edge = self.getEdge(v.getLabel() + "," + w.getLabel())
                        if edge != None:
                            T.enqueue(edge)
                            w.setVisited()
                            S.push(w)
                v = S.pop()
        return T

    # Clears all vertices of being visited to allow depthFirstSearch to work multiple times.
    def clearVisited(self):
        for currentNode in self.verticesList:
            currentNode.clearVisited()
        
        

        