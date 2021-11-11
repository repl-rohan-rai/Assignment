import unittest
from longest_substring import *

class longest_substring_test(unittest.TestCase):
    def test_longest_substring(self):
        self.assertEqual(longest_substring("123123",6),6)
        self.assertEqual(longest_substring("1538023",7),4)
        self.assertEqual(longest_substring("12a34",5),"Invalid String!.Contains non-integer values")
if __name__ == '__main__':
    unittest.main()