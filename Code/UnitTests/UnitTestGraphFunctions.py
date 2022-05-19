import sys
sys.path.append("../CampusGraphs/Code")
from unittest import *
from DSAGraph import *
from GraphFunctions import *
from Journey import *
class UnitTestGraphFunctions(TestCase):
    def __init__(self):
        super().__init__()
        self.functions = GraphFunctions()

    def runAllTests(self):
        self.testGenerateRoutes()

    def createGraph(self):
        self.functions.graph = DSAGraph()

    def addValuesForSearch(self):
        self.createGraph()
        self.functions.graph.addVertex("A")
        self.functions.graph.addVertex("B")
        self.functions.graph.addVertex("C")
        self.functions.graph.addEdge("A", "B", "A,B", 1)
        self.functions.graph.addEdge("B", "A", "B,A", 1)
        self.functions.graph.addEdge("B", "C", "B,C", 1)
        self.functions.graph.addEdge("C", "B", "C,B", 1)
    def testGenerateRoutes(self):
        self.createGraph()
        self.addValuesForSearch()
        self.functions.journey = Journey("A", "C", 4) 
        self.functions.generateRoutes()
        self.assertEqual(self.functions.routes[0].getLabel(), "A,B", "Routes AB Not First Index")
        self.assertEqual(self.functions.routes[1].getLabel(), "B,C", "Route BC Not Second Index")