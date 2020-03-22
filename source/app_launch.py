import sys  # for argv transferring to QApplication
from source.parsing_tools import strip, clear_spaces

from uis.NAM_ui import Ui_NAM_window
from uis.menu_ui import Ui_menu_window

from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
import source.NAM_class as NAM


# Path: pyuic5 -x C:\Users\Anton\PycharmProjects\MLiTA_application\uis\NAM_ui.ui -o C:\Users\Anton\PycharmProjects\MLiTA_application\uis\NAM_ui.py

class NAM_window(QtWidgets.QMainWindow, Ui_menu_window):
    def __init__(self, menu_window):
        super().__init__()
        self.ui = Ui_NAM_window()
        self.ui.setupUi(self)

        self.menu_window = menu_window

        self.ui.calc_button.clicked.connect(self.calculate)
        self.ui.back_button.clicked.connect(self.back_to_menu)

    def back_to_menu(self):
        self.menu_window.show()
        self.close()

    def calculate(self):
        self.ui.output_list.clear()
        self.ui.output_list.setStyleSheet(
            "border-color: rgb(255, 166, 23); "
            "background-color: rgb(85, 85, 85);")

        if self.ui.input_line.hasAcceptableInput():
            if len(self.ui.input_line.text()) > 0:
                if len(self.ui.code_text.toPlainText()) > 0:
                    input_word = self.ui.input_line.text()
                    code = self.ui.code_text.toPlainText()

                    input_word = strip(input_word)  # Clear from spaces

                    # Check if there are spaces inside
                    if input_word.find(' ') == -1:
                        self.ui.input_line.setText(input_word)  # Correct text at the input

                        # Small formatting code: Clear all spaces
                        clear_spaces(code)
                        self.ui.code_text.setText(code)  # Correct text at the code box

                        # Start calculating
                        self.ui.output_list.addItem("Input:\n" + input_word + "\n\nSteps:\n")
                        NAM_worker = NAM.NAM_worker(self.ui.output_list)
                        if NAM_worker.parse_code(code):
                            NAM_worker.calculate(input_word)
                        else:
                            self.error_msg_to_output(NAM_worker.report)

                    else:
                        self.error_msg_to_output("More than one word at the input")
                else:
                    self.error_msg_to_output("Empty code")
            else:
                self.error_msg_to_output("Empty word in input")
        else:
            self.error_msg_to_output("Input is unacceptable")

        # code = self.ui.code_text.text()
        # NAM_worker = NAM.NAM_worker()

    def error_msg_to_output(self, msg):
        self.ui.output_list.setStyleSheet(
            "border-color: rgb(255, 166, 23); "
            "background-color: rgb(85, 85, 85);"
            "color: rgb(255, 0, 0);")
        self.ui.output_list.addItem("Error:\n" + msg)


class MenuWindow(QtWidgets.QMainWindow, Ui_menu_window):
    def __init__(self):
        super().__init__()
        self.ui = Ui_menu_window()
        self.ui.setupUi(self)

        self.show()  # Show window

        # Connect signals to functions
        self.ui.NAM_button.clicked.connect(self.NAM_window_launch)

    def NAM_window_launch(self):
        self.hide()
        self.NAM_window = NAM_window(self)
        self.NAM_window.show()  # Show window


def launch():
    app = QtWidgets.QApplication(sys.argv)  # New QApplication
    menu_window = MenuWindow()  # Create MainWindow

    app.exec()
