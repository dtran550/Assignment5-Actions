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
        listOfTwo = [1, 2]
        listOfThree = [1, 2, 3]
        # Expecting None when function is passed an empty list
        self.assertEqual(None, task.firstLastListElem(listEmpty))
        # Function returns a tuple of first and last value, so call assert on
        # first element, and second element of returned object of function
        self.assertEqual(2, task.firstLastListElem(listOfOne[0]))
        self.assertEqual(2, task.firstLastListElem(listOfOne[1]))
        # Expecting first and last element to be first and second element of
        # the list passed in to Function
        self.assertEqual(1, task.firstLastListElem(listOfTwo)[0])
        self.assertEqual(2, task.firstLastListElem(listOfTwo)[1])
        # Expecting first and last element of list passed in to function to be
        # correct
        self.assertEqual(1, task.firstLastListElem(listOfThree)[0])
        self.assertEqual(3, task.firstLastListElem(listOfThree)[3])


if __name__ == '__main__':
    unittest.main()
