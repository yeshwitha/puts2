import unittest
import main


class TestCalculator(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def testmin1(self):
        solution = self.app.get("/min?X=1,2,5,100")
        self.assertEqual(b'1', solution.data)

    def testmin2(self):
        solution = self.app.get("/min?X=1,2.33,3.6")
        self.assertEqual(b'1', solution.data)

    def testmin3(self):
        solution = self.app.get("/min?X=1,2,5,0,100")
        self.assertEqual(b'0', solution.data)


if __name__ == '__main__':
    unittest.main()