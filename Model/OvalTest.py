# PROGRAMMERS: NHAT-KHAI Duong, Vanessa Garcia-cruz, MC Nguyen

# IMPORT STATEMENTS
from Oval import Oval
import unittest

class OvalTest(unittest.TestCase):
    # CONSTRUCTOR

    # INSTANCE METHODS
    def test_constructor(self):
        object_class = Oval()
        self.assertIn(type(object_class.get_radius_x()), (int, float))
        self.assertIn(type(object_class.get_radius_y()), (int, float))
        self.assertEqual(type(object_class.get_line_color()), str)
        self.assertEqual(type(object_class.get_fill_color()), str)

    def test_constructor_exceptions(self):
        with self.assertRaises(TypeError): Oval(4)
        with self.assertRaises(ValueError): Oval('')
        with self.assertRaises(ValueError): Oval('something.json')
        
    def test_setters(self):
        object_class = Oval()
        object_class.set_radius_x(400)
        self.assertEqual(object_class.get_radius_x(), 400)
        object_class.set_radius_y(200)
        self.assertEqual(object_class.get_radius_y(), 200)
        object_class.set_line_color('purple')
        self.assertEqual(object_class.get_line_color(), 'purple')
        object_class.set_fill_color('white')
        self.assertEqual(object_class.get_fill_color(), 'white')

    def test_setters_exceptions(self):
        object_class = Oval()
        with self.assertRaises(TypeError): object_class.set_radius_x('400')
        with self.assertRaises(ValueError): object_class.set_radius_x(-400)
        with self.assertRaises(TypeError): object_class.set_radius_y('200')
        with self.assertRaises(ValueError): object_class.set_radius_y(-400)
        with self.assertRaises(TypeError): object_class.set_line_color(100)
        with self.assertRaises(ValueError): object_class.set_line_color('indigo')
        with self.assertRaises(TypeError): object_class.set_fill_color(123)
        with self.assertRaises(ValueError): object_class.set_fill_color('indigo')

    def test_area_and_perimeter(self):
        object_class = Oval()
        object_class.set_radius_x(400)
        object_class.set_radius_y(200)
        self.assertAlmostEqual(object_class.area(), 251327.412287183459)
        self.assertAlmostEqual(object_class.perimeter(), 1986.9176531592202)

unittest.main()