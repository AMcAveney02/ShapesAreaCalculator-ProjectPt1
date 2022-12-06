# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# This is all the code from QTDesigner for the area shapes calculator.
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 601, 551))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.tab_selector = QtWidgets.QTabWidget(self.frame)
        self.tab_selector.setGeometry(QtCore.QRect(0, 0, 591, 541))
        self.tab_selector.setObjectName("tab_selector")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.power_label = QtWidgets.QLabel(self.widget)
        self.power_label.setGeometry(QtCore.QRect(130, 10, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.power_label.setFont(font)
        self.power_label.setObjectName("power_label")
        self.power_label_2 = QtWidgets.QLabel(self.widget)
        self.power_label_2.setGeometry(QtCore.QRect(230, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.power_label_2.setFont(font)
        self.power_label_2.setObjectName("power_label_2")
        self.power_base_input = QtWidgets.QLineEdit(self.widget)
        self.power_base_input.setGeometry(QtCore.QRect(180, 100, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.power_base_input.setFont(font)
        self.power_base_input.setObjectName("power_base_input")
        self.power_label_3 = QtWidgets.QLabel(self.widget)
        self.power_label_3.setGeometry(QtCore.QRect(220, 140, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.power_label_3.setFont(font)
        self.power_label_3.setObjectName("power_label_3")
        self.power_power_inpuit = QtWidgets.QLineEdit(self.widget)
        self.power_power_inpuit.setGeometry(QtCore.QRect(180, 170, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.power_power_inpuit.setFont(font)
        self.power_power_inpuit.setObjectName("power_power_inpuit")
        self.power_computeButton = QtWidgets.QPushButton(self.widget)
        self.power_computeButton.setGeometry(QtCore.QRect(240, 220, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.power_computeButton.setFont(font)
        self.power_computeButton.setObjectName("power_computeButton")
        self.power_answer_label = QtWidgets.QLabel(self.widget)
        self.power_answer_label.setGeometry(QtCore.QRect(230, 290, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.power_answer_label.setFont(font)
        self.power_answer_label.setObjectName("power_answer_label")
        self.power_answer_display = QtWidgets.QLabel(self.widget)
        self.power_answer_display.setGeometry(QtCore.QRect(130, 330, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.power_answer_display.setFont(font)
        self.power_answer_display.setText("")
        self.power_answer_display.setAlignment(QtCore.Qt.AlignCenter)
        self.power_answer_display.setObjectName("power_answer_display")
        self.tab_selector.addTab(self.widget, "")
        self.circle_tab = QtWidgets.QWidget()
        self.circle_tab.setObjectName("circle_tab")
        self.circle_label1 = QtWidgets.QLabel(self.circle_tab)
        self.circle_label1.setGeometry(QtCore.QRect(80, 20, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.circle_label1.setFont(font)
        self.circle_label1.setObjectName("circle_label1")
        self.circle_label2 = QtWidgets.QLabel(self.circle_tab)
        self.circle_label2.setGeometry(QtCore.QRect(230, 90, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.circle_label2.setFont(font)
        self.circle_label2.setObjectName("circle_label2")
        self.circle_input = QtWidgets.QLineEdit(self.circle_tab)
        self.circle_input.setGeometry(QtCore.QRect(170, 120, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.circle_input.setFont(font)
        self.circle_input.setObjectName("circle_input")
        self.circle_computeButton = QtWidgets.QPushButton(self.circle_tab)
        self.circle_computeButton.setGeometry(QtCore.QRect(230, 170, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.circle_computeButton.setFont(font)
        self.circle_computeButton.setObjectName("circle_computeButton")
        self.circle_answer_label = QtWidgets.QLabel(self.circle_tab)
        self.circle_answer_label.setGeometry(QtCore.QRect(220, 250, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.circle_answer_label.setFont(font)
        self.circle_answer_label.setObjectName("circle_answer_label")
        self.circle_answer_display = QtWidgets.QLabel(self.circle_tab)
        self.circle_answer_display.setGeometry(QtCore.QRect(120, 300, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.circle_answer_display.setFont(font)
        self.circle_answer_display.setText("")
        self.circle_answer_display.setAlignment(QtCore.Qt.AlignCenter)
        self.circle_answer_display.setObjectName("circle_answer_display")
        self.tab_selector.addTab(self.circle_tab, "")
        self.rectangle_tab = QtWidgets.QWidget()
        self.rectangle_tab.setObjectName("rectangle_tab")
        self.rectangle_label = QtWidgets.QLabel(self.rectangle_tab)
        self.rectangle_label.setGeometry(QtCore.QRect(50, 20, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.rectangle_label.setFont(font)
        self.rectangle_label.setObjectName("rectangle_label")
        self.rectangle_label_2 = QtWidgets.QLabel(self.rectangle_tab)
        self.rectangle_label_2.setGeometry(QtCore.QRect(230, 80, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.rectangle_label_2.setFont(font)
        self.rectangle_label_2.setObjectName("rectangle_label_2")
        self.rectangle_length_input = QtWidgets.QLineEdit(self.rectangle_tab)
        self.rectangle_length_input.setGeometry(QtCore.QRect(170, 120, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.rectangle_length_input.setFont(font)
        self.rectangle_length_input.setObjectName("rectangle_length_input")
        self.rectangle_computeButton = QtWidgets.QPushButton(self.rectangle_tab)
        self.rectangle_computeButton.setGeometry(QtCore.QRect(230, 250, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rectangle_computeButton.setFont(font)
        self.rectangle_computeButton.setObjectName("rectangle_computeButton")
        self.rectangle_answer_label = QtWidgets.QLabel(self.rectangle_tab)
        self.rectangle_answer_label.setGeometry(QtCore.QRect(220, 330, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.rectangle_answer_label.setFont(font)
        self.rectangle_answer_label.setObjectName("rectangle_answer_label")
        self.rectangle_answer_display = QtWidgets.QLabel(self.rectangle_tab)
        self.rectangle_answer_display.setGeometry(QtCore.QRect(120, 380, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.rectangle_answer_display.setFont(font)
        self.rectangle_answer_display.setText("")
        self.rectangle_answer_display.setAlignment(QtCore.Qt.AlignCenter)
        self.rectangle_answer_display.setObjectName("rectangle_answer_display")
        self.rectangle_label_3 = QtWidgets.QLabel(self.rectangle_tab)
        self.rectangle_label_3.setGeometry(QtCore.QRect(230, 160, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.rectangle_label_3.setFont(font)
        self.rectangle_label_3.setObjectName("rectangle_label_3")
        self.rectangle_width_input = QtWidgets.QLineEdit(self.rectangle_tab)
        self.rectangle_width_input.setGeometry(QtCore.QRect(170, 200, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.rectangle_width_input.setFont(font)
        self.rectangle_width_input.setObjectName("rectangle_width_input")
        self.label_6 = QtWidgets.QLabel(self.rectangle_tab)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 601, 531))
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.rectangle_label.raise_()
        self.rectangle_label_2.raise_()
        self.rectangle_length_input.raise_()
        self.rectangle_computeButton.raise_()
        self.rectangle_answer_label.raise_()
        self.rectangle_answer_display.raise_()
        self.rectangle_label_3.raise_()
        self.rectangle_width_input.raise_()
        self.tab_selector.addTab(self.rectangle_tab, "")
        self.square_tab = QtWidgets.QWidget()
        self.square_tab.setObjectName("square_tab")
        self.square_label = QtWidgets.QLabel(self.square_tab)
        self.square_label.setGeometry(QtCore.QRect(70, 20, 451, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.square_label.setFont(font)
        self.square_label.setObjectName("square_label")
        self.square_label_2 = QtWidgets.QLabel(self.square_tab)
        self.square_label_2.setGeometry(QtCore.QRect(210, 80, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.square_label_2.setFont(font)
        self.square_label_2.setObjectName("square_label_2")
        self.square_input = QtWidgets.QLineEdit(self.square_tab)
        self.square_input.setGeometry(QtCore.QRect(170, 110, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.square_input.setFont(font)
        self.square_input.setObjectName("square_input")
        self.square_computeButton = QtWidgets.QPushButton(self.square_tab)
        self.square_computeButton.setGeometry(QtCore.QRect(230, 160, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.square_computeButton.setFont(font)
        self.square_computeButton.setObjectName("square_computeButton")
        self.square_answer_label = QtWidgets.QLabel(self.square_tab)
        self.square_answer_label.setGeometry(QtCore.QRect(220, 240, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.square_answer_label.setFont(font)
        self.square_answer_label.setObjectName("square_answer_label")
        self.square_answer_display = QtWidgets.QLabel(self.square_tab)
        self.square_answer_display.setGeometry(QtCore.QRect(120, 280, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.square_answer_display.setFont(font)
        self.square_answer_display.setText("")
        self.square_answer_display.setAlignment(QtCore.Qt.AlignCenter)
        self.square_answer_display.setObjectName("square_answer_display")
        self.tab_selector.addTab(self.square_tab, "")
        self.triangle_tab = QtWidgets.QWidget()
        self.triangle_tab.setObjectName("triangle_tab")
        self.triangle_label = QtWidgets.QLabel(self.triangle_tab)
        self.triangle_label.setGeometry(QtCore.QRect(70, 20, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.triangle_label.setFont(font)
        self.triangle_label.setObjectName("triangle_label")
        self.triangle_label_2 = QtWidgets.QLabel(self.triangle_tab)
        self.triangle_label_2.setGeometry(QtCore.QRect(210, 80, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.triangle_label_2.setFont(font)
        self.triangle_label_2.setObjectName("triangle_label_2")
        self.triangle_base_input = QtWidgets.QLineEdit(self.triangle_tab)
        self.triangle_base_input.setGeometry(QtCore.QRect(170, 110, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.triangle_base_input.setFont(font)
        self.triangle_base_input.setObjectName("triangle_base_input")
        self.triangle_label_3 = QtWidgets.QLabel(self.triangle_tab)
        self.triangle_label_3.setGeometry(QtCore.QRect(200, 150, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.triangle_label_3.setFont(font)
        self.triangle_label_3.setObjectName("triangle_label_3")
        self.triangle_height_input = QtWidgets.QLineEdit(self.triangle_tab)
        self.triangle_height_input.setGeometry(QtCore.QRect(170, 190, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.triangle_height_input.setFont(font)
        self.triangle_height_input.setObjectName("triangle_height_input")
        self.triangle_computeButton = QtWidgets.QPushButton(self.triangle_tab)
        self.triangle_computeButton.setGeometry(QtCore.QRect(230, 240, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.triangle_computeButton.setFont(font)
        self.triangle_computeButton.setObjectName("triangle_computeButton")
        self.triangle_answer_label = QtWidgets.QLabel(self.triangle_tab)
        self.triangle_answer_label.setGeometry(QtCore.QRect(220, 310, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.triangle_answer_label.setFont(font)
        self.triangle_answer_label.setObjectName("triangle_answer_label")
        self.triangle_answer_display = QtWidgets.QLabel(self.triangle_tab)
        self.triangle_answer_display.setGeometry(QtCore.QRect(120, 350, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.triangle_answer_display.setFont(font)
        self.triangle_answer_display.setText("")
        self.triangle_answer_display.setAlignment(QtCore.Qt.AlignCenter)
        self.triangle_answer_display.setObjectName("triangle_answer_display")
        self.tab_selector.addTab(self.triangle_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_selector.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Math Functions"))
        self.power_label.setText(_translate("MainWindow", "Calculates Exponents"))
        self.power_label_2.setText(_translate("MainWindow", "Enter the Base:"))
        self.power_label_3.setText(_translate("MainWindow", "Enter the Power:"))
        self.power_computeButton.setText(_translate("MainWindow", "Compute"))
        self.power_answer_label.setText(_translate("MainWindow", "The answer is..."))
        self.tab_selector.setTabText(self.tab_selector.indexOf(self.widget), _translate("MainWindow", "Power"))
        self.circle_label1.setText(_translate("MainWindow", "Calculates Area of a Circle"))
        self.circle_label2.setText(_translate("MainWindow", "Enter Radius:"))
        self.circle_computeButton.setText(_translate("MainWindow", "Compute"))
        self.circle_answer_label.setText(_translate("MainWindow", "The answer is..."))
        self.tab_selector.setTabText(self.tab_selector.indexOf(self.circle_tab), _translate("MainWindow", "Circle"))
        self.rectangle_label.setText(_translate("MainWindow", "Calculates Area of a Rectangle"))
        self.rectangle_label_2.setText(_translate("MainWindow", "Enter Length:"))
        self.rectangle_computeButton.setText(_translate("MainWindow", "Compute"))
        self.rectangle_answer_label.setText(_translate("MainWindow", "The answer is..."))
        self.rectangle_label_3.setText(_translate("MainWindow", "Enter Width:"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/calcbackground/blue background bigger.jpg\"/></p></body></html>"))
        self.tab_selector.setTabText(self.tab_selector.indexOf(self.rectangle_tab), _translate("MainWindow", "Rectangle"))
        self.square_label.setText(_translate("MainWindow", "Calculates Area of a Square"))
        self.square_label_2.setText(_translate("MainWindow", "Enter Side Length:"))
        self.square_computeButton.setText(_translate("MainWindow", "Compute"))
        self.square_answer_label.setText(_translate("MainWindow", "The answer is..."))
        self.tab_selector.setTabText(self.tab_selector.indexOf(self.square_tab), _translate("MainWindow", "Square"))
        self.triangle_label.setText(_translate("MainWindow", "Calculates Area of a Triangle"))
        self.triangle_label_2.setText(_translate("MainWindow", "Enter Base Length:"))
        self.triangle_label_3.setText(_translate("MainWindow", "Enter Height Length:"))
        self.triangle_computeButton.setText(_translate("MainWindow", "Compute"))
        self.triangle_answer_label.setText(_translate("MainWindow", "The answer is..."))
        self.tab_selector.setTabText(self.tab_selector.indexOf(self.triangle_tab), _translate("MainWindow", "Triangle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())