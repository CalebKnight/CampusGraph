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
from file import File
from menu import *
from CampusRoute import CampusRoute
class GraphFunctions:
    def __init__(self):
        self.file = None
        self.graph = None

    def loadFile(self):
        print("Enter the name of the file you would like to load:")
        fileName = input()
        while not os.path.isfile("Code/{}".format(fileName)):
            print("File not found. Please try again.")
            fileName = input()
        file = File("Code/{}".format(fileName))
        file.readFile()
        self.graph = file.fileContent
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

    def enterJourneyDetails():
        pass

    def generateRoutes(self):
        pass

    def displayRoutes(self):
        self.generateRoutes()
        pass

    def saveFile(self):
        choice = SaveMenu()
        if choice == "1":
            self.file.writeFileFromGraph(self.graph)
    
    
    

    # def createCampusRoute(self, operation):
    #     fromBuilding = getInput("label", "first building", operation)
    #     toBuilding = getInput("label", "second building", operation)
    #     distance = getInput("distance", "route", operation)
    #     security = getInput("security", "route", operation)
    #     barriers = getInput("barriers", "route", operation)
    #     campusRoute = CampusRoute(fromBuilding, toBuilding, distance, security, barriers)
    #     return(campusRoute)


def getInput(lookingFor, type, operation):
    print("Enter the {} of the {} you would like to {}:").format(lookingFor, type, operation)
    value = input()
    return(value)
        
