import sys
sys.path.append("../CampusGraphs/Code")
from DSAStack import *
from unittest import *
class UnitTestStack(TestCase):
    def __init__(self):
            super().__init__()
            self.stack = DSAStack()

    def runAllTests(self):
        self.testPush()
        print("Push Passed")
        self.testPop()
        print("Pop Passed")


    def resetStack(self):
        self.stack = DSAStack()

    def testPush(self):
        self.resetStack()
        self.stack.push("A")
        self.assertEqual(self.stack.top(), "A", "Push Failed")
        self.stack.push("B")
        self.assertEqual(self.stack.top(), "B", "Push Failed")

    def testPop(self):
        self.resetStack()
        self.stack.push("A")
        self.stack.push("B")
        self.stack.push("C")
        self.stack.push("D")
        self.stack.push("E")
        self.stack.push("F")
        self.stack.pop()
        self.assertEqual(self.stack.top(), "E", "Pop Failed")
        