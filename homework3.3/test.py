import unittest
import task

class TestSequenceFunctions(unittest.TestCase):
    def test_dataset1(self):
        self.assertEquals(task.product_list([9]),9)

    def test_dataset2(self):
        self.assertEquals(task.product_list([1,2,3,4]),24)

if __name__ == '__main__':
    unittest.main()
