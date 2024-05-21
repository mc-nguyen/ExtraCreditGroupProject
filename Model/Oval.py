# PROGRAMMERS: NHAT-KHAI Duong, Vanessa Garcia-cruz, MC Nguyen

# IMPORT STATEMENTS
import math

class Oval:
    # CONSTRUCTION
    def __init__(self, radius_x=250, radius_y=200, line_color="blue", fill_color="white"):
        header_err = "Oval.py __init__ "
        available_colors = ["red", "white", "blue", "orange", "white", "black", "green", "yellow", "purple"]
        if type(radius_x) is not int and type(radius_x) is not float:
            raise TypeError(header_err + "radius_x - must be int or float")
        if radius_x <= 0:
            raise ValueError(header_err + "radius_x - must be positive")
        if type(radius_y) is not int and type(radius_y) is not float:
            raise TypeError(header_err + "radius_y - must be int or float")
        if radius_y <= 0:
            raise ValueError(header_err + "radius_y - must be positive")
        if type(line_color) is not str:
            raise TypeError(header_err + "line_color - must be str type")
        if line_color not in available_colors:
            raise ValueError(header_err + "line_color - not a valid color")
        if type(fill_color) is not str:
            raise TypeError(header_err + "fill_color - must be str type")
        if fill_color not in available_colors:
            raise ValueError(header_err + "fill_color - not a valid color")

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
    def perimeter(self): return 2 * math.pi * math.sqrt( (self.__radius_x ** 2 + self.__radius_y ** 2) / 2 )