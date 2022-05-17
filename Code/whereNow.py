from menu import *
from file import File
from DSAGraph import DSAGraph
from CampusRoute import CampusRoute
from GraphFunctions import *
def main():
    print("Welcome to the Where Now program!")
    
    file = File("Code/map.txt")
    file.readFile()
    functions = GraphFunctions()
    functions.graph = file.fileContent
    choice = ""
    while(choice != "0"):
        choice = MainMenu()
        if choice == "1":
           functions.loadFile()
        elif choice == "2":
            functions.nodeOperations()
        elif choice == "3":
            functions.edgeOperations()
        elif choice == "4":
            functions.editCampusRoute()
        elif choice == "5":
            functions.displayGraph()
        elif choice == "6":
            functions.DisplayWorld()
        elif choice == "7":
            functions.enterJourneyDetails()
        elif choice == "8":
            functions.generateRoutes()
        elif choice == "9":
            functions.displayRoutes()
        elif choice == "10":
            functions.saveFile()
            pass
        else:
            print("Invalid choice")
            
       
    
    

if __name__ == '__main__':
    main()


    