import unittest
from bracket import *


class Testbracket(unittest.TestCase):

    def test_invalid_expression1(self):
        self.assertEqual(IsInputValid("(){"), ("{", 3))
        self.assertEqual(IsInputValid("(abc)[{123}]"),"Valid Expression")
        self.assertEqual(IsInputValid("[1+2(ab]"), ("(", 5))

    def test_no_input(self):
        self.assertRaises(Exception, IsInputValid(""))


if __name__ == '__main__':
    unittest.main()