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

	def testmax1(self):
		solution = self.app.get("/max?X=1,2,5,100")
		self.assertEqual(b'100', solution.data)

	def testmax2(self):
		solution = self.app.get("/max?X=1,2.33,3.6")
		self.assertEqual(b'3.6', solution.data)

	def testmax3(self):
		solution = self.app.get("/max?X=1,2,5,0,100")
		self.assertEqual(b'100', solution.data)

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

	def testmedian1(self):
		solution = self.app.get("/median?X=1,2,5,100")
		self.assertEqual(b'3.5', solution.data)

	def testmedian2(self):
		solution = self.app.get("/median?X=1,2.33,3.6")
		self.assertEqual(b'2.33', solution.data)

	def testmedian3(self):
		solution = self.app.get("/median?X=1,2,5,0,100")
		self.assertEqual(b'2', solution.data)

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
