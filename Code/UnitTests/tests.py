from UnitTestCampusRoute import *
from UnitTestDSAGraph import *
from UnitTestFile import *
from UnitTestGraphFunctions import *

def main():
    print("Test Harnesses for: UnitTests\n")
    UnitTestGraphFunctions().runAllTests()
    UnitTestDSAGraph().runAllTests()
    CampusRouteUnitTest.runAllTests(CampusRouteUnitTest())
    UnitTestFile.runAllTests(UnitTestFile())
    

if __name__ == '__main__':
    main()