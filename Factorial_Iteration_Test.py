import unittest
from Factorial_Iteration import *

class factTest(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(fact(10),3628800)
        self.assertEqual(fact(5),120)
        self.assertEqual(fact(0),1)
        self.assertEqual(fact(1),1)
if __name__ == '__main__':
    unittest.main()