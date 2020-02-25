import unittest
import task


class TestCase(unittest.TestCase):
    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_areaCircle(self):
        # Setting up environmental variables to use for test of areaCircle()
        radius = 10
        expected = radius * radius * task.math.pi
        self.assertEqual(expected, task.areaCircle(radius))
        # Testing case where radius provided is negative
        radius = - 10
        self.assertEqual(None, task.areaCircle(radius))
        # Testing case where radius provided is negative
        radius = 0
        self.assertEqual(0, task.areaCircle(radius))

    def test_firstLastListElem(self):
        # Setting up environmental variables which consist of lists of varying length
        listEmpty = []
        listOfOne = [2]
        listOfTTwo = [1, 2]
        listOfThree = [1, 2, 3]
        # Expecting None when function is passed an empty list
        assertEqual(None, firstLastListElem(listEmpty))
        # Function returns a tuple of first and last value, so call assert on
        # first element, and second element of returned object of function
        assertEqual(2, firstLastListElem(listOfOne[0]))
        assertEqual(2, firstLastListElem(listOfOne[1]))
        # Expecting first and last element to be first and second element of
        # the list passed in to Function
        assertEqual(1, firstLastListElem(listOfTTwo)[0])
        assertEqual(2, firstLastListElem(listOfTTwo)[1])
        # Expecting first and last element of list passed in to function to be
        # correct
        assertEqual(1, firstLastListElem(listOfTThree)[0])
        assertEqual(3, firstLastListElem(listOfTThree)[3])


if __name__ == '__main__':
    unittest.main()
