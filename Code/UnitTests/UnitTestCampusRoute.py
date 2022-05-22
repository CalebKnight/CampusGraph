import sys
sys.path.append("../CampusGraphs/Code/")
from CampusRoute import CampusRoute
from unittest import *
class CampusRouteUnitTest(TestCase):
    def __init__(self):
        super().__init__()
        
    def runAllTests(self):
        self.testSetter()
    
    def createRoute(self, fromBuilding, toBuilding, distance, security, barriers):
        return CampusRoute(fromBuilding, toBuilding, distance, security, barriers)
    def testSetter(self):
        route = self.createRoute("A", "B", "1", "2", "3")
        print("Setting CampusRoute to: C, D, 4, 5, 6")
        route.setFromBuilding("C")
        route.setToBuilding("D")
        route.setDistance("4")
        route.setSecurity("5")
        route.setBarriers("6")
        self.assertEqual(route.fromBuilding, "C", "FromBuilding is not C")
        self.assertEqual(route.toBuilding, "D", "ToBuilding is not D")
        self.assertEqual(route.distance, "4", "Distance is not 4")
        self.assertEqual(route.security, "5", "Security is not 5")
        self.assertEqual(route.barriers, "6", "Barriers is not 6")

