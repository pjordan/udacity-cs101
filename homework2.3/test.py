import unittest
import task

class TestSequenceFunctions(unittest.TestCase):
    def test_dataset1(self):
        self.assertEquals(task.udacify('dacity'),'Udacity')

    def test_dataset2(self):
        self.assertEquals(task.udacify('bob'),'Ubob')

if __name__ == '__main__':
    unittest.main()
