# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TRAINindicator.ui'
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

class Ui_MainWindow_TRAINindicator(object):
    def setupUi(self, MainWindow_TRAINindicator):
        MainWindow_TRAINindicator.setObjectName(_fromUtf8("MainWindow_TRAINindicator"))
        MainWindow_TRAINindicator.resize(221, 332)
        self.centralwidget = QtGui.QWidget(MainWindow_TRAINindicator)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 200, 201, 121))
        self.groupBox_5.setTitle(_fromUtf8(""))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.checkBox_SUPRESSvisualization = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox_SUPRESSvisualization.setGeometry(QtCore.QRect(40, 50, 131, 21))
        self.checkBox_SUPRESSvisualization.setObjectName(_fromUtf8("checkBox_SUPRESSvisualization"))
        self.pushButton_EDIT = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_EDIT.setGeometry(QtCore.QRect(10, 80, 181, 31))
        self.pushButton_EDIT.setObjectName(_fromUtf8("pushButton_EDIT"))
        self.pushButton_EXTRACT = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_EXTRACT.setGeometry(QtCore.QRect(10, 10, 181, 31))
        self.pushButton_EXTRACT.setObjectName(_fromUtf8("pushButton_EXTRACT"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 201, 181))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 100, 181, 71))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_SELECT = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_SELECT.setGeometry(QtCore.QRect(10, 30, 161, 31))
        self.pushButton_SELECT.setObjectName(_fromUtf8("pushButton_SELECT"))
        self.radioButton_RGB = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_RGB.setGeometry(QtCore.QRect(10, 10, 51, 17))
        self.radioButton_RGB.setObjectName(_fromUtf8("radioButton_RGB"))
        self.radioButton_HSV = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_HSV.setGeometry(QtCore.QRect(70, 10, 41, 17))
        self.radioButton_HSV.setObjectName(_fromUtf8("radioButton_HSV"))
        self.radioButton_NDVI = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_NDVI.setGeometry(QtCore.QRect(120, 10, 51, 17))
        self.radioButton_NDVI.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_NDVI.setObjectName(_fromUtf8("radioButton_NDVI"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 181, 71))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.checkBox_LAB = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_LAB.setGeometry(QtCore.QRect(40, 40, 101, 17))
        self.checkBox_LAB.setObjectName(_fromUtf8("checkBox_LAB"))
        self.radio_PHVALUE = QtGui.QRadioButton(self.groupBox_3)
        self.radio_PHVALUE.setGeometry(QtCore.QRect(110, 10, 61, 17))
        self.radio_PHVALUE.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radio_PHVALUE.setObjectName(_fromUtf8("radio_PHVALUE"))
        self.radio_MOISTURE = QtGui.QRadioButton(self.groupBox_3)
        self.radio_MOISTURE.setGeometry(QtCore.QRect(10, 10, 72, 17))
        self.radio_MOISTURE.setObjectName(_fromUtf8("radio_MOISTURE"))
        MainWindow_TRAINindicator.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_TRAINindicator)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_TRAINindicator)

    def retranslateUi(self, MainWindow_TRAINindicator):
        MainWindow_TRAINindicator.setWindowTitle(_translate("MainWindow_TRAINindicator", "Train indicator for pH and Moisture", None))
        self.checkBox_SUPRESSvisualization.setText(_translate("MainWindow_TRAINindicator", "Suppress Visualization", None))
        self.pushButton_EDIT.setText(_translate("MainWindow_TRAINindicator", "EDIT VALUES", None))
        self.pushButton_EXTRACT.setText(_translate("MainWindow_TRAINindicator", "EXTRACT FEATURES", None))
        self.groupBox.setTitle(_translate("MainWindow_TRAINindicator", "Select Features", None))
        self.pushButton_SELECT.setText(_translate("MainWindow_TRAINindicator", "SELECT IMAGES", None))
        self.radioButton_RGB.setText(_translate("MainWindow_TRAINindicator", "RGB", None))
        self.radioButton_HSV.setText(_translate("MainWindow_TRAINindicator", "HSV", None))
        self.radioButton_NDVI.setText(_translate("MainWindow_TRAINindicator", "NDVI", None))
        self.checkBox_LAB.setText(_translate("MainWindow_TRAINindicator", "LAB TRANFORM", None))
        self.radio_PHVALUE.setText(_translate("MainWindow_TRAINindicator", "pH Value", None))
        self.radio_MOISTURE.setText(_translate("MainWindow_TRAINindicator", "Moisture", None))

