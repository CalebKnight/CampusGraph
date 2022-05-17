from UnitTestCampusRoute import *
from UnitTestDSAGraph import *
from UnitTestFile import *

def main():
    print("Test Harnesses for: UnitTests\n")
    DSAGraphUnitTest().runAllTests()
    # CampusRouteUnitTest.runAllTests(CampusRouteUnitTest())
    # UnitTestFile.runAllTests(UnitTestFile())
    

if __name__ == '__main__':
    main()