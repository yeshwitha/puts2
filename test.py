import unittest
import main


class TestCalculator(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def testmedian1(self):
        solution = self.app.get("/median?X=1,2,5,100")
        self.assertEqual(b'3.5', solution.data)

    def testmedian2(self):
        solution = self.app.get("/median?X=1,2.33,3.6")
        self.assertEqual(b'2.33', solution.data)

    def testmedian3(self):
        solution = self.app.get("/median?X=1,2,5,0,100")
        self.assertEqual(b'2', solution.data)


if __name__ == '__main__':
    unittest.main()