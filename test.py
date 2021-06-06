import unittest
import main


class TestCalculator(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def testAverage(self):
        solution = self.app.get("/average?X=1,2,5,0,100")
        self.assertEqual(b'21.6', solution.data)

    def testAvg(self):
        solution = self.app.get("/avg?X=1,2.33,4.5,3.6")
        self.assertEqual(b'2.8575', solution.data)

    def testMean(self):
        solution = self.app.get("/mean?X=1,2,5,0,100,-100,-5,-2")
        self.assertEqual(b'0.125', solution.data)


if __name__ == '__main__':
    unittest.main()