# PROGRAMMERS: NHAT-KHAI Duong, Vanessa Garcia-cruz, MC Nguyen

# IMPORT STATEMENTS
import tkinter.filedialog

class ApplicationController:
    # CONSTRUCTOR
    def __init__(self, view, model_inside, model_outside):
        self.__view = view
        self.__model_inside = model_inside
        self.__model_outside = model_outside
        
        self.__view.menu(self)

        self.__view.get_application_window().mainloop()

    # INSTANCE METHODS
    def get_model_inside(self): return self.__model_inside
    def get_model_outside(self): return self.__model_outside

    def file_new(self):
        canvas = self.__view.get_canvas()
        print(self.__model_inside.get_side_length())
        canvas.create_oval(
            ( (500 - self.__model_outside.get_radius_x()) , (350 - self.__model_outside.get_radius_y()) ),
            ( (500 + self.__model_outside.get_radius_x()) , (350 + self.__model_outside.get_radius_y()) ),
            fill=self.__model_outside.get_fill_color(),
            outline=self.__model_outside.get_line_color(),
        )
        canvas.create_rectangle(
            ( 500 - self.__model_inside.get_side_length() , 350 - self.__model_inside.get_side_length() ),
            ( 500 + self.__model_inside.get_side_length() , 350 + self.__model_inside.get_side_length() ),
            fill=self.__model_inside.get_fill_color(),
            outline=self.__model_inside.get_line_color(),
        )
        canvas.pack()

    def file_open(self):
        filename_to_open = tkinter.filedialog.askopenfilename(filetypes=[
            ('JSON files', '*.json'),
            ('XML files', '*.xml')
        ])

        canvas = self.__view.get_canvas()
        canvas.create_oval(
            ( (500 - self.__model_outside.get_radius_x()) , (350 - self.__model_outside.get_radius_y()) ),
            ( (500 + self.__model_outside.get_radius_x()) , (350 + self.__model_outside.get_radius_y()) ),
            fill=self.__model_outside.get_fill_color(),
            outline=self.__model_outside.get_line_color(),
        )
        canvas.create_rectangle(
            ( (500 - self.__model_inside.get_side_length()) , (350 - self.__model_inside.get_side_length()) ),
            ( (500 + self.__model_inside.get_side_length()) , (350 + self.__model_inside.get_side_length()) ),
            fill=self.__model_inside.get_fill_color(),
            outline=self.__model_inside.get_line_color(),
        )
        canvas.pack()

    def view_outside_geometric_shape(self):
        information = 'Radius X: ' + str(self.__model_outside.get_radius_x()) + ' px'
        information += '\nRadius Y: ' + str(self.__model_outside.get_radius_y()) + ' px'
        information += '\nLine Color: ' + self.__model_outside.get_line_color()
        information += '\nFill Color: ' + self.__model_outside.get_fill_color()
        information += '\nArea: ' + str(self.__model_outside.area()) + ' px^2'
        information += '\nPerimeter: ' + str(self.__model_outside.perimeter()) + ' px'
        tkinter.messagebox.showinfo('Outside Geometric Shape - Oval', information)
        self.__view.get_application_window().update()
    
    def view_inside_geometric_shape(self):
        information = 'Side Length: ' + str(self.__model_inside.get_side_length()) + ' px'
        information += '\nLine Color: ' + self.__model_inside.get_line_color()
        information += '\nFill Color: ' + self.__model_inside.get_fill_color()
        information += '\nArea: ' + str(self.__model_inside.area()) + ' px^2'
        information += '\nPerimeter: ' + str(self.__model_inside.perimeter()) + ' px'
        tkinter.messagebox.showinfo('Inside Geometric Shape - Square', information)
        self.__view.get_application_window().update()