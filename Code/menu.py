import numpy as np
def Menu(options):
    for i in range(len(options)):
        print(i+1, ":", options[i])
    print("\n0: Exit\n")
    while choice not in range(len(options)):
        try:
            choice = int(input("\nEnter your choice: "))
            if choice > len(options) or choice < 0:
                print("Choice out of range of options")
            return(choice)
        except Exception:
            print("Invalid input please input an integer between 1 and {}".format(len(options)))
            

def MainMenu():
    options =  np.array([
    "Load input file"
    ,"Node operations (find, insert, delete, update)"
    ,"Edge operations (find, add, remove, update)"
    ,"Parameter tweaks (adjust mapping of codes to impacts, see sample input file)"
    ,"Display graph (weighted adjacency matrix, option to save)"
    ,"Display world (your choice of representation, does not need to be graphical, should include counts of features, option to save)"
    ,"Enter journey details"
    ,"Generate routes"
    ,"Display routes (ranked, option to save)"
    ,"Save network"
    ], dtype=object)
    print("\nMain Menu\n")
    return(Menu(options))
    
def TextInput(text):
        print(text)
        fileName = input()
        return(fileName)


def NodeMenu():
    options = np.array([
    "Find node"
    ,"Insert node"
    ,"Delete node"
    ,"Update node"
    ], dtype=object)
    print("\nHow would you like to edit the node/s?\n")
    return(Menu(options))

def EdgeMenu():
    options = np.array([
    "Find edge"
    ,"Add edge"
    ,"Remove edge"
    ,"Update edge"
    ], dtype=object)
    print("\nHow would you like to edit the edge/s?\n")
    return(Menu(options))

def SaveMenu():
    options = np.array([
    "Save"
    , "Don't save"
    ], dtype=object)
    print("\nWould you like to save the graph?\n")
    return(Menu(options))


 
 
 
 
 
 
 
 
 
 

        
    
        
    
    