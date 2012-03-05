import unittest
import task

class TestSequenceFunctions(unittest.TestCase):
    def test_dataset1(self):
        self.assertEquals(task.median(1,2,3),2)

    def test_dataset2(self):
        self.assertEquals(task.median(3,2,1),2)

    def test_dataset3(self):
        self.assertEquals(task.median(2,3,1),2)

    def test_dataset4(self):
        self.assertEquals(task.median(2,1,3),2)

    def test_dataset5(self):
        self.assertEquals(task.median(3,1,2),2)

    def test_dataset6(self):
        self.assertEquals(task.median(1,3,2),2)

    def test_dataset7(self):
        self.assertEquals(task.median(1,3,1),1)

    def test_dataset8(self):
        self.assertEquals(task.median(1,3,3),3)

    def test_dataset9(self):
        self.assertEquals(task.median(3,3,3),3)

if __name__ == '__main__':
    unittest.main()
