# CampusGraph

"Usage:
"Enter interactive mode:
"python3 whereNow.py -i
"Enter silent mode:
"python3 whereNow.py <mapFileName> <journeyFileName> <outputFileName>

CampusRoute.py: Contains campusRoute class used for storing journey information and edge values
DSAGraph.py: Contains DSAGraph class which has all functions and functionality pertaining to the graph implementation
DSAGraphEdge.py: Contains DSAGraphEdge class which has all functionality related to graph edges
DSAGraphVertex.py: Contains DSAGraphVertex class which has all functionality related to graph vertices
DSALinkedList.py: Contains the DSALinkedList class which has all functionality related to linked lists and inherits LinkedListIterator
DSALinkedListIterator.py: Contains a **iter** method to loop through a linked list
DSAListNode.py: Contains the DSAListNode class which has all functionality related to nodes in the linked list
DSAQueue.py: Contains the DSAQueue class which has an implementation of a shuffling queue
DSAStack.py: Contains a DSAStack class which has an implementation of a stack
file.py: Contains the File class which has an implementation of a FILE IO system
GraphFunctions.py: Contains all functions in the main menu for users to upload , edit or export graphs within
menu.py: Contains all menus used in the program
modes.py: Contains each mode such as interactive or silent mode used in the program
whereNow.py: Wrapper for all other functions with the main for the program.

UnitTests/tests.py: Calls all other Unit Test classes to initiate all of their tests on the given code.
Maps/ : Contains all txt map input and outputs
Data/ : Contains map and journey information for testing
UML Info: Class methods for writing UML diagrams.

(import numpy as np) in files: numpy is used for initialising and performing functions on arrays.
