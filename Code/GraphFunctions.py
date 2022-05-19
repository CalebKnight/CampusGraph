# "Load input file"
# Node operations (find, insert, delete, update)
# Edge operations (find, add, remove, update)
# Parameter tweaks (adjust mapping of codes to impacts, see sample input file)
# Display graph (weighted adjacency matrix, option to save)
# Display world (your choice of representation, does not need to be graphical, should include counts of features, option to save)
# Enter journey details
# Generate routes
# Display routes (ranked, option to save)
# Save network
import os
import numpy as np
from DSAQueue import DSAQueue
from file import File
from menu import *
from CampusRoute import CampusRoute
class GraphFunctions:
    def __init__(self):
        self.file = None
        self.graph = None
        self.routes = np.zeros(0, dtype=object)
        journey = None

    def loadFile(self):
        print("Enter the name of the file you would like to load:")
        fileName = input()
        while not os.path.isfile("Code/{}".format(fileName)):
            print("File not found. Please try again.")
            fileName = input()
        file = File("Code/{}".format(fileName))
        file.readGraph()
        self.graph = file.graph
        self.journey = file.journey
        return(file)

    def nodeOperations(self):
        print("\nHow would you like to edit the node/s?\n")
        choice = NodeMenu()
        if choice == 1:
            vertexName = getInput("label", "vertex", "find")
            self.graph.getVertex(vertexName)
        elif choice == 2:
            label = getInput("label", "vertex", "insert")
            value = getInput("value", "vertex", "insert")
            self.graph.addVertex(label, value)
        elif choice == 3:
            label = getInput("label", "vertex", "delete")
            self.graph.removeVertex(label)
        elif choice == 4:
            label = getInput("label", "vertex", "update")
            newLabel = getInput("label", "vertex", "update")
            self.graph.updateVertex(label, newLabel)
        else:
            print("Invalid choice. Please try again.")
    
    def edgeOperations(self):
        print("\nHow would you like to edit the edge/s?\n")
        choice = EdgeMenu()
        if choice == 1:
            fromBuilding = getInput("label", "first building", "find")
            toBuilding = getInput("label", "second building", "find")
            self.graph.getEdge(fromBuilding, toBuilding)
        elif choice == 2:
            campusRoute = self.createCampusRoute("add")
            self.graph.addEdge(campusRoute)
        elif choice == 3:
            deletionLabel = getInput("label", "edge", "delete")
            self.graph.removeEdge(deletionLabel)
        elif choice == 4:
            updateLabel = getInput("previous label", "edge", "update")
            newLabel = campusRoute.fromBuilding + "," + campusRoute.toBuilding
            self.graph.updateEdge(updateLabel, newLabel, campusRoute)
        else:
            print("Invalid choice. Please try again.")

    def editCampusRoute(self):
        label = getInput("label", "edge", "update")
        edge = self.graph.getEdge(label)
        campusRoute = edge.getValue()
        campusRoute.distance = getInput("distance", "route", "update")
        campusRoute.security = getInput("security", "route", "update")
        campusRoute.barriers = getInput("barriers", "route", "update")
        self.graph.updateEdge(label, label, campusRoute)

    def displayGraph(self):
        self.graph.displayAsMatrix()
        if SaveMenu() == "1":
            self.file.writeFileFromGraph(self.graph)

    def DisplayGraph(self):
        self.graph.displayAsMatrix()

    def DisplayWorld(self):
        pass

    def enterJourneyDetails(self):
        print("\nPossible targets and start points are:\n")
        for vertex in self.graph.verticesList:
            print(vertex.getLabel())
        startPoint = getInput("start point", "journey", "enter")
        target = getInput("target point", "journey", "enter")
        # Lowercase so that Stairs is the same as stairs
        barriers = getInput("barriers", "journey", "enter").lower()
        self.journey = CampusRoute(startPoint, target, None, None, barriers)

    def generateRoutes(self):
        if self.journey == None:
            self.enterJourneyDetails()
        startPoint, target, barriers = self.journey.fromBuilding, self.journey.toBuilding, self.journey.barriers
        idx = 0
        routes = np.zeros(self.graph.getEdgeCount(), dtype=object)
        visited = self.graph.depthFirstSearch(startPoint, target)
        currentNode = visited.queue.tail
        while currentNode != None:
            # If the current node points to the target edge then we have found a path that follows the main route
            if(currentNode.getValue().getTo() == target):
                if self._isPathBlocked(currentNode.getValue().getValue(), barriers) == False or len(barriers) < 2:                  
                    routes[idx] = currentNode.getValue()
                    target = currentNode.getValue().getFrom()
                    idx += 1
            currentNode = currentNode.getTail()
        self.routes = self._invertArray(routes)
        self.routes = self._shuffleArrayDown(self.routes)

    def _isPathBlocked(self, path, barriers):
        if path.barriers == barriers or barriers in path.barriers:
            return True
        return False
            
    def _invertArray(self, array):
        invertedArray = np.zeros(len(array), dtype=object)
        for i in range(len(array)):
            invertedArray[i] = array[len(array) - i - 1]
        return(invertedArray)

    def _shuffleArrayDown(self, array):
        shuffledArray = np.zeros(len(array), dtype=object)
        shuffleIdx = 0
        for i in array:
            if i != 0:
                shuffledArray[shuffleIdx] = i
                shuffleIdx += 1
        return(shuffledArray)


    def displayRoutes(self):
        if len(self.routes) == 0:
            self.generateRoutes()
        for path in self.routes:
            if path != None and path != 0:
                print("\nPath\n")
                print(path.getLabel().replace(",", " -> "))

    def saveFile(self):
        choice = SaveMenu()
        if choice == "1":
            self.file.writeFileFromGraph(self.graph)


def getInput(lookingFor, type, operation):
    print("Enter the {} of the {} you would like to {}:".format(lookingFor, type, operation))
    value = input()
    return(value)
        
