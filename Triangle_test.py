import unittest
from Triangle import *

class Triangle_test(unittest.TestCase):
    def test_Triangle(self):
        self.assertEqual(triangle([[2],[3,7],[8,5,6],[6,1,9,3]]),11)
        self.assertEqual(triangle([[3],[6,4],[5,2,7],[9,1,8.6]]),10)
        self.assertEqual(triangle([1]),1)
        self.assertEqual(triangle([]),"List cannot be empty")
if __name__ == '__main__':
    unittest.main()