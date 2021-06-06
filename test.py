import unittest
import main


class TestCalculator(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()

	def test_mul1(self):
		solution = self.app.get('/mul?A=20&B=2')
		self.assertEqual(b'40.0', solution.data)

	def test_mul2(self):
		solution = self.app.get('/mul?A=3/2&B=1/2')
		self.assertEqual(b'0.75', solution.data)

	def test_mul3(self):
		solution = self.app.get('/mul?A=122.22&B=1.002')
		self.assertEqual(b'122.46444', solution.data)

	def test_mul4(self):
		solution = self.app.get('/mul?A=22.222&B=98')
		self.assertEqual(b'2177.756', solution.data)

	def test_mul5(self):
		solution = self.app.get('/mul?A=100&B=98.9')
		self.assertEqual(b'9890.0', solution.data)

if __name__ == '__main__':
	unittest.main()