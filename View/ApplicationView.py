# PROGRAMMERS: NHAT-KHAI Duong, Vanessa Garcia-cruz, MC Nguyen

# IMPORT STATEMENTS
import tkinter
import tkinter.messagebox

class ApplicationView:
    # CONSTRUCTOR
    def __init__(self):
        self.__application_window = tkinter.Tk()
        self.__application_window.title("Group Project: Square inside Oval")
        self.__application_window.geometry("1024x720")

        self.__application_menu = tkinter.Menu(self.__application_window)

        self.__file_menu = tkinter.Menu(self.__application_menu)
        self.__application_menu.add_cascade(label='File', menu=self.__file_menu)
        
        self.__edit_menu = tkinter.Menu(self.__application_menu)
        self.__application_menu.add_cascade(label='Edit', menu=self.__edit_menu)
        
        self.__view_menu = tkinter.Menu(self.__application_menu)
        self.__application_menu.add_cascade(label='View', menu=self.__view_menu)
        
        self.__help_menu = tkinter.Menu(self.__application_menu)
        self.__help_menu.add_command(label='About', command=self.about)
        self.__application_menu.add_cascade(label='Help', menu=self.__help_menu)

        self.__application_window['menu'] = self.__application_menu

        self.__canvas = tkinter.Canvas(self.__application_window, bg='black', width=1000, height=700)

    # INSTANCE METHODS
    def get_application_window(self): return self.__application_window
    def get_canvas(self): return self.__canvas
    def menu(self, controller):         
        self.__file_menu.add_command(label='New', command=controller.file_new)
        self.__file_menu.add_command(label='Open', command=controller.file_open)
        self.__file_menu.add_command(label='Save as XML')
        self.__file_menu.add_command(label='Save as JSON')
        
        self.__edit_menu.add_command(label='One for each instance variable of Outside Geometric Shape')
        self.__edit_menu.add_command(label='One for each instance variable of Inside Geometric Shape')
        self.__edit_menu.add_command(label='One for each Pickle File Default Value of Outside Geometric Shape')
        self.__edit_menu.add_command(label='One for each Pickle File Default Value of Inside Geometric Shape')
        
        self.__view_menu.add_command(label='Outside Geometric Shape', command=controller.view_outside_geometric_shape)
        self.__view_menu.add_command(label='Inside Geometric Shape', command=controller.view_inside_geometric_shape)

    def about(self):
        information = "Extra Credits - Group Project:".upper() + "\n\tSquare inside Oval"
        information += "\nProgrammers:".upper() + "\n\tNHAT-KHAI Duong\n\tVanessa Garcia-cruz\n\tMC Nguyen"
        tkinter.messagebox.showinfo('About', information)
        self.__application_window.update()