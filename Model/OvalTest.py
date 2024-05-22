# PROGRAMMERS: NHAT-KHAI Duong, Vanessa Garcia-cruz, MC Nguyen

# IMPORT STATEMENTS
from Oval import Oval
import unittest

class OvalTest(unittest.TestCase):
    # CONSTRUCTOR

    # INSTANCE METHODS
    def test_constructor(self):
        with self.assertRaises(TypeError): Oval(4)
        with self.assertRaises(ValueError): Oval('')
        with self.assertRaises(ValueError): Oval('something.json')

        

unittest.main()