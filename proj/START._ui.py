# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'START.ui'
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

class Ui_MainWindow_START(object):
    def setupUi(self, MainWindow_START):
        MainWindow_START.setObjectName(_fromUtf8("MainWindow_START"))
        MainWindow_START.resize(291, 458)
        self.centralwidget = QtGui.QWidget(MainWindow_START)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 131, 321))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton_TRAINleaf = QtGui.QPushButton(self.groupBox)
        self.pushButton_TRAINleaf.setGeometry(QtCore.QRect(10, 140, 111, 51))
        self.pushButton_TRAINleaf.setObjectName(_fromUtf8("pushButton_TRAINleaf"))
        self.pushButton_TRAINphNmoisture = QtGui.QPushButton(self.groupBox)
        self.pushButton_TRAINphNmoisture.setGeometry(QtCore.QRect(10, 20, 111, 51))
        self.pushButton_TRAINphNmoisture.setObjectName(_fromUtf8("pushButton_TRAINphNmoisture"))
        self.pushButton_TRAINgypsum = QtGui.QPushButton(self.groupBox)
        self.pushButton_TRAINgypsum.setGeometry(QtCore.QRect(10, 200, 111, 51))
        self.pushButton_TRAINgypsum.setObjectName(_fromUtf8("pushButton_TRAINgypsum"))
        self.pushButton_TRAINanalogMeter = QtGui.QPushButton(self.groupBox)
        self.pushButton_TRAINanalogMeter.setGeometry(QtCore.QRect(10, 80, 111, 51))
        self.pushButton_TRAINanalogMeter.setObjectName(_fromUtf8("pushButton_TRAINanalogMeter"))
        self.pushButton_TRAINurea = QtGui.QPushButton(self.groupBox)
        self.pushButton_TRAINurea.setGeometry(QtCore.QRect(10, 260, 111, 51))
        self.pushButton_TRAINurea.setObjectName(_fromUtf8("pushButton_TRAINurea"))
        self.pushButton_TRAINleaf.raise_()
        self.pushButton_TRAINphNmoisture.raise_()
        self.pushButton_TRAINgypsum.raise_()
        self.pushButton_TRAINanalogMeter.raise_()
        self.pushButton_TRAINurea.raise_()
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(150, 10, 131, 321))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_GYPSUM = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_GYPSUM.setGeometry(QtCore.QRect(10, 200, 111, 51))
        self.pushButton_GYPSUM.setObjectName(_fromUtf8("pushButton_GYPSUM"))
        self.pushButton_LEAFAREAMETER = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_LEAFAREAMETER.setGeometry(QtCore.QRect(10, 140, 111, 51))
        self.pushButton_LEAFAREAMETER.setObjectName(_fromUtf8("pushButton_LEAFAREAMETER"))
        self.pushButton_ANALOGmeter = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_ANALOGmeter.setGeometry(QtCore.QRect(10, 80, 111, 51))
        self.pushButton_ANALOGmeter.setObjectName(_fromUtf8("pushButton_ANALOGmeter"))
        self.pushButton_PH_Moisture = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_PH_Moisture.setGeometry(QtCore.QRect(10, 20, 111, 51))
        self.pushButton_PH_Moisture.setObjectName(_fromUtf8("pushButton_PH_Moisture"))
        self.pushButton_LEAFCOLOURurea = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_LEAFCOLOURurea.setGeometry(QtCore.QRect(10, 260, 111, 51))
        self.pushButton_LEAFCOLOURurea.setObjectName(_fromUtf8("pushButton_LEAFCOLOURurea"))
        self.pushButton_ACQUIREimages = QtGui.QPushButton(self.centralwidget)
        self.pushButton_ACQUIREimages.setGeometry(QtCore.QRect(10, 340, 271, 51))
        self.pushButton_ACQUIREimages.setObjectName(_fromUtf8("pushButton_ACQUIREimages"))
        self.pushButton_LOG = QtGui.QPushButton(self.centralwidget)
        self.pushButton_LOG.setGeometry(QtCore.QRect(10, 400, 131, 51))
        self.pushButton_LOG.setObjectName(_fromUtf8("pushButton_LOG"))
        self.pushButton_HELP = QtGui.QPushButton(self.centralwidget)
        self.pushButton_HELP.setGeometry(QtCore.QRect(150, 400, 131, 51))
        self.pushButton_HELP.setObjectName(_fromUtf8("pushButton_HELP"))
        MainWindow_START.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_START)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_START)

    def retranslateUi(self, MainWindow_START):
        MainWindow_START.setWindowTitle(_translate("MainWindow_START", "NETRA", None))
        self.groupBox.setTitle(_translate("MainWindow_START", "Train System", None))
        self.pushButton_TRAINleaf.setText(_translate("MainWindow_START", "Leaf Area Meter", None))
        self.pushButton_TRAINphNmoisture.setText(_translate("MainWindow_START", "pH / Moisture", None))
        self.pushButton_TRAINgypsum.setText(_translate("MainWindow_START", "Gypsum", None))
        self.pushButton_TRAINanalogMeter.setText(_translate("MainWindow_START", "Analog Meter", None))
        self.pushButton_TRAINurea.setText(_translate("MainWindow_START", "Leaf Colour/ Urea", None))
        self.groupBox_2.setTitle(_translate("MainWindow_START", "Applications", None))
        self.pushButton_GYPSUM.setText(_translate("MainWindow_START", "Gypsum ", None))
        self.pushButton_LEAFAREAMETER.setText(_translate("MainWindow_START", "Leaf Area Meter", None))
        self.pushButton_ANALOGmeter.setText(_translate("MainWindow_START", "Analog Meter", None))
        self.pushButton_PH_Moisture.setText(_translate("MainWindow_START", "pH / Moisture", None))
        self.pushButton_LEAFCOLOURurea.setText(_translate("MainWindow_START", "Leaf Colour / Urea", None))
        self.pushButton_ACQUIREimages.setText(_translate("MainWindow_START", "Acquire Images", None))
        self.pushButton_LOG.setText(_translate("MainWindow_START", "Log", None))
        self.pushButton_HELP.setText(_translate("MainWindow_START", "Help", None))

