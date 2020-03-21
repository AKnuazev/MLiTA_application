# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Anton\PycharmProjects\MLiTA_application\uis\menu_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menu_window(object):
    def setupUi(self, menu_window):
        menu_window.setObjectName("menu_window")
        menu_window.resize(1157, 756)
        menu_window.setStyleSheet("\n"
"* {\n"
"    background: #191919;\n"
"    color: #DDDDDD;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QWidget::item:selected {\n"
"    background: #3D7848;\n"
"}\n"
"\n"
"QCheckBox, QRadioButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator, QCheckBox::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked, QCheckBox::indicator::unchecked {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: none;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover, QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #DDDDDD;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked, QCheckBox::indicator::checked {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #5A5A5A;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover, QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #DDDDDD;\n"
"    background: #DDDDDD;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    margin-top: 6px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -7px;\n"
"    left: 7px;\n"
"}\n"
"\n"
"QScrollBar {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #191919;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height: 15px;\n"
"    margin: 0px 0px 0px 32px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 15px;\n"
"    margin: 32px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #353535;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    border-width: 0px 1px 0px 1px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    border-width: 1px 0px 1px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background:#353535;\n"
"    border: 1px solid #5A5A5A;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line {\n"
"    position: absolute;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    width: 15px;\n"
"    subcontrol-position: left;\n"
"    left: 15px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    top: 15px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 15px;\n"
"    subcontrol-position: top left;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"}\n"
"\n"
"QScrollBar:left-arrow, QScrollBar::right-arrow, QScrollBar::up-arrow, QScrollBar::down-arrow {\n"
"    border: 1px solid #5A5A5A;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"    background: none;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QAbstractButton:pressed {\n"
"    background: #5A5A5A;\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"    show-decoration-selected: 1;\n"
"    selection-background-color: #3D7848;\n"
"    selection-color: #DDDDDD;\n"
"    alternate-background-color: #353535;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: #191919;\n"
"    border: 1px solid #5A5A5A;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QHeaderView::section:selected, QHeaderView::section::checked {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QTableView {\n"
"    gridline-color: #5A5A5A;\n"
"}\n"
"\n"
"QTabBar {\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-radius: 0px;\n"
"    padding: 4px;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-right: 15px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-button, QAbstractSpinBox::down-button {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"    subcontrol-origin: border;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow, QAbstractSpinBox::down-arrow {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QSlider {\n"
"    border: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    margin: 4px 0px 4px 0px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    margin: 0px 4px 0px 4px;\n"
"}\n"
"\n"
"QSlider::handle {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 15px;\n"
"    margin: -4px 0px -4px 0px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 15px;\n"
"    margin: 0px -4px 0px -4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical, QSlider::sub-page:horizontal {\n"
"    background: #3D7848;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical, QSlider::add-page:horizontal {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QLabel {\n"
"    border: none;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    width: 1px;\n"
"    background-color: #3D7848;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    background: #353535;\n"
"}")
        self.groupBox = QtWidgets.QGroupBox(menu_window)
        self.groupBox.setGeometry(QtCore.QRect(120, 60, 921, 631))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.titel_text = QtWidgets.QLabel(self.groupBox)
        self.titel_text.setGeometry(QtCore.QRect(270, 230, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.titel_text.setFont(font)
        self.titel_text.setObjectName("titel_text")
        self.NAM_button = QtWidgets.QPushButton(self.groupBox)
        self.NAM_button.setGeometry(QtCore.QRect(270, 310, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.NAM_button.setFont(font)
        self.NAM_button.setStyleSheet("QPushButton{\n"
"border-color: rgb(255, 166, 23);\n"
"background-color: rgb(85, 85, 85);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 166, 23);}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"background-color: rgb(163, 109, 0);}\n"
"\n"
"")
        self.NAM_button.setObjectName("NAM_button")
        self.MT_button = QtWidgets.QPushButton(self.groupBox)
        self.MT_button.setGeometry(QtCore.QRect(270, 400, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.MT_button.setFont(font)
        self.MT_button.setStyleSheet("QPushButton{\n"
"border-color: rgb(255, 166, 23);\n"
"background-color: rgb(85, 85, 85);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 166, 23);}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"background-color: rgb(163, 109, 0);}")
        self.MT_button.setObjectName("MT_button")
        self.RAM_button = QtWidgets.QPushButton(self.groupBox)
        self.RAM_button.setGeometry(QtCore.QRect(270, 490, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.RAM_button.setFont(font)
        self.RAM_button.setStyleSheet("QPushButton{\n"
"border-color: rgb(255, 166, 23);\n"
"background-color: rgb(85, 85, 85);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 166, 23);}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"background-color: rgb(163, 109, 0);}")
        self.RAM_button.setObjectName("RAM_button")
        self.titel_text_2 = QtWidgets.QLabel(self.groupBox)
        self.titel_text_2.setGeometry(QtCore.QRect(320, 80, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(57)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.titel_text_2.setFont(font)
        self.titel_text_2.setObjectName("titel_text_2")

        self.retranslateUi(menu_window)
        QtCore.QMetaObject.connectSlotsByName(menu_window)

    def retranslateUi(self, menu_window):
        _translate = QtCore.QCoreApplication.translate
        menu_window.setWindowTitle(_translate("menu_window", "Dialog"))
        self.groupBox.setTitle(_translate("menu_window", "Main menu"))
        self.titel_text.setText(_translate("menu_window", "Choose algorithm type:"))
        self.NAM_button.setText(_translate("menu_window", "Normal Markov algorithm"))
        self.MT_button.setText(_translate("menu_window", "Turing machine"))
        self.RAM_button.setText(_translate("menu_window", "Random-access machine"))
        self.titel_text_2.setText(_translate("menu_window", "ML&TA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu_window = QtWidgets.QDialog()
    ui = Ui_menu_window()
    ui.setupUi(menu_window)
    menu_window.show()
    sys.exit(app.exec_())
