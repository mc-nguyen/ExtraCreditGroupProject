# PROGRAMMERS: NHAT-KHAI Duong, Vanessa Garcia-cruz, MC Nguyen

# IMPORT STATEMENTS
from Model.Oval import Oval
from Model.Square import Square
from Controller.ApplicationController import ApplicationController
from View.ApplicationView import ApplicationView

# UNITS

# SOLUTION

model_inside = Square()
model_outside = Oval()
view = ApplicationView()
controller = ApplicationController(view, model_inside, model_outside)