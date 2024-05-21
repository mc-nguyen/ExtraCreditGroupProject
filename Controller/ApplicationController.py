# PROGRAMMERS: NHAT-KHAI Duong, Vanessa Garcia-cruz, MC Nguyen

# IMPORT STATEMENTS
import tkinter.filedialog
import tkinter.simpledialog
import pickle
import xml.etree.ElementTree as ET

class ApplicationController:
    # CONSTRUCTOR
    def __init__(self, view, model_inside, model_outside):
        self.__model_inside = model_inside
        self.__model_outside = model_outside
        
        self.__view = view
        self.__view.menu(self)
        self.__view.get_application_window().mainloop()

    # INSTANCE METHODS
    def file_new(self):
        canvas = self.__view.get_canvas()
        canvas.delete('all')
        canvas.create_oval(
            ( (500 - self.__model_outside.get_radius_x()) , (350 - self.__model_outside.get_radius_y()) ),
            ( (500 + self.__model_outside.get_radius_x()) , (350 + self.__model_outside.get_radius_y()) ),
            fill=self.__model_outside.get_fill_color(),
            outline=self.__model_outside.get_line_color(),
        )
        side_length = self.__model_inside.get_side_length()
        canvas.create_rectangle(
            ( 500 - side_length / 2 , 350 - side_length / 2 ),
            ( 500 + side_length / 2 , 350 + side_length / 2 ),
            fill=self.__model_inside.get_fill_color(),
            outline=self.__model_inside.get_line_color(),
        )
        canvas.pack()

    def file_open(self):
        filename_to_open = tkinter.filedialog.askopenfilename(filetypes=[
            ('JSON files', '*.json'),
            ('XML files', '*.xml')
        ])

        if filename_to_open.endswith('.xml'):
            root = ET.parse(filename_to_open).getroot()
            for child in root:
                print(child.tag, child.attrib)

        self.file_new()

    def save_as_xml(self):
        root = ET.Element('DefaultValue')
        tree = ET.ElementTree(root)

        outside_oval = ET.SubElement(root, "OutsideOval")
        attribute = ET.SubElement(outside_oval, "RadiusX")
        attribute.text = str(self.__model_outside.get_radius_x())
        attribute = ET.SubElement(outside_oval, "RadiusY")
        attribute.text = str(self.__model_outside.get_radius_y())
        attribute = ET.SubElement(outside_oval, "LineColor")
        attribute.text = str(self.__model_outside.get_line_color())
        attribute = ET.SubElement(outside_oval, "FillColor")
        attribute.text = str(self.__model_outside.get_fill_color())

        inside_oval = ET.SubElement(root, "InsideSquare")
        attribute = ET.SubElement(inside_oval, "SideLength")
        attribute.text = str(self.__model_inside.get_side_length())
        attribute = ET.SubElement(inside_oval, "LineColor")
        attribute.text = str(self.__model_inside.get_line_color())
        attribute = ET.SubElement(inside_oval, "FillColor")
        attribute.text = str(self.__model_inside.get_fill_color())

        with open('OutsideGeometricShapeDefaultValues.xml', 'w') as output_file:
            tree.write(output_file)

    def edit_outside_geometric_shape(self):
        try:
            self.__model_outside.set_radius_x(tkinter.simpledialog.askfloat("Radius X", "Enter size of radius x:"))
            self.__model_outside.set_radius_y(tkinter.simpledialog.askfloat("Radius Y", "Enter size of radius y:"))
            self.__model_outside.set_line_color(tkinter.simpledialog.askstring("Line Color", "Enter color for outline:"))
            self.__model_outside.set_fill_color(tkinter.simpledialog.askstring("Fill Color", "Enter color for fill:"))
            self.file_new()
        except ValueError as err:
            tkinter.messagebox.showerror("Error Found", err)
        except TypeError as err:
            tkinter.messagebox.showerror("Error Found", err)
            
        self.__view.get_application_window().update()

    def edit_inside_geometric_shape(self):
        try:
            self.__model_inside.set_side_length(tkinter.simpledialog.askfloat("Side Length", "Enter size of side length:"))
            self.__model_inside.set_line_color(tkinter.simpledialog.askstring("Line Color", "Enter color for outline:"))
            self.__model_inside.set_fill_color(tkinter.simpledialog.askstring("Fill Color", "Enter color for fill:"))
            self.file_new()
        except ValueError as err:
            tkinter.messagebox.showerror("Error Found", err)
        except TypeError as err:
            tkinter.messagebox.showerror("Error Found", err)
            
        self.__view.get_application_window().update()

    def edit_pickle_file_outside_geometric_shape(self):
        self.edit_outside_geometric_shape()
        with open('OutsideGeometricShapeDefaultValues.pickle', 'wb') as binary_output_file:
            pickle.dump((
                self.__model_outside.get_radius_x(),
                self.__model_outside.get_radius_y(),
                self.__model_outside.get_line_color(),
                self.__model_outside.get_fill_color()
            ), binary_output_file)

    def edit_pickle_file_inside_geometric_shape(self):
        self.edit_inside_geometric_shape()
        with open('InsideGeometricShapeDefaultValues.pickle', 'wb') as binary_output_file:
            pickle.dump((
                self.__model_inside.get_side_length(),
                self.__model_inside.get_line_color(),
                self.__model_inside.get_fill_color()
            ), binary_output_file)

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