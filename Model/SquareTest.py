# PROGRAMMERS: NHAT-KHAI Duong, Vanessa Garcia-cruz, MC Nguyen

# IMPORT STATEMENTS
from Square import Square
import unittest

class OvalTest(unittest.TestCase):
    # CONSTRUCTOR

    # INSTANCE METHODS
    def test_constructor(self):
        object_class = Square()
        self.assertIn(type(object_class.get_side_length()), (int, float))
        self.assertEqual(type(object_class.get_line_color()), str)
        self.assertEqual(type(object_class.get_fill_color()), str)

    def test_constructor_exceptions(self):
        with self.assertRaises(TypeError): Square(4)
        with self.assertRaises(ValueError): Square('')
        with self.assertRaises(ValueError): Square('something.json')
        
    def test_setters(self):
        object_class = Square()
        object_class.set_side_length(100)
        self.assertEqual(object_class.get_side_length(), 100)
        object_class.set_line_color('purple')
        self.assertEqual(object_class.get_line_color(), 'purple')
        object_class.set_fill_color('white')
        self.assertEqual(object_class.get_fill_color(), 'white')

    def test_setters_exceptions(self):
        object_class = Square()
        with self.assertRaises(TypeError): object_class.set_side_length('400')
        with self.assertRaises(ValueError): object_class.set_side_length(-400)
        with self.assertRaises(TypeError): object_class.set_line_color(100)
        with self.assertRaises(ValueError): object_class.set_line_color('indigo')
        with self.assertRaises(TypeError): object_class.set_fill_color(123)
        with self.assertRaises(ValueError): object_class.set_fill_color('indigo')

    def test_area_and_perimeter(self):
        object_class = Square()
        object_class.set_side_length(100)
        self.assertEqual(object_class.area(), 10000)
        self.assertEqual(object_class.perimeter(), 400)

unittest.main()