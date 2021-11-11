import unittest
from Factorial_Recursive import *

class Factorial_RecursiveTest(unittest.TestCase):
    def test_Factorial_Recursive(self):
        self.assertEqual(fact(10),3628800)
        self.assertEqual(fact(5),120)
        self.assertEqual(fact(0),1)
        self.assertEqual(fact(1),1)
if __name__ == '__main__':
    unittest.main()