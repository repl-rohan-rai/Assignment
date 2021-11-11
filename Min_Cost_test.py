import unittest
from Min_Cost import *

class Min_Cost_test(unittest.TestCase):
    def test_Min_Cost(self):
        self.assertEqual(Min_Cost([20,10,4,50,100],5),14)
        self.assertEqual(Min_Cost([1,10,4,50,100],0),"Weight cannot be zero or less than zero")
        self.assertEqual(Min_Cost([1,2,3,4,5],5),5)
        self.assertEqual(Min_Cost([],5),-1)
if __name__ == '__main__':
    unittest.main()