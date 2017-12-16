import unittest
from zadanie1 import action, searching
import urllib


class TestCase(unittest.TestCase):


    def test_action(self):
        """when URL is right"""
        self.assertTrue(action('http://www.ii.uni.wroc.pl/~marcinm/dyd/python/'))

    def test_action2(self):
        """ when URL is wrong"""
        with self.assertRaises(urllib.error.HTTPError):
            action('http://www.ii.uniwroc.pl/~marcinm/dyd/python/')

    def test_searching(self):
        """when functions is good"""
        self.assertTrue(searching('http://www.ii.uni.wroc.pl/~marcinm/dyd/python/' , 1))   

    def test_searching2(self):
        self.assertTrue(searching('http://www.ii.uni.wroc.pl/~marcinm/dyd/python/' , 3))

    def test_searching3(self):
        with self.assertRaises(urllib.error.URLError):
            searching('http://www.wp.pl/', 5)
                        

if __name__ == '__main__':
    unittest.main()