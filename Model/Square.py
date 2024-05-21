# PROGRAMMERS: NHAT-KHAI Duong, Vanessa Garcia-cruz, MC Nguyen

# IMPORT STATEMENTS
import pickle

class Square:
    # CONSTRUCTION
    def __init__(self, pickle_file='InsideGeometricShapeDefaultValues.pickle'):
        header_err = "Oval.py __init__ pickle_file - "
        if type(pickle_file) is not str:
            raise TypeError(header_err + "line_color - must be str type")
        if not pickle_file.endswith('.pickle'):
            raise ValueError(header_err + "must end with .pickle")
        
        try:
            with open(pickle_file, 'rb') as binary_input_file:
                input_data = pickle.load(binary_input_file)
                if len(input_data) != 3:
                    raise ValueError(header_err + "invalid file content to save values")
                side_length, line_color, fill_color = input_data
        except FileNotFoundError:
            side_length, line_color, fill_color = 100, 'blue', 'white'
            with open('InsideGeometricShapeDefaultValues.pickle', 'wb') as binary_output_file:
                pickle.dump((side_length, line_color, fill_color), binary_output_file)

        self.__side_length = side_length
        self.__line_color = line_color
        self.__fill_color = fill_color

    # INSTANCE METHODS
    def get_side_length(self): return self.__side_length
    def get_line_color(self): return self.__line_color
    def get_fill_color(self): return self.__fill_color

    def set_side_length(self, side_length):
        header_err = "Square.py set_side_length side_length - "
        if type(side_length) is not int and type(side_length) is not float:
            raise TypeError(header_err + "must be int or float")
        if side_length <= 0:
            raise ValueError(header_err + "must be positive")
        self.__side_length = side_length
    
    def set_line_color(self, line_color):
        header_err = "Square.py set_line_color line_color - "
        available_colors = ["red", "white", "blue", "orange", "white", "black", "green", "yellow", "purple"]
        if type(line_color) is not str:
            raise TypeError(header_err + "must be str type")
        if line_color not in available_colors:
            raise ValueError(header_err + "not a valid color")
        self.__line_color = line_color

    def set_fill_color(self, fill_color):
        header_err = "Square.py set_fill_color fill_color - "
        available_colors = ["red", "white", "blue", "orange", "white", "black", "green", "yellow", "purple"]
        if type(fill_color) is not str:
            raise TypeError(header_err + "must be str type")
        if fill_color not in available_colors:
            raise ValueError(header_err + "not a valid color")
        self.__fill_color = fill_color

    def area(self): return self.__side_length ** 2
    def perimeter(self): return self.__side_length * 4