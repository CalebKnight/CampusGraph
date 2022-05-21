import sys
import os 
from GraphFunctions import GraphFunctions
from menu import *
from file import *

# Interactive mod takes in main menu user input and calls functions in GraphFunctions.py to generate appropriate output to the graph or routes in that object. 

def interactiveMode():
    print("Welcome to the Where Now program!")
    functions = GraphFunctions()
    choice = ""
    functions.loadFile()
    while(choice != 0):
        choice = mainMenu()
        if choice == 1:
            try:
                functions.loadFile()
            except Exception as e:
                print(e)
        elif choice == 2:
            try:
                functions.nodeOperations()
            except Exception as e:
                print(e)
        elif choice == 3:
            try:
                functions.edgeOperations()
            except Exception as e:
                print(e)
        elif choice == 4:
            try:
                functions.editCampusRoute()
            except Exception as e:
                print(e)
        elif choice == 5:
            try:
                functions.displayGraph()
            except Exception as e:
                print(e)
        elif choice == 6:
            try:
                functions.displayWorld()
            except Exception as e:
                print(e)
        elif choice == 7:
            try:
                functions.enterJourneyDetails()
            except Exception as e:
                print(e)
        elif choice == 8:
            try:
                functions.generateRoutes()
            except Exception as e:
                print(e)
        elif choice == 9:
            try:
                functions.displayRoutes()
            except Exception as e:
                print(e)
        elif choice == 10:
            try:
                functions.saveFile()
            except Exception as e:
                print(e)
        else:
            if choice != 0:
                print("Invalid choice")
    return

# Silent mod takes in a map file name, journey file name, and output file name and calls functions in GraphFunctions.py to generate an appropriate file from this input.
# Output file is a list of routes which contain paths from the source building to the target building
def silentMode(mapFileName, journeyFileName, outPutName):
    if(not os.path.isfile("Maps/" + mapFileName)):
        print("File not found")
    else:
        try:
            functions = GraphFunctions()
            functions.file = File("Maps/" + journeyFileName)
            functions.file.readJourney()
            functions.journey = functions.file.journey
            functions.file.fileName = "Maps/" + mapFileName
            functions.file.readGraph()
            functions.graph = functions.file.graph
            functions.file.fileName = "Maps/" + outPutName
            functions.generateRoutes()
            functions.file.writeRoutesToFile(functions.routes)
        except Exception as e:
            print(e)
    return

def usageInfo():
    pass
