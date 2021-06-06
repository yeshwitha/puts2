import unittest
import main


class TestCalculator(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()

	def test_add1(self):
		solution = self.app.get('/add?A=20&B=2')
		self.assertEqual(b'22.0', solution.data)

	def test_add2(self):
		solution = self.app.get('/add?A=3/2&B=1/2')
		self.assertEqual(b'2.0', solution.data)

	def test_add3(self):
		solution = self.app.get('/add?A=122.22&B=1.002')
		self.assertEqual(b'123.222', solution.data)

	def test_add4(self):
		solution = self.app.get('/add?A=22.222&B=98')
		self.assertEqual(b'120.222', solution.data)

	def test_add5(self):
		solution = self.app.get('/add?A=100&B=98.9')
		self.assertEqual(b'198.9', solution.data)

if __name__ == '__main__':
	unittest.main()