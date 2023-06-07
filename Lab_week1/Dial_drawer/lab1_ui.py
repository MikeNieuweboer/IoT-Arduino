# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from mplwidget import MplWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(543, 364)
        self.MplWidget = MplWidget(Form)
        self.MplWidget.setGeometry(QtCore.QRect(150, 10, 381, 341))
        self.MplWidget.setObjectName("MplWidget")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 70, 80, 23))
        self.pushButton.setObjectName("pushButton")
        self.dial = QtWidgets.QDial(Form)
        self.dial.setGeometry(QtCore.QRect(30, 120, 101, 111))
        self.dial.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dial.setMaximum(999)
        self.dial.setProperty("value", 0)
        self.dial.setOrientation(QtCore.Qt.Vertical)
        self.dial.setWrapping(True)
        self.dial.setObjectName("dial")
        self.dial.setProperty("value", 750)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 20, 80, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 260, 120, 80))
        self.groupBox.setObjectName("groupBox")
        self.spinBox_Y = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_Y.setGeometry(QtCore.QRect(10, 50, 47, 24))
        self.spinBox_Y.setObjectName("spinBox_X")
        self.spinBox_Y.setProperty("value", 50)
        self.spinBox_X = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_X.setGeometry(QtCore.QRect(10, 20, 47, 24))
        self.spinBox_X.setObjectName("spinBox_Y")
        self.spinBox_X.setProperty("value", 50)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Start/Stop"))
        self.pushButton_2.setText(_translate("Form", "Reset"))
        self.groupBox.setTitle(_translate("Form", "X and Y Bounds"))
