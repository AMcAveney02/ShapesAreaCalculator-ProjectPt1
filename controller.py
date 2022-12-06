# This imports the PyQt5 widgets.
from PyQt5.QtWidgets import *
# This imports the program layout made in QTDesigner into the controller.
from gui import *
# This imports the functions I created for calculations into the controller.
from functions import *



# These two commands ensure that the window isn't smashed together when the program is run.
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


# Created a class for the controller
class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        # These four lines control clicking the compute button in each window of the program
        # Each line calls a separate function for computation of the inpput information.
        self.circle_computeButton.clicked.connect(lambda: self.compute_circle())
        self.rectangle_computeButton.clicked.connect(lambda: self.compute_rectangle())
        self.square_computeButton.clicked.connect(lambda: self.compute_square())
        self.triangle_computeButton.clicked.connect(lambda: self.compute_triangle())
        self.power_computeButton.clicked.connect(lambda: self.compute_power())

# Creates the function for circle area computation.
    def compute_circle(self) -> None:
        """
        Funciton to display the area of the circle from the inputed values
        :return: Area of the circle from inputed values and called area_of_circle function displayed to 8 decimal places
        """
        try:
            radius = float(self.circle_input.text()) # Retrieves input in label and converts it to a float

            if radius > 0: # This checks to make sure the input value isn't negative
                area_of_circle(radius) # Calls the function with the input, calculating the area of the circle
                area = area_of_circle(radius) # Creates the variable area and assigns it to computed area of the circle
                self.circle_answer_display.setText(f"{area:.8f}") # displays the calculated area of a circle to the answer display label
                self.circle_input.setText('') # Clears the input box
            elif radius < 0: # Sets an action for if the input value is less than 0
                self.circle_answer_display.setText( # Displays the below message if the input value is less than 0
                    "Only enter positive integers and floats."
                )
                self.circle_input.setText('') # Clears the input box

        except ValueError: # Creates an exception for value errors
            self.circle_answer_display.setText(
                "Only enter positive integers and floats."
            )
            self.circle_input.setText('')

    # Creates function for rectangle area computation
    def compute_rectangle(self) -> None:
        """
        Function to display the area of a rectangle from inputed values of length and width
        :return: Area of the rectangle from inputed values and called area_of_rectangle function displayed to 8 decimal places
        """
        try: # retreives inpuit from length and width input boxes and converts the input to a float
            length = float(self.rectangle_length_input.text())
            width = float(self.rectangle_width_input.text())

            if length and width > 0: # this checks to make sure the input is not negative and then calls the area_of_rectangle function
                area_of_rectangle(length, width)
                area = area_of_rectangle(length, width) # assigns the answer of the function w/input to variable area
                self.rectangle_answer_display.setText(f"{area:.8f}") # sets the answer to 8 decimal places and displays it
                self.rectangle_width_input.setText('') # these two clear the input boxes
                self.rectangle_length_input.setText('')
            elif length < 0: # tells the user to input correct values if the input is negative
                self.rectangle_answer_display.setText(
                    "Only enter positive integers and floats." # sets answer display to show correcting message
                )
                self.rectangle_width_input.setText('') # clears the input boxes
                self.rectangle_length_input.setText('')
            elif width < 0: # tells the user to input correct values if the input is negative
                self.rectangle_answer_display.setText( # sets answer display to show correcting message
                    "Only enter positive integers and floats."
                )
                self.rectangle_width_input.setText('') # clears the input boxes
                self.rectangle_length_input.setText('')

        except ValueError: # raises a value error if the input is negative
            self.rectangle_answer_display.setText(
                "Only enter positive integers and floats." # sets answer display to show correcting message
            )
            self.rectangle_width_input.setText('')
            self.rectangle_length_input.setText('') # clears the input boxes


    def compute_square(self) -> None: # Creates the square computation function
        """
        Function to display the area of a square from the inputed values
        :return: Area of the square from inputed values and called area_of_square function displayed to 8 decimal places
        """
        try:
            square_length = float(self.square_input.text()) # Takes the input and converts it to a float, assigning it to the length variable

            if square_length > 0: # Checks to make sure input is not negative
                area_of_square(square_length) # Calls the function with the input value
                area = area_of_square(square_length) # Assigns the result of the function to the area variable
                self.square_answer_display.setText(f"{area:.8f}") # Displays the answer to the answer display to 8 decimal points
                self.square_input.setText('') # Clears the input box of any text
            elif square_length < 0: # Checks to make sure input is not negative
                self.square_answer_display.setText( # Displays the below message if the input value is less than 0
                    "Only enter positive integers and floats."
                )
                self.square_input.setText('')

        except ValueError: # Provides an exception for a value error
            self.square_answer_display.setText( # Displays the below message if there is a value error
                "Only enter positive integers and floats."
            )
            self.square_input.setText('')


    def compute_triangle(self) -> None: # Creates the compute_triangle function for when the compute button is clicked on the triangle tab
        """
        Function to display the area of a triangle from the inputed base and height values
        :return: Area of a triangle from inputed values and called area_of_triangle function displayed to 8 decimal places
        """
        try: # takes the input from base and height input boxes and converts it to a float, assigning it to the base and height variables
            base = float(self.triangle_base_input.text())
            height = float(self.triangle_height_input.text())

            if base and height > 0: # checks to make sure input for base and height is greater than 0, if it is the rest of the function executes
                area_of_triangle(base, height) # calls the function with the input height and base values
                area = area_of_triangle(base, height) # assings the result of the called area_of_triangle function to the variable area
                self.triangle_answer_display.setText(f"{area:.8f}") # displays the answer to the answer display to 8 decimal points
                self.triangle_base_input.setText('') # both of these clear the input boxes of text
                self.triangle_height_input.setText('')
            elif base < 0: # checks if the input for base is negative
                self.triangle_answer_display.setText( # displays the below correcting message
                    "Only enter positive integers and floats."
                )
                self.triangle_base_input.setText('') # clears both input text boxes
                self.triangle_height_input.setText('')
            elif height < 0: # checks if the input for height is negative
                self.triangle_answer_display.setText( # displays the below correcting message
                    "Only enter positive integers and floats."
                )
                self.triangle_base_input.setText('') # clears both input text boxes
                self.triangle_height_input.setText('')

        except TypeError: # this provides an exception for a type error (string input)
            self.triangle_answer_display.setText( # displays the below correcting message
                "Only enter positive integers and floats."
            )
            self.triangle_base_input.setText('') # clears both input text boxes
            self.triangle_height_input.setText('')
        except ValueError: # this provides an exception for a value error (negative value)
            self.triangle_answer_display.setText( # displays the below correcting message
                "Only enter positive integers and floats."
            )
            self.triangle_base_input.setText('') # clears both input text boxes
            self.triangle_height_input.setText('')


    def compute_power(self) -> None: # Creates the power computation function
        """
        Function to display a number raised to an exponent
        :return: Number raised to an exponent and called power_of_number function displayed to 8 decimal places
        """
        try:
            number_base = float(self.power_base_input.text()) # assigns input from the base entry box to the variable (retrieves input)
            exponent = float(self.power_power_inpuit.text()) #assigns input from the exponent entry box to the variable (retrieves input)

            if number_base and exponent is not str: # checks to make sure that the input is not a string, but only a float or integer
                power_of_number(number_base, exponent) # calls the function to be performed with the input
                power = power_of_number(number_base, exponent) # assigns the answer from the called function to the variable power
                self.power_answer_display.setText(f"{power:.8f}") # displays the answer to the answer label to 8 decimal points
                self.power_base_input.setText('') # These two commands clears the input box of any text
                self.power_power_inpuit.setText('')

        except ValueError: # Raises an exception for a value error
            self.power_answer_display.setText( # Displays the below error message for a value error
                "Only enter integers and floats."
            )
            self.power_base_input.setText('') # clears both input boxes
            self.power_power_inpuit.setText('')

