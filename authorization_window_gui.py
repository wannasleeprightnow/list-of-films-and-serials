# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)
        Form.setMinimumSize(QtCore.QSize(500, 300))
        Form.setMaximumSize(QtCore.QSize(500, 300))
        Form.setWindowTitle("Your Trip")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(63, 46, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(33, 126, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(182, 50, 250, 20))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(182, 130, 250, 20))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(62, 190, 374, 30))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(62, 240, 374, 30))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "Login:"))
        self.label_2.setText(_translate("Form", "Password:"))
        self.pushButton.setText(_translate("Form", "Sign in"))
        self.pushButton_2.setText(_translate("Form", "Sign up"))
    


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Ui_Form()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
