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



if __name__ == '__main__':
    unittest.main()
