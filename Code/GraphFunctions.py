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

    # Takes in a filename from the user for both the input map and the journey and adds these to the class field values.
    # Needs to be called prior to the main menu to prevent None type errors occuring from an empty graph.
    # Returns the file object for the journey.
    # Doesn't necessarily need to return anything in the current implementation.
    def loadFile(self):
        print("Enter the name of the file you would like to load for a graph:")
        fileName = input()
        # Nice way to check if the file exists without needing a try except loop
        while not os.path.isfile("Maps/{}".format(fileName)):
            print("File not found. Please try again.")
            fileName = input()
        file = File("Maps/{}".format(fileName))
        file.readGraph()
        self.graph = file.graph
        print("Enter the name of the file you would like to load for a journey:")
        fileName = input()
        while not os.path.isfile("Maps/{}".format(fileName)):
            print("File not found. Please try again.")
            fileName = input()
        file = File("Maps/{}".format(fileName))
        file.readJourney()
        self.journey = file.journey
        return(file)

    # Calls node menu and allows the user to perform operations in the menu.
    # Returns nothing as the graph object is edited and stored in the object.
    def nodeOperations(self):
        choice = nodeMenu()
        print("Current Vertices: \n")
        for vertex in self.graph.verticesList:
            print(vertex.getLabel())
        if choice == 1:
            vertexName = getInput("label", "vertex", "find")
            print(vertexName, self.graph.getVertex(vertexName).getValue() + " exists")
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
    
    # Calls edge menu and allows the user to perform operations in the menu.
    # Returns nothing as the graph object is edited and stored in the object.
    def edgeOperations(self):
        choice = edgeMenu()
        print("Current Edges: \n")
        for edge in self.graph.edges:
            print(edge.getLabel())
        if choice == 1:
            fromBuilding = getInput("label", "first building", "find", True)
            toBuilding = getInput("label", "second building", "find", True)
            print(self.graph.getEdge(fromBuilding + "," + toBuilding).getLabel() + " exists")
        elif choice == 2:
            campusRoute = self.createCampusRoute()
            # To prevent user errors the labels are taken in then a comma is added instead of requiring it to be inputted.
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

    # Gets inputs for a campus object from user so it can be added to the relevant edge. 
    # Only the labels are required as the program accounts for empty distance, security and barrier fields elsewhere.
    def createCampusRoute(self):
        fromBuilding = getInput("label", "first building", "add", True)
        toBuilding = getInput("label", "second building", "add", True)
        distance = getInput("distance", "route", "add")
        distance = self._isDistanceEmpty(distance)
        security = getInput("security", "route", "add")
        barriers = getInput("barriers", "route", "add")
        return CampusRoute(fromBuilding, toBuilding, distance, security, barriers)
    
    # Similar to creating a route however inputs are used to modify existing values.
    def editCampusRoute(self):
        label = getInput("label", "edge", "update", True)
        edge = self.graph.getEdge(label)
        campusRoute = edge.getValue()
        campusRoute.distance = getInput("distance", "route", "update")
        # Used to prevent errors from empty inputs.
        distance = self._isDistanceEmpty(distance)
        distance = "D:" + distance
        campusRoute.security = getInput("security", "route", "update")
        campusRoute.barriers = getInput("barriers", "route", "update")
        self.graph.updateEdge(label, label, campusRoute)

    # Checks if the distance input is empty.
    def _isDistanceEmpty(self, distance):
        if distance == "" or len(distance) < 1:
            return ""
        else:
            return distance

    # Allows the user to view the graph as a matrix and save it if it is correct.
    def displayGraph(self):
        self.graph.displayAsMatrix()
        if saveMenu() == "1":
            self.file.writeFileFromGraph(self.graph)

    # Displays a representation of the graph in a more human readable way.
    def displayWorld(self):
        self.graph.displayAsList()
        if saveMenu() == "1":
            self.file.writeFileFromGraph(self.graph)

    # The user may want a journey that isn't pre-defined in a file so this function allows them to create one by utilising the campusRoute class which already contains most of the information required.
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

    # Generate a collection of routes from a stack returned by depthFirstSearch. 
    # Currently not complete however in it's finished variant would call generateRoute until the queue only contains a head or tail or is empty.
    def generateRoutes(self):
        # If there isn't a journey the user is asked to input one
        if self.journey == None:
            self.enterJourneyDetails()
        startPoint, target, barriers, security = self.journey.fromBuilding, self.journey.toBuilding, self.journey.barriers, self.journey.security
        routes = np.zeros(self.graph.getEdgeCount(), dtype=object)
        visited = self.graph.depthFirstSearch(startPoint, target)
        # Only one route is generated thus it is indexed to 0.
        routes[0] = self.generateRoute(visited, target, barriers, security)
        self.routes = routes

    # Takes in the queue containing all vertices that branch from the critical path towards the target. 
    # To find a path to the target it checks first that any journey pre-conditions such as barriers and security are met.
    # If they are it then checks if the vertex is the target and if so appends it to the route and sets the target to that vertex. 
    # The end of the loop should naturally reach the startpoint and the route is returned.
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
        # Since the route is inverted going from the end to the start it is inverted using this function.
        route = self._invertArray(route)
        # The route could also contain 0 fields which are used to tell when at the end of an array in this program.
        # As such the array is shuffled down so that the 0 fields are at the end.
        route = self._shuffleArrayDown(route)
        return route

    # Checks if any pre-conditions are met that would cause the path to be untraversible and returns true or false if they are
    def _isPathBlocked(self, path, barriers, security):
        if len(barriers) > 2 and (path.barriers == barriers or barriers in path.barriers):
            return True
        if len(security) > 2 and (security not in path.security):
            return True
        return False
            
    # Inverts an array by making it go from back to front.
    def _invertArray(self, array):
        invertedArray = np.zeros(len(array), dtype=object)
        for i in range(len(array)):
            invertedArray[i] = array[len(array) - i - 1]
        return(invertedArray)

    # Shuffles an array down so that the 0 fields are at the end.
    def _shuffleArrayDown(self, array):
        shuffledArray = np.zeros(len(array), dtype=object)
        shuffleIdx = 0
        for i in array:
            if i != 0:
                shuffledArray[shuffleIdx] = i
                shuffleIdx += 1
        return(shuffledArray)

    # Goes through all the routes and prints off the paths inside the route and it's total distance.
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
                        # The edges are stored with ,'s between vertices however an arrow is more representative of the actual path.
                        print(path.getLabel().replace(",", " -> "))
                        # Check if distance is empty as the float calculation cannot handle a None value.
                        if path.getValue().distance != '':
                            # Convert string distance to float without it's marker D:
                            distance += float(path.getValue().distance.replace("D:", ""))   
        print("\nThe distance is: "+ str(distance) + "\n")

    # Save the file to an output file defined by the user.
    def saveFile(self):
        choice = saveMenu()
        # Need to get a file name from a user to save the file.
        if self.file == None and choice != 0:
            self.file = File()
            fileName = input("Enter the name of the file you would like to save:")
            self.file.fileName = fileName
            if(len(self.file.fileName.split(".txt")) < 2):
                self.file.fileName += ".txt"
            self.file.fileName = "Maps/{}".format(self.file.fileName )
        if choice == 1:
            self.file.writeFileFromGraph(self.graph)

# Dynamic function to ask for input from the user.
# If the input is required and the user inputs an empty string will call itself again until the user inputs atleast a value.
# Because it's dynamic cannot validate that the input is valid beyond checking it is not empty.
def getInput(lookingFor, type, operation, required = False):
    print("Enter the {} of the {} you would like to {}:".format(lookingFor, type, operation))
    value = input()
    if len(value) < 1 and required == True:
        print("Please input a value")
        return getInput(lookingFor, type, operation, True)
    return(value)
        
