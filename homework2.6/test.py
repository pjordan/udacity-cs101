import unittest
import task

class TestSequenceFunctions(unittest.TestCase):
    def test_dataset1(self):
        self.assertEquals(task.find_last('aaaa', 'a'),3)

    def test_dataset2(self):
        self.assertEquals(task.find_last('aaaa', 'c'),-1)

    def test_dataset3(self):
        self.assertEquals(task.find_last('aaab', 'b'),3)

if __name__ == '__main__':
    unittest.main()
