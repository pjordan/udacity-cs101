import unittest
import task

class TestSequenceFunctions(unittest.TestCase):
    def test_dataset1(self):
        self.assertEquals(task.greatest([4,23,1]),23)

    def test_dataset2(self):
        self.assertEquals(task.greatest([]),0)

if __name__ == '__main__':
    unittest.main()
