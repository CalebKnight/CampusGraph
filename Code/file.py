import os
from DSAGraph import DSAGraph
from CampusRoute import CampusRoute
import sys

class File:
    def __init__(self, fileName):
        self.fileName = fileName
        self.fileContent = None
    def readFile(self):
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
                    line = file.readline()
                else:
                    self._processLine(line[0], graph)
                    line = file.readline()
        file.close()
        self.fileContent = graph
        
    def writeFileFromGraph(self, graph):
        with open(os.path.join(self.fileName), "w") as file:
            for edge in graph.edges:
                line = self._edgeToString(edge, graph)
                file.write(line)
        file.close()

    def appendGraph(self, graph, route):
        if(graph.getVertex(route.fromBuilding) == None):
            graph.addVertex(route.fromBuilding)
        if(graph.getVertex(route.toBuilding) == None):
            graph.addVertex(route.toBuilding)
        if(graph.getEdge(route.fromBuilding + "," + route.toBuilding) == None):
            graph.addEdge(route.fromBuilding , route.toBuilding, route.fromBuilding + "," + route.toBuilding, route)
        return

    def getRouteDirection(self, line):
            if len(line[0].split("<>")) > 1:
                return 3
            elif len(line[0].split(">")) > 1:
                return 1
            elif len(line[0].split("<")) > 1:
                return 2
            else:
                return 4


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
        string += "D:{}|".format(str(edge.getValue().distance))
        string += "S:{}|".format(str(edge.getValue().security))
        string += "B:{}".format(str(edge.getValue().barriers))
        string += "\n"
        return string
            
        
    
        
            
        
        
            
       
        
    
    
    
