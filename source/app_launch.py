import sys  # for argv transferring to QApplication

from uis.NAM_ui import Ui_NAM_window
from uis.menu_ui import Ui_menu_window

from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication


class NAM_window(QtWidgets.QMainWindow, Ui_menu_window):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NAM_window()
        self.ui.setupUi(self)


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
        self.NAM_window = NAM_window()
        self.NAM_window.show()  # Show window


def launch():
    app = QtWidgets.QApplication(sys.argv)  # New QApplication
    menu_window = MenuWindow()  # Create MainWindow

    app.exec()
