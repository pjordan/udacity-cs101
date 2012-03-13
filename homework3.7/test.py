import unittest
import task

class TestSequenceFunctions(unittest.TestCase):
    def test_dataset1(self):
		expected = ['http://www.udacity.com/cs101x/index.html']
		self.assertEquals(task.crawl_web("http://www.udacity.com/cs101x/index.html",0),expected)

    def test_dataset2(self):
	    expected = ['http://www.udacity.com/cs101x/index.html', 'http://www.udacity.com/cs101x/flying.html', 'http://www.udacity.com/cs101x/walking.html', 'http://www.udacity.com/cs101x/crawling.html']
		self.assertEquals(task.crawl_web("http://www.udacity.com/cs101x/index.html",1) , expected)

    def test_dataset3(self):
	    expected = ['http://www.udacity.com/cs101x/index.html', 'http://www.udacity.com/cs101x/flying.html', 'http://www.udacity.com/cs101x/walking.html', 'http://www.udacity.com/cs101x/crawling.html', 'http://www.udacity.com/cs101x/kicking.html']
		self.assertEquals(task.crawl_web("http://www.udacity.com/cs101x/index.html",50) , expected)

if __name__ == '__main__':
    unittest.main()
