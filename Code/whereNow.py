from menu import *
from file import File
from DSAGraph import DSAGraph
from CampusRoute import CampusRoute
from GraphFunctions import *
import sys
from modes import *
def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "i":
            interactiveMode()
        else:
            silentMode(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        usageInfo()
        
            
       
    
    

if __name__ == '__main__':
    main()


    