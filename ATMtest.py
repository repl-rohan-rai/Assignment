import unittest
from ATM import *

class ATMTest(unittest.TestCase):
    def test_ATM(self):
        self.assertEqual(ATM(555),{500: 1, 100: 0, 50: 1, 10: 0, 5: 0})
        self.assertEqual(ATM(600),{100: 6, 50: 0, 500: 0, 10: 0, 5: 0})
        self.assertEqual(ATM(0),("Invalid Amount"))
        self.assertEqual(ATM(12),("Invalid Amount"))
if __name__ == '__main__':
    unittest.main()