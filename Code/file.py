import os
from DSAGraph import DSAGraph
from CampusRoute import CampusRoute
import sys
import numpy as np
import os
class File:
    def __init__(self, fileName = None):
        self.fileName = fileName
        self.graph = None
        self.journey = None

    # Reads a graph from a file by processing each line into an edge. 
    # Checks to ensure each line is not empty or a comment
    # Sets the classes graph variable to the graph read from the file
    def readGraph(self):
        graph = DSAGraph()
        with open(os.path.join(self.fileName), "r") as file:
            line = file.readline()
            # This check is only run on the first line as the file could be missing subsequent lines without being invalid
            if(line == "" or line == "\n"):
                print("File is empty")
                return
            while(line):
                line = line.split("\n")[0]
                line = line.split(" ")
                # print(line)
                if line == "\n" or line == "" or line == None or line == " " or line[0] == '#':
                    # Skip line if empty
                    line = file.readline()
                else:
                    # Process line converts the line into an edge and adds it to the graph
                    self._processLine(line[0], graph)
                    line = file.readline()
        file.close()
        self.graph = graph


    # Reads a journey from a file by processing each line into seperate parts of a journey object. 
    # It is assumed the files end line is the last value however it should handle the edge cases properly provided the file is valid
    # Sets the classes journey variable to the journey read from the file
    def readJourney(self):
        journey = CampusRoute(None, None, None, None, None)
        values = np.zeros(5, dtype=object)
        # Need an idx to keep track of the values as the program needs to know which value to assign the journey component to
        idx = 0
        with open(os.path.join(self.fileName), "r") as file:
            line = file.readline()
            if(line == "" or line == "\n"):
                print("File is empty")
                return
            while(line):
                line = line.split("\n")[0]
                line = line.split(" ")
                # print(line)
                if line == "\n" or line == "" or line == None or line == " " or line[0] == '#':
                    line = file.readline()
                else:
                    values[idx] = line[1]
                    idx += 1
                    line = file.readline()
        file.close()
        journey.fromBuilding = values[0]
        journey.toBuilding = values[1]
        journey.distance = values[2]
        journey.security = values[4]
        journey.barriers = values[3]
        self.journey = journey
        
    # Calls a helper function to convert each edge in a graph to a string and writes it in the exact same format as the input file however it only uses > and <> deliminators for the edge directions
    def writeFileFromGraph(self, graph):
        with open(os.path.join(self.fileName), "w") as file:
            for edge in graph.edges:
                line = self._edgeToString(edge, graph)
                file.write(line)
        file.close()

    # Writes routes from functions.routes to a file
    # Adds each path number before writing it to a file and then writes the path vertices to a file
    def writeRoutesToFile(self, routes):
        distance = 0
        with open(os.path.join(self.fileName), "w") as file:
            for i,route in enumerate(routes):
            # this is one of the only ways to check if int without firing an error at this stage as route is both an indexable array and a integer value
                if type(route) != int:
                    file.write("\nPath: " + str(i + 1) + "\n")
                    for path in  route:
                        if path != 0:
                            file.write(path.getLabel().replace(",", " -> "))
                            if path.getValue().distance != '':
                                distance += float(path.getValue().distance.replace("D:", ""))  
            file.write("\nDistance: " + str(distance))
        file.close()

    # Add an edge object to the graph using information from a file.
    # Uses deliminators to determine direction of the edge.
    def appendGraph(self, graph, route):
        if(graph.getVertex(route.fromBuilding) == None):
            graph.addVertex(route.fromBuilding)
        if(graph.getVertex(route.toBuilding) == None):
            graph.addVertex(route.toBuilding)
        if(graph.getEdge(route.fromBuilding + "," + route.toBuilding) == None):
            graph.addEdge(route.fromBuilding , route.toBuilding, route.fromBuilding + "," + route.toBuilding, route)

    # Helper function to convert a deliminator to a integer for direction.
    def getRouteDirection(self, line):
            if len(line[0].split("<>")) > 1:
                return 3
            elif len(line[0].split(">")) > 1:
                return 1
            elif len(line[0].split("<")) > 1:
                return 2
            else:
                return 4
    
    # Converts a string line into an edge object by taking in a line that has already been split into a list of strings.
    # Uses the direction of the edge to determine if the edge is a one way or two way edge.
    # The list of strings is used to assign the appropriate values.
    # List does not violate coding standard as it comes from a split().
    # Creates a campus route object to add to the edge with these values.
    def _processLine(self, line, graph):
        line = line.split("|")
        direction = self.getRouteDirection(line)
        if direction == 1 or direction == 2:
            if direction == 1:
                buildings = line[0].split(">")
                route = CampusRoute(buildings[0], buildings[1], line[1], line[2], line[3])
                self.appendGraph(graph, route)
            else:
                buildings = line[0].split("<")
                route = CampusRoute(buildings[1], buildings[0], line[1], line[2], line[3])
                self.appendGraph(graph, route)
        else:
            buildings = line[0].split("<>")
            route1 = CampusRoute(buildings[0], buildings[1], line[1], line[2], line[3])
            route2 = CampusRoute(buildings[1], buildings[0], line[1], line[2], line[3])
            self.appendGraph(graph, route1)
            self.appendGraph(graph, route2)

    # When writing the graph need to convert edge values back into the format of the input value.
    # This function takes in an edge object and converts it to a string in this format.
    def _edgeToString(self, edge, graph):
        delimiter = " "
        # If we can find an edge with the opposite label add it as a delimiter of <>
        # It is not necessary to do a < like in the source file as the edges can be written the opposite way and have the same meaning
        if(graph.getEdge(edge.toVertex + "," + edge.fromVertex) != None):
            delimiter = "<>"
            graph.removeEdge(edge.toVertex + "," + edge.fromVertex)
        else:
            delimiter = ">"
        string = edge.fromVertex + delimiter + edge.toVertex + "|"
        string += "{}|".format(str(edge.getValue().distance))
        string += "{}|".format(str(edge.getValue().security))
        string += "{}".format(str(edge.getValue().barriers))
        string += "\n"
        return string
            
        
    
        
            
        

            
       
        
    
    
    

