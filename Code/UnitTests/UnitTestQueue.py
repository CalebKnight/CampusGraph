import sys
sys.path.append("../CampusGraphs/Code/")
from DSAQueue import *
from unittest import *
class UnitTestQueue(TestCase):
    def __init__(self):
            super().__init__()
            self.queue = DSAQueue()

    def runAllTests(self):
        self.testEnqueue()
        print("Enqueue Passed")
        self.testDequeue()
        print("Dequeue Passed")

    def resetQueue(self):
        self.queue = DSAQueue()

    def testEnqueue(self):
        self.queue.enqueue("A")
        self.assertEqual(self.queue.peek(), "A", "Enqueue Failed")
        self.queue.enqueue("B")
        self.assertEqual(self.queue.peek(), "A", "Enqueue Failed")

    def testDequeue(self):
        self.resetQueue()
        self.queue.enqueue("A")
        self.queue.enqueue("B")
        self.queue.enqueue("C")
        self.queue.enqueue("D")
        self.queue.enqueue("E")
        self.queue.enqueue("F")
        self.queue.dequeue()
        self.assertEqual(self.queue.peek(), "B", "Dequeue Failed")