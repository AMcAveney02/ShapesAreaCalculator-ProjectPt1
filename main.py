# This imports the controls for the buttons in the program from controller.py
from controller import *

# This allows the program to run within a window and launches the program.
def main() -> None:
    app = QApplication([])
    # calling the controller function to control the window itself
    window = Controller()
    # showing the window
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

