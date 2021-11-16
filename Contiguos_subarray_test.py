import unittest
from Contiguos_subarray import *

class Contiguos_subarray_test(unittest.TestCase):
    def test_Contiguos_subarray(self):
        self.assertEqual(Contiguos_subarray([-2,-3,4,-1,-2,1,5,-3],8),7)
        self.assertEqual(Contiguos_subarray([1,2,3],3),6)
        self.assertEqual(Contiguos_subarray([0],1),0)
        self.assertEqual(Contiguos_subarray([],0),"List cannot be empty")
if __name__ == '__main__':
    unittest.main()