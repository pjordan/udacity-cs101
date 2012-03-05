import unittest
import task

class TestSequenceFunctions(unittest.TestCase):
    def test_dataset1(self):
        self.assertEquals(find_last('aaaa', 'a'),3)

if __name__ == '__main__':
    unittest.main()
