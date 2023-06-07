# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

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
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName("Extra data")
        self.textBrowser.setGeometry(QtCore.QRect(20, 120, 120, 80))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Start/Stop"))

from mplwidget import MplWidget
