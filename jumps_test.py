import unittest
from jumps import *

class jumps_test(unittest.TestCase):
    def test_jumps(self):
        self.assertEqual(jumps([1,3,5,8,9,2,6,7,6,8,9],11),3)
        self.assertEqual(jumps([0],1),"Jump length cannot be less than or equal to zero")
        self.assertEqual(jumps([],0),"List cannot be empty")
        self.assertEqual(jumps([-1,3,2],3),"Jump length cannot be less than or equal to zero")
if __name__ == '__main__':
    unittest.main()