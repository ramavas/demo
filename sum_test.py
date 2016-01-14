import unittest
import sum

class sum_test(unittest.TestCase):
	def test_sum(self):
		self.assertEqual(sum.sum(4,5), 9)

	def test_sum_fail(self):
		self.assertFalse(sum.sum(4,5) == 8)

	def test_fail(self):
		self.assertTrue(sum.sum(8,9), 17)

if __name__ == '__main__':
    unittest.main()

