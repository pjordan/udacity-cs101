import unittest
import task

class TestSequenceFunctions(unittest.TestCase):
    def test_dataset1(self):
		udacious_univs = [['Udacity',90000,0]]
		self.assertEquals(task.total_enrollment(udacious_univs),(90000,0))

    def test_dataset2(self):
		usa_univs = [ ['California Institute of Technology',2175,37704],
		              ['Harvard',19627,39849],
		              ['Massachusetts Institute of Technology',10566,40732],
		              ['Princeton',7802,37000],
		              ['Rice',5879,35551],
		              ['Stanford',19535,40569],
		              ['Yale',11701,40500]]
		self.assertEquals(task.total_enrollment(usa_univs),(77285,3058581079L))

if __name__ == '__main__':
    unittest.main()
