import sys
sys.path.append("../CampusGraphs/Code")
from file import File
from unittest import *
from DSAGraph import *
from CampusRoute import *


class UnitTestFile(TestCase):
    def __init__(self):
        super().__init__()
        self.file = None
        self.graph = None

    def runAllTests(self):
        self.testReadGraph()
        print("TestReadFile passed")
        self.testWriteFile()
        print("TestWriteFile passed")
        self.testReadJourney()
        print("TestReadJourney passed")
        
    def addGraphValues(self):
        self.graph.addVertex("A")
        self.graph.addVertex("B")
        self.graph.addVertex("C")
        self.graph.addEdge("A", "B", "A,B", CampusRoute("A", "B", 3, 1, 2))
        self.graph.addEdge("B", "A", "B,A", CampusRoute("B", "A", 6, 1, 2))
        self.graph.addEdge("B", "C", "B,C", CampusRoute("B", "C", 2, 1, 2))

    def createGraph(self):
        self.graph = DSAGraph()
        self.addGraphValues()

    def testWriteFile(self):
        self.createGraph()
        self.file = File("../CampusGraphs/Code/Data/test.txt")
        self.file.writeFileFromGraph(self.graph)
        self.file = File("../CampusGraphs/Code/Data/test.txt")
        self.file.readGraph()
        self.assertEqual(self.graph.edges.peekFirst().getFrom(), self.file.graph.edges.peekFirst().getFrom())
        self.assertEqual(self.graph.edges.peekFirst().getTo(), self.file.graph.edges.peekFirst().getTo())
        # self.assertEqual(self.graph.edges.peekFirst().getValue().distance, self.file.graph.edges.peekFirst().getValue().distance)
        
    def testReadGraph(self):
        self.createGraph()
        self.file = File("../CampusGraphs/Code/Data/test.txt")
        self.file.readGraph()
        self.assertEqual(self.graph.edges.peekFirst().getFrom(), self.file.graph.edges.peekFirst().getFrom())
        self.assertEqual(self.graph.edges.peekFirst().getTo(), self.file.graph.edges.peekFirst().getTo())
        # self.assertEqual(self.graph.edges.peekFirst().getValue().distance, self.file.graph.edges.peekFirst().getValue().distance)

    def testReadJourney(self):
        self.file = File("../CampusGraphs/Code/Data/Journey.txt")
        self.file.readJourney()
        self.assertEqual(self.file.journey.fromBuilding, "314.221.lab")
       




   


