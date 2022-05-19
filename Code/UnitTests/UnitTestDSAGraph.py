import sys
sys.path.append("../CampusGraphs/Code")
from DSAGraph import *
from unittest import *

class UnitTestDSAGraph(TestCase):
    def __init__(self):
        super().__init__()
        self.graph = DSAGraph()

    def runAllTests(self):
        self.testAddVertex()
        print("TestAddVertex passed")
        self.testAddEdge()
        print("TestAddEdge passed")
        self.testHasVertex()
        print("TestHasVertex passed")
        self.testGetVertexCount()
        print("TestGetVertexCount passed")
        self.testGetEdgeCount()
        print("TestGetEdgeCount passed")
        self.testGetVertex()
        print("TestGetVertex passed")
        self.testGetEdge()
        print("TestGetEdge passed")
        self.testGetAdjacent()
        print("TestGetAdjacent passed")
        self.testRemoveVertex()
        print("TestRemoveVertex passed")
        self.testRemoveEdge()
        print("TestRemoveEdge passed")
        self.testUpdateVertex()
        print("TestUpdateVertex passed")
        self.testUpdateEdge()
        print("TestUpdateEdge passed")
        self.testDepthFirstSearch()
        print("TestDepthFirstSearch passed")
        
    def createGraph(self):
        self.graph = DSAGraph()

    def addABC(self):
        self.graph.addVertex("A")
        self.graph.addVertex("B")
        self.graph.addVertex("C")
        self.graph.addEdge("A", "B", "A,B", 1)
        self.graph.addEdge("B", "A", "B,A", 1)
        self.graph.addEdge("B", "C", "B,C", 1)
    
    def resetGraph(self):
        self.createGraph()
        self.addABC()

    def testAddVertex(self):
        self.resetGraph()
        self.assertEqual(self.graph.verticesList.getLength(), 3, "Vertex count is not 3")

    def testAddEdge(self):
        self.resetGraph()
        self.assertEqual(self.graph.edges.getLength(), 3, "Edge count is not 3")

    def testHasVertex(self):
        self.resetGraph()
        self.assertEqual(self.graph.hasVertex("A"), True, "Vertex A is not found")
        self.assertEqual(self.graph.hasVertex("B"), True, "Vertex B is not found")

    def testGetVertexCount(self):
        self.resetGraph()
        self.assertEqual(self.graph.getVertexCount(), 3, "Vertex count is not 3")

    def testGetEdgeCount(self):
        self.resetGraph()
        self.assertEqual(self.graph.getEdgeCount(), 3, "Edge count is not 3")

    def testGetVertex(self):
        self.resetGraph()
        self.assertEqual(self.graph.getVertex("A").getLabel(), "A", "Vertex A is not found")
        self.assertEqual(self.graph.getVertex("C").getLabel(), "C", "Vertex C is not found")

    def testGetEdge(self):
        self.resetGraph()
        self.assertEqual(self.graph.getEdge("A,B").getLabel(), "A,B", "Edge AB is not found")
        self.assertEqual(self.graph.getEdge("B,A").getLabel(), "B,A", "Edge BA is not found")

    def testGetAdjacent(self):
        self.resetGraph()
        # self.assertEqual(self.graph.getAdjacent("A").getLength(), 1, "Vertex A is not adjacent to 1 vertex")
        self.assertEqual(self.graph.getAdjacent("B").getLength(), 2, "Vertex B is not adjacent to 1 vertex")
    
    def testRemoveVertex(self):
        self.resetGraph()
        self.graph.removeVertex("A")
        self.assertEqual(self.graph.getVertexCount(), 2, "Vertex A is not removed")
        self.assertEqual(self.graph.getEdgeCount(), 1, "Edge AB is not removed")

    def testRemoveEdge(self):
        self.resetGraph()
        self.graph.removeEdge("A,B")
        self.assertEqual(self.graph.getEdgeCount(), 2, "Edge AB is not removed")

    def testUpdateVertex(self):
        self.resetGraph()
        self.graph.updateVertex("A", "D")
        self.assertEqual(self.graph.getVertex("D").getLabel(), "D", "Vertex A is not updated")

    def testUpdateEdge(self):
        self.resetGraph()
        self.graph.updateEdge("A,B", "A,D", 2)
        self.assertEqual(self.graph.getEdge("A,D").getLabel(), "A,D", "Edge AB is not updated")

    def addValuesForSearch(self):
        self.createGraph()
        self.graph.addVertex("A")
        self.graph.addVertex("B")
        self.graph.addVertex("C")
        self.graph.addVertex("D")
        self.graph.addVertex("E")
        self.graph.addVertex("F")
        self.graph.addVertex("G")
        self.graph.addEdge("A", "B", "A,B", 1)
        self.graph.addEdge("A", "D", "A,D", 1)
        self.graph.addEdge("A", "E", "A,E", 1)
        self.graph.addEdge("B", "A", "B,A", 1)
        self.graph.addEdge("B", "C", "B,C", 1)
        self.graph.addEdge("B", "E", "B,E", 1)
        self.graph.addEdge("C", "B", "C,B", 1)
        self.graph.addEdge("C", "D", "C,D", 1)
        self.graph.addEdge("C", "E", "C,E", 1)
        self.graph.addEdge("D", "A", "D,A", 1)
        self.graph.addEdge("D", "C", "D,C", 1)
        self.graph.addEdge("E", "A", "E,A", 1)
        self.graph.addEdge("E", "B", "E,B", 1)
        self.graph.addEdge("E", "C", "E,C", 1)

    def testDepthFirstSearch(self):
        self.addValuesForSearch()
        target = "D"
        routes = np.zeros(self.graph.getEdgeCount() * self.graph.getEdgeCount(), dtype=object)
        # visited = self.graph.depthFirstSearch("A")
        idx = 0
        for vertex in self.graph.verticesList:
            visited = self.graph.depthFirstSearch(vertex.getLabel(), target)
            if visited != None:
                print(visited)
                routes[idx] = visited
                idx += 1
        for route in routes:
            if route != None and route != 0:
                print("\nPath\n")
                for path in route.queue:
                    print(path.getLabel())
    

    