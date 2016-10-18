# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'METER.ui'
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

class Ui_MainWindow_AnalogMETER(object):
    def setupUi(self, MainWindow_AnalogMETER):
        MainWindow_AnalogMETER.setObjectName(_fromUtf8("MainWindow_AnalogMETER"))
        MainWindow_AnalogMETER.resize(479, 159)
        self.centralwidget = QtGui.QWidget(MainWindow_AnalogMETER)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 461, 141))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit_METERreading = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_METERreading.setGeometry(QtCore.QRect(10, 60, 211, 31))
        self.lineEdit_METERreading.setObjectName(_fromUtf8("lineEdit_METERreading"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(80, 40, 71, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowser_ACTUALreading = QtGui.QTextBrowser(self.groupBox)
        self.textBrowser_ACTUALreading.setGeometry(QtCore.QRect(240, 60, 211, 31))
        self.textBrowser_ACTUALreading.setObjectName(_fromUtf8("textBrowser_ACTUALreading"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(310, 40, 81, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_RESET = QtGui.QPushButton(self.groupBox)
        self.pushButton_RESET.setGeometry(QtCore.QRect(240, 100, 211, 31))
        self.pushButton_RESET.setObjectName(_fromUtf8("pushButton_RESET"))
        self.pushButton_CALCULATE = QtGui.QPushButton(self.groupBox)
        self.pushButton_CALCULATE.setGeometry(QtCore.QRect(10, 100, 211, 31))
        self.pushButton_CALCULATE.setObjectName(_fromUtf8("pushButton_CALCULATE"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 441, 31))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.checkBox_SUPRESS = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_SUPRESS.setGeometry(QtCore.QRect(40, -1, 371, 31))
        self.checkBox_SUPRESS.setObjectName(_fromUtf8("checkBox_SUPRESS"))
        MainWindow_AnalogMETER.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_AnalogMETER)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_AnalogMETER)

    def retranslateUi(self, MainWindow_AnalogMETER):
        MainWindow_AnalogMETER.setWindowTitle(_translate("MainWindow_AnalogMETER", "Corelation Value", None))
        self.label.setText(_translate("MainWindow_AnalogMETER", "Meter Reading", None))
        self.label_2.setText(_translate("MainWindow_AnalogMETER", "Correlated Value", None))
        self.pushButton_RESET.setText(_translate("MainWindow_AnalogMETER", "RESET", None))
        self.pushButton_CALCULATE.setText(_translate("MainWindow_AnalogMETER", "CALCULATE", None))
        self.checkBox_SUPRESS.setText(_translate("MainWindow_AnalogMETER", "Supress the graph showing the regression equation and training dataset", None))

