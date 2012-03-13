import unittest
import task

class TestSequenceFunctions(unittest.TestCase):
    def test_dataset1(self):
		correct = [[1,2,3],
		           [2,3,1],
		           [3,1,2]]
		self.assertEquals(task.check_sudoku(correct),True)

    def test_dataset2(self):
	    incorrect = [[1,2,3,4],
		             [2,3,1,3],
		             [3,1,2,3],
		             [4,4,4,4]]
		self.assertEquals(task.check_sudoku(incorrect) , False)

if __name__ == '__main__':
    unittest.main()
