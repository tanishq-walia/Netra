# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PREDICTOR.ui'
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

class Ui_MainWindow_PREDICTOR(object):
    def setupUi(self, MainWindow_PREDICTOR):
        MainWindow_PREDICTOR.setObjectName(_fromUtf8("MainWindow_PREDICTOR"))
        MainWindow_PREDICTOR.resize(727, 463)
        self.centralwidget = QtGui.QWidget(MainWindow_PREDICTOR)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(510, 10, 211, 441))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.textBrowser_OUTPUT = QtGui.QTextBrowser(self.groupBox_2)
        self.textBrowser_OUTPUT.setGeometry(QtCore.QRect(10, 360, 191, 31))
        self.textBrowser_OUTPUT.setObjectName(_fromUtf8("textBrowser_OUTPUT"))
        self.pushButton_CALCULATEfromStream = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_CALCULATEfromStream.setGeometry(QtCore.QRect(10, 230, 191, 41))
        self.pushButton_CALCULATEfromStream.setObjectName(_fromUtf8("pushButton_CALCULATEfromStream"))
        self.pushButton_SAVE = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_SAVE.setGeometry(QtCore.QRect(10, 400, 91, 31))
        self.pushButton_SAVE.setObjectName(_fromUtf8("pushButton_SAVE"))
        self.pushButton_CAPTURE = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_CAPTURE.setGeometry(QtCore.QRect(10, 20, 91, 61))
        self.pushButton_CAPTURE.setObjectName(_fromUtf8("pushButton_CAPTURE"))
        self.pushButton_RESET = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_RESET.setGeometry(QtCore.QRect(110, 400, 91, 31))
        self.pushButton_RESET.setObjectName(_fromUtf8("pushButton_RESET"))
        self.pushButton_CALCULATEfromPath = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_CALCULATEfromPath.setGeometry(QtCore.QRect(10, 280, 191, 41))
        self.pushButton_CALCULATEfromPath.setObjectName(_fromUtf8("pushButton_CALCULATEfromPath"))
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
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 90, 191, 41))
        self.groupBox_5.setTitle(_fromUtf8(""))
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.radioButton_RGB = QtGui.QRadioButton(self.groupBox_5)
        self.radioButton_RGB.setGeometry(QtCore.QRect(10, 10, 41, 17))
        self.radioButton_RGB.setObjectName(_fromUtf8("radioButton_RGB"))
        self.radioButton_HSV = QtGui.QRadioButton(self.groupBox_5)
        self.radioButton_HSV.setGeometry(QtCore.QRect(80, 10, 41, 17))
        self.radioButton_HSV.setObjectName(_fromUtf8("radioButton_HSV"))
        self.radioButton_NDVI = QtGui.QRadioButton(self.groupBox_5)
        self.radioButton_NDVI.setGeometry(QtCore.QRect(130, 10, 51, 17))
        self.radioButton_NDVI.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_NDVI.setObjectName(_fromUtf8("radioButton_NDVI"))
        self.pushButton_SET = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_SET.setGeometry(QtCore.QRect(110, 190, 91, 31))
        self.pushButton_SET.setObjectName(_fromUtf8("pushButton_SET"))
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 140, 191, 41))
        self.groupBox_6.setTitle(_fromUtf8(""))
        self.groupBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.radio_MOISTURE = QtGui.QRadioButton(self.groupBox_6)
        self.radio_MOISTURE.setGeometry(QtCore.QRect(10, 10, 72, 17))
        self.radio_MOISTURE.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radio_MOISTURE.setObjectName(_fromUtf8("radio_MOISTURE"))
        self.radio_PHVALUE = QtGui.QRadioButton(self.groupBox_6)
        self.radio_PHVALUE.setGeometry(QtCore.QRect(110, 10, 72, 17))
        self.radio_PHVALUE.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radio_PHVALUE.setObjectName(_fromUtf8("radio_PHVALUE"))
        self.checkBox_LAB = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_LAB.setGeometry(QtCore.QRect(20, 190, 81, 21))
        self.checkBox_LAB.setObjectName(_fromUtf8("checkBox_LAB"))
        self.horizontalSlider_RELATIVESCALE = QtGui.QSlider(self.groupBox_2)
        self.horizontalSlider_RELATIVESCALE.setGeometry(QtCore.QRect(10, 330, 191, 22))
        self.horizontalSlider_RELATIVESCALE.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_RELATIVESCALE.setObjectName(_fromUtf8("horizontalSlider_RELATIVESCALE"))
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
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 491, 381))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_FEEDLABEL = QtGui.QLabel(self.groupBox)
        self.label_FEEDLABEL.setGeometry(QtCore.QRect(10, 20, 471, 351))
        self.label_FEEDLABEL.setObjectName(_fromUtf8("label_FEEDLABEL"))
        MainWindow_PREDICTOR.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_PREDICTOR)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_PREDICTOR)

    def retranslateUi(self, MainWindow_PREDICTOR):
        MainWindow_PREDICTOR.setWindowTitle(_translate("MainWindow_PREDICTOR", "PREDICTOR", None))
        self.groupBox_2.setTitle(_translate("MainWindow_PREDICTOR", "Controls", None))
        self.pushButton_CALCULATEfromStream.setText(_translate("MainWindow_PREDICTOR", "CALCULATE FROM STREAM", None))
        self.pushButton_SAVE.setText(_translate("MainWindow_PREDICTOR", "SAVE", None))
        self.pushButton_CAPTURE.setText(_translate("MainWindow_PREDICTOR", "CAPTURE", None))
        self.pushButton_RESET.setText(_translate("MainWindow_PREDICTOR", "RESET", None))
        self.pushButton_CALCULATEfromPath.setText(_translate("MainWindow_PREDICTOR", "CALCULATE FROM PATH", None))
        self.radio_NGB.setText(_translate("MainWindow_PREDICTOR", "NGB Mode", None))
        self.radio_RGB.setText(_translate("MainWindow_PREDICTOR", "RGB Mode", None))
        self.radioButton_RGB.setText(_translate("MainWindow_PREDICTOR", "RGB", None))
        self.radioButton_HSV.setText(_translate("MainWindow_PREDICTOR", "HSV", None))
        self.radioButton_NDVI.setText(_translate("MainWindow_PREDICTOR", "NDVI", None))
        self.pushButton_SET.setText(_translate("MainWindow_PREDICTOR", "SET VALUES", None))
        self.radio_MOISTURE.setText(_translate("MainWindow_PREDICTOR", "Moisture", None))
        self.radio_PHVALUE.setText(_translate("MainWindow_PREDICTOR", "pH Value", None))
        self.checkBox_LAB.setText(_translate("MainWindow_PREDICTOR", "LAB SPACE", None))
        self.pushButton_SELECT.setText(_translate("MainWindow_PREDICTOR", "SELECT FILE", None))
        self.groupBox.setTitle(_translate("MainWindow_PREDICTOR", "Display", None))
        self.label_FEEDLABEL.setText(_translate("MainWindow_PREDICTOR", "Feed Label", None))

