# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PREDICTORgypsum.ui'
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

class Ui_MainWindow_Gypsum(object):
    def setupUi(self, MainWindow_Gypsum):
        MainWindow_Gypsum.setObjectName(_fromUtf8("MainWindow_Gypsum"))
        MainWindow_Gypsum.resize(479, 252)
        self.centralwidget = QtGui.QWidget(MainWindow_Gypsum)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 461, 231))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit_pHValue = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_pHValue.setGeometry(QtCore.QRect(10, 100, 221, 41))
        self.lineEdit_pHValue.setObjectName(_fromUtf8("lineEdit_pHValue"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(100, 70, 46, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_ESTIMATEvalue = QtGui.QPushButton(self.groupBox)
        self.pushButton_ESTIMATEvalue.setGeometry(QtCore.QRect(10, 150, 221, 41))
        self.pushButton_ESTIMATEvalue.setObjectName(_fromUtf8("pushButton_ESTIMATEvalue"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(300, 70, 111, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_RESET = QtGui.QPushButton(self.groupBox)
        self.pushButton_RESET.setGeometry(QtCore.QRect(240, 150, 211, 41))
        self.pushButton_RESET.setObjectName(_fromUtf8("pushButton_RESET"))
        self.textBrowser_GYPSUMestimate = QtGui.QTextBrowser(self.groupBox)
        self.textBrowser_GYPSUMestimate.setGeometry(QtCore.QRect(240, 100, 211, 41))
        self.textBrowser_GYPSUMestimate.setObjectName(_fromUtf8("textBrowser_GYPSUMestimate"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 441, 51))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.checkBox_SUPRESS = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_SUPRESS.setGeometry(QtCore.QRect(40, 0, 371, 31))
        self.checkBox_SUPRESS.setObjectName(_fromUtf8("checkBox_SUPRESS"))
        self.radioButton_MEDIUM = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_MEDIUM.setGeometry(QtCore.QRect(190, 30, 61, 17))
        self.radioButton_MEDIUM.setObjectName(_fromUtf8("radioButton_MEDIUM"))
        self.radioButton_HEAVY = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_HEAVY.setGeometry(QtCore.QRect(40, 30, 61, 17))
        self.radioButton_HEAVY.setObjectName(_fromUtf8("radioButton_HEAVY"))
        self.radioButton_LIGHT = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_LIGHT.setGeometry(QtCore.QRect(350, 30, 51, 17))
        self.radioButton_LIGHT.setObjectName(_fromUtf8("radioButton_LIGHT"))
        self.checkBox_Polyfit = QtGui.QCheckBox(self.groupBox)
        self.checkBox_Polyfit.setGeometry(QtCore.QRect(150, 200, 171, 17))
        self.checkBox_Polyfit.setObjectName(_fromUtf8("checkBox_Polyfit"))
        MainWindow_Gypsum.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_Gypsum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Gypsum)

    def retranslateUi(self, MainWindow_Gypsum):
        MainWindow_Gypsum.setWindowTitle(_translate("MainWindow_Gypsum", "GYPSUM", None))
        self.label.setText(_translate("MainWindow_Gypsum", "pH Value", None))
        self.pushButton_ESTIMATEvalue.setText(_translate("MainWindow_Gypsum", "ESTIMATE", None))
        self.label_2.setText(_translate("MainWindow_Gypsum", "Gypsum Requirement", None))
        self.pushButton_RESET.setText(_translate("MainWindow_Gypsum", "RESET", None))
        self.checkBox_SUPRESS.setText(_translate("MainWindow_Gypsum", "Supress the graph showing the regression equation and training dataset", None))
        self.radioButton_MEDIUM.setText(_translate("MainWindow_Gypsum", "Medium", None))
        self.radioButton_HEAVY.setText(_translate("MainWindow_Gypsum", "Heavy", None))
        self.radioButton_LIGHT.setText(_translate("MainWindow_Gypsum", "Light", None))
        self.checkBox_Polyfit.setText(_translate("MainWindow_Gypsum", "Use Poly fit instead of ML model", None))

