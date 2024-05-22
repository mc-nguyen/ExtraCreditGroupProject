# PROGRAMMERS: NHAT-KHAI Duong, Vanessa Garcia-cruz, MC Nguyen

# IMPORT STATEMENTS
import math
import pickle

class Oval:
    # CONSTRUCTION
    def __init__(self, pickle_file='OutsideGeometricShapeDefaultValues.pickle'):
        header_err = "Oval.py __init__ pickle_file - "
        if type(pickle_file) is not str:
            raise TypeError(header_err + "line_color - must be str type")
        if not pickle_file.endswith('.pickle'):
            raise ValueError(header_err + "must end with .pickle")
        
        try:
            with open(pickle_file, 'rb') as binary_input_file:
                input_data = pickle.load(binary_input_file)
                if len(input_data) != 4:
                    raise ValueError(header_err + "invalid file content to save values")
                radius_x, radius_y, line_color, fill_color = input_data
        except FileNotFoundError:
            radius_x, radius_y, line_color, fill_color = 300, 150, 'red', 'yellow'
            with open('OutsideGeometricShapeDefaultValues.pickle', 'wb') as binary_output_file:
                pickle.dump((radius_x, radius_y, line_color, fill_color), binary_output_file)

        self.__radius_x = radius_x
        self.__radius_y = radius_y
        self.__line_color = line_color
        self.__fill_color = fill_color

    # INSTANCE METHODS
    def get_radius_x(self): return self.__radius_x
    def get_radius_y(self): return self.__radius_y
    def get_line_color(self): return self.__line_color
    def get_fill_color(self): return self.__fill_color

    def set_radius_x(self, radius_x):
        header_err = "Oval.py set_radius_x radius_x - "
        if type(radius_x) is not int and type(radius_x) is not float:
            raise TypeError(header_err + "must be int or float")
        if radius_x <= 0:
            raise ValueError(header_err + "must be positive")
        self.__radius_x = radius_x

    def set_radius_y(self, radius_y):
        header_err = "Oval.py set_radius_y radius_y - "
        if type(radius_y) is not int and type(radius_y) is not float:
            raise TypeError(header_err + "must be int or float")
        if radius_y <= 0:
            raise ValueError(header_err + "must be positive")
        self.__radius_y = radius_y
    
    def set_line_color(self, line_color):
        header_err = "Oval.py set_line_color line_color - "
        available_colors = ["red", "white", "blue", "orange", "white", "black", "green", "yellow", "purple"]
        if type(line_color) is not str:
            raise TypeError(header_err + "must be str type")
        if line_color not in available_colors:
            raise ValueError(header_err + "not a valid color")
        self.__line_color = line_color

    def set_fill_color(self, fill_color):
        header_err = "Oval.py set_fill_color fill_color - "
        available_colors = ["red", "white", "blue", "orange", "white", "black", "green", "yellow", "purple"]
        if type(fill_color) is not str:
            raise TypeError(header_err + "must be str type")
        if fill_color not in available_colors:
            raise ValueError(header_err + "not a valid color")
        self.__fill_color = fill_color

    def area(self): return self.__radius_x * self.__radius_y * math.pi
    def perimeter(self): return math.pi * math.sqrt( 2 * (self.__radius_x ** 2 + self.__radius_y ** 2) )