from UnitTestCampusRoute import *
from UnitTestDSAGraph import *
from UnitTestFile import *
from UnitTestGraphFunctions import *
from UnitTestQueue import *
from UnitTestStack import *

def main():
    # The test harnesses test each function for expected output. 
    # They also inherit unit test so that assert equal and other functionality can be easily run inside the class.
    print("Test Harnesses for: UnitTests\n")
    UnitTestGraphFunctions().runAllTests()
    UnitTestDSAGraph().runAllTests()
    CampusRouteUnitTest().runAllTests()
    UnitTestFile().runAllTests()
    UnitTestQueue().runAllTests()
    UnitTestStack().runAllTests()
    

if __name__ == '__main__':
    main()