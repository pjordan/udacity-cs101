import unittest
import doctest
import task

class TestSequenceFunctions(unittest.TestCase):
	def test_dataset1(self):
		failure_count, test_count = doctest.testfile("dataset1.txt")
		self.assertEquals(failure_count,0)

	def test_dataset2(self):
		failure_count, test_count = doctest.testfile("dataset2.txt")
		self.assertEquals(failure_count,0)
		
if __name__ == '__main__':
    unittest.main()
