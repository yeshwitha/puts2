import unittest
import main


class TestCalculator(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()

	def test_sub1(self):
		solution = self.app.get('/sub?A=20&B=2')
		self.assertEqual(b'18.0', solution.data)

	def test_sub2(self):
		solution = self.app.get('/sub?A=3/2&B=1/2')
		self.assertEqual(b'1.0', solution.data)

	def test_sub3(self):
		solution = self.app.get('/sub?A=122.22&B=1.002')
		self.assertEqual(b'121.218', solution.data)

	def test_sub4(self):
		solution = self.app.get('/sub?A=22.222&B=98')
		self.assertEqual(b'-75.778', solution.data)

	def test_sub5(self):
		solution = self.app.get('/sub?A=100&B=98.9')
		self.assertEqual(b'1.1', solution.data)

if __name__ == '__main__':
	unittest.main()