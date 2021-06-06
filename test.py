import unittest
import main


class TestCalculator(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def testmax1(self):
        solution = self.app.get("/max?X=1,2,5,100")
        self.assertEqual(b'100', solution.data)

    def testmax2(self):
        solution = self.app.get("/max?X=1,2.33,3.6")
        self.assertEqual(b'3.6', solution.data)

    def testmax3(self):
        solution = self.app.get("/max?X=1,2,5,0,100")
        self.assertEqual(b'100', solution.data)


if __name__ == '__main__':
    unittest.main()