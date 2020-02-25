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
        self.assertEqual(2, task.firstLastListElem(listOfOne)[0])
        self.assertEqual(2, task.firstLastListElem(listOfOne)[1])
        # Expecting first and last element to be first and second element of
        # the list passed in to Function
        self.assertEqual(1, task.firstLastListElem(listOfTwo)[0])
        self.assertEqual(2, task.firstLastListElem(listOfTwo)[1])
        # Expecting first and last element of list passed in to function to be
        # correct
        self.assertEqual(1, task.firstLastListElem(listOfThree)[0])
        self.assertEqual(3, task.firstLastListElem(listOfThree)[1])

    def test_diffTwoDates(self):
        # Setting up environmental variables which consist of varying date objects
        # pair 1, expect 0
        date1a = task.datetime.date(2000, 5, 2)
        date1b = task.datetime.date(2000, 5, 2)
        self.assertEqual(0, task.diffTwoDates(date1a, date1b))
        # pair 2, expect 3 when the dates are switched in the function call
        date2a = task.datetime.date(2000, 5, 2)
        date2b = task.datetime.date(2000, 4, 30)
        self.assertEqual(2, task.diffTwoDates(date2a, date2b))
        self.assertEqual(2, task.diffTwoDates(date2b, date2a))
        # pair 3, Checking that leap year is accounted for in date difference
        date3a = task.datetime.date(2020, 2, 21)
        date3b = task.datetime.date(2020, 3, 1)
        self.assertEqual(9, task.diffTwoDates(date3a, date3b))
        # pair 4, checking entire year difference
        date4a = task.datetime.date(2020, 1, 1)
        date4b = task.datetime.date(2021, 1, 1)
        self.assertEqual(366, task.diffTwoDates(date4a, date4b))
        # Ensuring faulty year values return None
        date5a = task.datetime.date(2020, 1, 1)
        date5b = task.datetime.date(0, 1, 1)
        self.assertEqual(None, task.diffTwoDates(date5a, date5b))


if __name__ == '__main__':
    unittest.main()
