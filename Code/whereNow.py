from menu import *
from file import File
from DSAGraph import DSAGraph
from CampusRoute import CampusRoute
from GraphFunctions import *
def main():
    print("Welcome to the Where Now program!")
    functions = GraphFunctions()
    file = File("Code/Maps/{}".format("map.txt"))
    file.readGraph()
    functions.graph = file.graph
    file = File("Code/Maps/{}".format("journey.txt"))
    file.readJourney()
    functions.journey = file.journey
    choice = ""
    while(choice != 0):
        choice = mainMenu()
        if choice == 1:
            functions.loadFile()
        elif choice == 2:
            functions.nodeOperations()
        elif choice == 3:
            functions.edgeOperations()
        elif choice == 4:
            functions.editCampusRoute()
        elif choice == 5:
            functions.displayGraph()
        elif choice == 6:
            functions.DisplayWorld()
        elif choice == 7:
            functions.enterJourneyDetails()
        elif choice == 8:
            functions.generateRoutes()
        elif choice == 9:
            functions.displayRoutes()
        elif choice == 10:
            functions.saveFile()
        else:
            print("Invalid choice")
            
       
    
    

if __name__ == '__main__':
    main()


    