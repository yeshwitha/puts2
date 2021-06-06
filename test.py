import unittest
import main


class TestCalculator(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()

	def test_div1(self):
		solution = self.app.get('/div?A=20&B=2')
		self.assertEqual(b'10.0', solution.data)

	def test_div2(self):
		solution = self.app.get('/div?A=3/2&B=1/2')
		self.assertEqual(b'3.0', solution.data)

	def test_div3(self):
		solution = self.app.get('/div?A=122.22&B=1.002')
		self.assertEqual(b'121.97604790419162', solution.data)

	def test_div4(self):
		solution = self.app.get('/div?A=22.222&B=98')
		self.assertEqual(b'0.22675510204081634', solution.data)

	def test_div5(self):
		solution = self.app.get('/div?A=100&B=98.9')
		self.assertEqual(b'1.0111223458038423', solution.data)

if __name__ == '__main__':
	unittest.main()