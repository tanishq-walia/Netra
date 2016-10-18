# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PREDICTORleaf.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow_PREDICRTORleaf(object):
    def setupUi(self, MainWindow_PREDICRTORleaf):
        MainWindow_PREDICRTORleaf.setObjectName(_fromUtf8("MainWindow_PREDICRTORleaf"))
        MainWindow_PREDICRTORleaf.resize(730, 459)
        self.centralwidget = QtGui.QWidget(MainWindow_PREDICRTORleaf)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 491, 381))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_FEEDLABEL = QtGui.QLabel(self.groupBox)
        self.label_FEEDLABEL.setGeometry(QtCore.QRect(10, 20, 471, 351))
        self.label_FEEDLABEL.setObjectName(_fromUtf8("label_FEEDLABEL"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(510, 10, 211, 441))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_RESET = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_RESET.setGeometry(QtCore.QRect(110, 390, 91, 41))
        self.pushButton_RESET.setObjectName(_fromUtf8("pushButton_RESET"))
        self.textBrowser_OUTPUT = QtGui.QTextBrowser(self.groupBox_2)
        self.textBrowser_OUTPUT.setGeometry(QtCore.QRect(10, 340, 191, 41))
        self.textBrowser_OUTPUT.setObjectName(_fromUtf8("textBrowser_OUTPUT"))
        self.pushButton_CALCULATEfromPath = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_CALCULATEfromPath.setGeometry(QtCore.QRect(10, 240, 191, 41))
        self.pushButton_CALCULATEfromPath.setObjectName(_fromUtf8("pushButton_CALCULATEfromPath"))
        self.pushButton_CALCULATEfromStream = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_CALCULATEfromStream.setGeometry(QtCore.QRect(10, 290, 191, 41))
        self.pushButton_CALCULATEfromStream.setObjectName(_fromUtf8("pushButton_CALCULATEfromStream"))
        self.lineEdit_RESIZEfactor = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_RESIZEfactor.setGeometry(QtCore.QRect(110, 150, 91, 31))
        self.lineEdit_RESIZEfactor.setObjectName(_fromUtf8("lineEdit_RESIZEfactor"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 150, 81, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_SAVE = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_SAVE.setGeometry(QtCore.QRect(10, 390, 91, 41))
        self.pushButton_SAVE.setObjectName(_fromUtf8("pushButton_SAVE"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 91, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(120, 80, 81, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_CALIBRATIONunit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_CALIBRATIONunit.setGeometry(QtCore.QRect(110, 110, 91, 31))
        self.lineEdit_CALIBRATIONunit.setObjectName(_fromUtf8("lineEdit_CALIBRATIONunit"))
        self.lineEdit_CALIBRATIONvalue = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_CALIBRATIONvalue.setGeometry(QtCore.QRect(10, 110, 91, 31))
        self.lineEdit_CALIBRATIONvalue.setObjectName(_fromUtf8("lineEdit_CALIBRATIONvalue"))
        self.pushButton_SET = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_SET.setGeometry(QtCore.QRect(10, 190, 191, 41))
        self.pushButton_SET.setObjectName(_fromUtf8("pushButton_SET"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(110, 20, 91, 61))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.radio_NGB = QtGui.QRadioButton(self.groupBox_4)
        self.radio_NGB.setGeometry(QtCore.QRect(10, 30, 71, 20))
        self.radio_NGB.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radio_NGB.setObjectName(_fromUtf8("radio_NGB"))
        self.radio_RGB = QtGui.QRadioButton(self.groupBox_4)
        self.radio_RGB.setGeometry(QtCore.QRect(10, 10, 72, 17))
        self.radio_RGB.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radio_RGB.setObjectName(_fromUtf8("radio_RGB"))
        self.pushButton_CAPTURE = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_CAPTURE.setGeometry(QtCore.QRect(10, 20, 91, 61))
        self.pushButton_CAPTURE.setObjectName(_fromUtf8("pushButton_CAPTURE"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 400, 491, 51))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.lineEdit_FILEpath = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_FILEpath.setGeometry(QtCore.QRect(120, 10, 361, 31))
        self.lineEdit_FILEpath.setObjectName(_fromUtf8("lineEdit_FILEpath"))
        self.pushButton_SELECT = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_SELECT.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.pushButton_SELECT.setObjectName(_fromUtf8("pushButton_SELECT"))
        MainWindow_PREDICRTORleaf.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_PREDICRTORleaf)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_PREDICRTORleaf)

    def retranslateUi(self, MainWindow_PREDICRTORleaf):
        MainWindow_PREDICRTORleaf.setWindowTitle(_translate("MainWindow_PREDICRTORleaf", "PREDICTOR", None))
        self.groupBox.setTitle(_translate("MainWindow_PREDICRTORleaf", "Display", None))
        self.label_FEEDLABEL.setText(_translate("MainWindow_PREDICRTORleaf", "Feed Label", None))
        self.groupBox_2.setTitle(_translate("MainWindow_PREDICRTORleaf", "Controls", None))
        self.pushButton_RESET.setText(_translate("MainWindow_PREDICRTORleaf", "RESET", None))
        self.pushButton_CALCULATEfromPath.setText(_translate("MainWindow_PREDICRTORleaf", "CALCULATE FROM PATH", None))
        self.pushButton_CALCULATEfromStream.setText(_translate("MainWindow_PREDICRTORleaf", "CALCULATE FROM STREAM", None))
        self.label.setText(_translate("MainWindow_PREDICRTORleaf", "Resize factor :", None))
        self.pushButton_SAVE.setText(_translate("MainWindow_PREDICRTORleaf", "SAVE", None))
        self.label_3.setText(_translate("MainWindow_PREDICRTORleaf", "Referance Length", None))
        self.label_2.setText(_translate("MainWindow_PREDICRTORleaf", "Referance Unit", None))
        self.pushButton_SET.setText(_translate("MainWindow_PREDICRTORleaf", "SET VALUES", None))
        self.radio_NGB.setText(_translate("MainWindow_PREDICRTORleaf", "NGB Mode", None))
        self.radio_RGB.setText(_translate("MainWindow_PREDICRTORleaf", "RGB Mode", None))
        self.pushButton_CAPTURE.setText(_translate("MainWindow_PREDICRTORleaf", "CAPTURE", None))
        self.pushButton_SELECT.setText(_translate("MainWindow_PREDICRTORleaf", "SELECT FILE", None))

