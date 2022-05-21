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
        self.journey = None

    def loadFile(self):
        print("Enter the name of the file you would like to load for a graph:")
        fileName = input()
        while not os.path.isfile("Code/Maps/{}".format(fileName)):
            print("File not found. Please try again.")
            fileName = input()
        file = File("Code/Maps/{}".format(fileName))
        file.readGraph()
        self.graph = file.graph
        print("Enter the name of the file you would like to load for a journey:")
        fileName = input()
        while not os.path.isfile("Code/Maps/{}".format(fileName)):
            print("File not found. Please try again.")
            fileName = input()
        file = File("Code/Maps/{}".format(fileName))
        file.readJourney()
        self.journey = file.journey
        return(file)

    def nodeOperations(self):
        choice = nodeMenu()
        print("Current Vertices: \n")
        for vertex in self.graph.verticesList:
            print(vertex.getLabel())
        if choice == 1:
            vertexName = getInput("label", "vertex", "find")
            self.graph.getVertex(vertexName)
        elif choice == 2:
            label = getInput("label", "vertex", "insert", True)
            value = getInput("value", "vertex", "insert")
            self.graph.addVertex(label, value)
        elif choice == 3:
            label = getInput("label", "vertex", "delete", True)
            self.graph.removeVertex(label)
        elif choice == 4:
            label = getInput("previous label", "vertex", "update", True)
            newLabel = getInput("new label", "vertex", "update", True)
            self.graph.updateVertex(label, newLabel)
        else:
            print("Invalid choice. Please try again.")
    
    def edgeOperations(self):
        choice = edgeMenu()
        print("Current Edges: \n")
        for edge in self.graph.edges:
            print(edge.getLabel())
        if choice == 1:
            fromBuilding = getInput("label", "first building", "find", True)
            toBuilding = getInput("label", "second building", "find", True)
            self.graph.getEdge(fromBuilding, toBuilding)
        elif choice == 2:
            campusRoute = self.createCampusRoute()
            self.graph.addEdge(campusRoute.fromBuilding, campusRoute.toBuilding, campusRoute.fromBuilding + "," + campusRoute.toBuilding, campusRoute)
        elif choice == 3:
            deletionLabel = getInput("label", "edge", "delete", True)
            self.graph.removeEdge(deletionLabel)
        elif choice == 4:
            previousLabel = getInput("previous label", "edge", "update", True)
            campusRoute = self.createCampusRoute()
            self.graph.updateEdge(previousLabel, campusRoute.fromBuilding + "," + campusRoute.toBuilding, campusRoute)
        else:
            print("Invalid choice. Please try again.")

    def createCampusRoute(self):
        fromBuilding = getInput("label", "first building", "add", True)
        toBuilding = getInput("label", "second building", "add", True)
        distance = getInput("distance", "route", "add")
        distance = self._isDistanceEmpty(distance)
        security = getInput("security", "route", "add")
        barriers = getInput("barriers", "route", "add")
        return CampusRoute(fromBuilding, toBuilding, distance, security, barriers)
    
    def editCampusRoute(self):
        label = getInput("label", "edge", "update", True)
        edge = self.graph.getEdge(label)
        campusRoute = edge.getValue()
        campusRoute.distance = getInput("distance", "route", "update")
        distance = self._isDistanceEmpty(distance)
        distance = "D:" + distance
        campusRoute.security = getInput("security", "route", "update")
        campusRoute.barriers = getInput("barriers", "route", "update")
        self.graph.updateEdge(label, label, campusRoute)

    def _isDistanceEmpty(self, distance):
        if distance == "" or len(distance) < 1:
            return ""
        else:
            return distance

    def displayGraph(self):
        self.graph.displayAsMatrix()
        if saveMenu() == "1":
            self.file.writeFileFromGraph(self.graph)

    def DisplayGraph(self):
        self.graph.displayAsMatrix()

    def DisplayWorld(self):
        pass

    def enterJourneyDetails(self):
        print("\nPossible targets and start points are:\n")
        for vertex in self.graph.verticesList:
            print(vertex.getLabel())
        startPoint = getInput("start point", "journey", "enter", True)
        target = getInput("target point", "journey", "enter", True)
        # Lowercase so that Stairs is the same as stairs
        barriers = getInput("barriers", "journey", "enter").lower()
        security = getInput("security", "journey", "enter")
        self.journey = CampusRoute(startPoint, target, None, security, barriers)

    def generateRoutes(self):
        if self.journey == None:
            self.enterJourneyDetails()
        startPoint, target, barriers, security = self.journey.fromBuilding, self.journey.toBuilding, self.journey.barriers, self.journey.security
        routes = np.zeros(self.graph.getEdgeCount(), dtype=object)
        visited = self.graph.depthFirstSearch(startPoint, target)
        routes[0] = self.generateRoute(visited, target, barriers, security)
        self.routes = routes

    def generateRoute(self, visited, target, barriers, security):
        route = np.zeros(self.graph.getEdgeCount(), dtype=object)
        currentNode = visited.queue.tail
        idx = 0
        while currentNode != None:
            # If the current node points to the target edge then we have found a path that follows the main route
            if(currentNode.getValue().getTo() == target):
                if self._isPathBlocked(currentNode.getValue().getValue(), barriers, security) == False:                
                    route[idx] = currentNode.getValue()
                    target = currentNode.getValue().getFrom()
                    idx += 1
            currentNode = currentNode.getTail()
        route = self._invertArray(route)
        route = self._shuffleArrayDown(route)
        return route


    def _isPathBlocked(self, path, barriers, security):
        if len(barriers) > 2 and (path.barriers == barriers or barriers in path.barriers):
            return True
        if len(security) > 2 and (security not in path.security):
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
        distance = 0
        for route in self.routes:
            # this is one of the only ways to check if int without firing an error at this stage as route is both an indexable array and a integer value
            if type(route) != int:
                for idx, path in  enumerate(route):
                    if path != 0:
                        print("\nStep {}\n".format(idx + 1))
                        print(path.getLabel().replace(",", " -> "))
                        if path.getValue().distance != '':
                            distance += float(path.getValue().distance.replace("D:", ""))   
        print("\nThe distance is: "+ str(distance) + "\n")

    def saveFile(self):
        choice = saveMenu()
        if self.file == None:
            self.file = File()
            self.file.fileName = getInput("file name", "file", "save")
            if(len(self.file.fileName.split(".txt")) < 2):
                self.file.fileName += ".txt"
            self.file.fileName = "Code/Maps/{}".format(self.file.fileName )
        if choice == 1:
            self.file.writeFileFromGraph(self.graph)


def getInput(lookingFor, type, operation, required = False):
    print("Enter the {} of the {} you would like to {}:".format(lookingFor, type, operation))
    value = input()
    if len(value) < 1 and required == True:
        print("Please input a value")
        return getInput(lookingFor, type, operation, True)
    return(value)
        
