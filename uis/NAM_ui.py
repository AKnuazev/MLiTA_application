# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Anton\PycharmProjects\MLiTA_application\uis\NAM_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NAM_window(object):
    def setupUi(self, NAM_window):
        NAM_window.setObjectName("NAM_window")
        NAM_window.resize(1074, 769)
        NAM_window.setStyleSheet("/*\n"
"    Copyright 2013 Emanuel Claesson\n"
"\n"
"    Licensed under the Apache License, Version 2.0 (the \"License\");\n"
"    you may not use this file except in compliance with the License.\n"
"    You may obtain a copy of the License at\n"
"\n"
"        http://www.apache.org/licenses/LICENSE-2.0\n"
"\n"
"    Unless required by applicable law or agreed to in writing, software\n"
"    distributed under the License is distributed on an \"AS IS\" BASIS,\n"
"    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n"
"    See the License for the specific language governing permissions and\n"
"    limitations under the License.\n"
"*/\n"
"\n"
"/*\n"
"    COLOR_DARK     = #191919\n"
"    COLOR_MEDIUM   = #353535\n"
"    COLOR_MEDLIGHT = #5A5A5A\n"
"    COLOR_LIGHT    = #DDDDDD\n"
"    COLOR_ACCENT   = #3D7848\n"
"*/\n"
"\n"
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
        self.centralwidget = QtWidgets.QWidget(NAM_window)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(80, 60, 921, 631))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.listView = QtWidgets.QListView(self.groupBox)
        self.listView.setGeometry(QtCore.QRect(630, 130, 241, 421))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listView.setFont(font)
        self.listView.setStyleSheet("border-color: rgb(255, 166, 23);background-color: rgb(85, 85, 85);")
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(690, 60, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.input_line = QtWidgets.QLineEdit(self.groupBox)
        self.input_line.setGeometry(QtCore.QRect(70, 130, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.input_line.setFont(font)
        self.input_line.setStyleSheet("border-color: rgb(255, 166, 23);\n"
"background-color: rgb(85, 85, 85);")
        self.input_line.setObjectName("input_line")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(240, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.code_text = QtWidgets.QTextEdit(self.groupBox)
        self.code_text.setGeometry(QtCore.QRect(70, 260, 431, 291))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.code_text.setFont(font)
        self.code_text.setStyleSheet("border-color: rgb(255, 166, 23);background-color: rgb(85, 85, 85);")
        self.code_text.setObjectName("code_text")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(240, 200, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.calc_button = QtWidgets.QPushButton(self.groupBox)
        self.calc_button.setGeometry(QtCore.QRect(390, 130, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.calc_button.setFont(font)
        self.calc_button.setStyleSheet("QPushButton{\n"
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
        self.calc_button.setObjectName("calc_button")
        self.back_button = QtWidgets.QPushButton(self.groupBox)
        self.back_button.setGeometry(QtCore.QRect(860, 600, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("QPushButton{\n"
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
        self.back_button.setObjectName("back_button")
        self.groupBox.raise_()
        self.back_button.raise_()
        NAM_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(NAM_window)
        QtCore.QMetaObject.connectSlotsByName(NAM_window)

    def retranslateUi(self, NAM_window):
        _translate = QtCore.QCoreApplication.translate
        NAM_window.setWindowTitle(_translate("NAM_window", "MainWindow"))
        self.groupBox.setTitle(_translate("NAM_window", "Normal Markov Algorithm"))
        self.label.setText(_translate("NAM_window", "Output"))
        self.label_2.setText(_translate("NAM_window", "Input"))
        self.label_3.setText(_translate("NAM_window", "Code"))
        self.calc_button.setText(_translate("NAM_window", "Calculate"))
        self.back_button.setText(_translate("NAM_window", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NAM_window = QtWidgets.QMainWindow()
    ui = Ui_NAM_window()
    ui.setupUi(NAM_window)
    NAM_window.show()
    sys.exit(app.exec_())
