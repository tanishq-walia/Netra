# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TRAINgypsum.ui'
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

class Ui_MainWindow_TRAINgypsum(object):
    def setupUi(self, MainWindow_TRAINgypsum):
        MainWindow_TRAINgypsum.setObjectName(_fromUtf8("MainWindow_TRAINgypsum"))
        MainWindow_TRAINgypsum.resize(231, 300)
        self.centralwidget = QtGui.QWidget(MainWindow_TRAINgypsum)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 211, 231))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit_ALPHA = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_ALPHA.setGeometry(QtCore.QRect(10, 70, 91, 31))
        self.lineEdit_ALPHA.setObjectName(_fromUtf8("lineEdit_ALPHA"))
        self.pushButton_EDIT = QtGui.QPushButton(self.groupBox)
        self.pushButton_EDIT.setGeometry(QtCore.QRect(10, 10, 191, 31))
        self.pushButton_EDIT.setObjectName(_fromUtf8("pushButton_EDIT"))
        self.lineEdit_ITERATION = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_ITERATION.setGeometry(QtCore.QRect(110, 70, 91, 31))
        self.lineEdit_ITERATION.setObjectName(_fromUtf8("lineEdit_ITERATION"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 50, 31, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(130, 50, 51, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.checkBox_SUPRESSvisualization = QtGui.QCheckBox(self.groupBox)
        self.checkBox_SUPRESSvisualization.setGeometry(QtCore.QRect(10, 110, 131, 31))
        self.checkBox_SUPRESSvisualization.setObjectName(_fromUtf8("checkBox_SUPRESSvisualization"))
        self.checkBox_SUPRESSregression = QtGui.QCheckBox(self.groupBox)
        self.checkBox_SUPRESSregression.setGeometry(QtCore.QRect(10, 150, 371, 21))
        self.checkBox_SUPRESSregression.setObjectName(_fromUtf8("checkBox_SUPRESSregression"))
        self.pushButton_TRAIN = QtGui.QPushButton(self.groupBox)
        self.pushButton_TRAIN.setGeometry(QtCore.QRect(10, 190, 191, 31))
        self.pushButton_TRAIN.setObjectName(_fromUtf8("pushButton_TRAIN"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 211, 41))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.radioButton_MEDIUM = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_MEDIUM.setGeometry(QtCore.QRect(80, 10, 61, 17))
        self.radioButton_MEDIUM.setObjectName(_fromUtf8("radioButton_MEDIUM"))
        self.radioButton_HEAVY = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_HEAVY.setGeometry(QtCore.QRect(10, 10, 61, 17))
        self.radioButton_HEAVY.setObjectName(_fromUtf8("radioButton_HEAVY"))
        self.radioButton_LIGHT = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_LIGHT.setGeometry(QtCore.QRect(160, 10, 41, 17))
        self.radioButton_LIGHT.setObjectName(_fromUtf8("radioButton_LIGHT"))
        MainWindow_TRAINgypsum.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_TRAINgypsum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_TRAINgypsum)

    def retranslateUi(self, MainWindow_TRAINgypsum):
        MainWindow_TRAINgypsum.setWindowTitle(_translate("MainWindow_TRAINgypsum", "Train Gypsum Predictor", None))
        self.pushButton_EDIT.setText(_translate("MainWindow_TRAINgypsum", "EDIT VALUES", None))
        self.label.setText(_translate("MainWindow_TRAINgypsum", "Alpha", None))
        self.label_2.setText(_translate("MainWindow_TRAINgypsum", "Iterations", None))
        self.checkBox_SUPRESSvisualization.setText(_translate("MainWindow_TRAINgypsum", "Suppress Visualization", None))
        self.checkBox_SUPRESSregression.setText(_translate("MainWindow_TRAINgypsum", "Supress the regression curve", None))
        self.pushButton_TRAIN.setText(_translate("MainWindow_TRAINgypsum", "TRAIN NETWORK", None))
        self.radioButton_MEDIUM.setText(_translate("MainWindow_TRAINgypsum", "Medium", None))
        self.radioButton_HEAVY.setText(_translate("MainWindow_TRAINgypsum", "Heavy", None))
        self.radioButton_LIGHT.setText(_translate("MainWindow_TRAINgypsum", "Light", None))

