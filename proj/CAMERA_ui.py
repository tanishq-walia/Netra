# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CAMERA.ui'
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

class Ui_MainWindow_CAMERA(object):
    def setupUi(self, MainWindow_CAMERA):
        MainWindow_CAMERA.setObjectName(_fromUtf8("MainWindow_CAMERA"))
        MainWindow_CAMERA.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow_CAMERA.resize(752, 498)
        MainWindow_CAMERA.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow_CAMERA)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(510, 10, 231, 381))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_CAPTURE = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_CAPTURE.setGeometry(QtCore.QRect(10, 20, 101, 71))
        self.pushButton_CAPTURE.setObjectName(_fromUtf8("pushButton_CAPTURE"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(120, 20, 101, 71))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.radio_NGB = QtGui.QRadioButton(self.groupBox_4)
        self.radio_NGB.setGeometry(QtCore.QRect(20, 40, 71, 20))
        self.radio_NGB.setObjectName(_fromUtf8("radio_NGB"))
        self.radio_RGB = QtGui.QRadioButton(self.groupBox_4)
        self.radio_RGB.setGeometry(QtCore.QRect(20, 10, 72, 17))
        self.radio_RGB.setObjectName(_fromUtf8("radio_RGB"))
        self.groupBox_7 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 100, 211, 171))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.pushButton_SHOWfromStream = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_SHOWfromStream.setGeometry(QtCore.QRect(10, 20, 91, 41))
        self.pushButton_SHOWfromStream.setObjectName(_fromUtf8("pushButton_SHOWfromStream"))
        self.pushButton_SHOWdvi = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_SHOWdvi.setGeometry(QtCore.QRect(110, 120, 91, 41))
        self.pushButton_SHOWdvi.setObjectName(_fromUtf8("pushButton_SHOWdvi"))
        self.pushButton_SHOWlab = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_SHOWlab.setGeometry(QtCore.QRect(110, 70, 91, 41))
        self.pushButton_SHOWlab.setObjectName(_fromUtf8("pushButton_SHOWlab"))
        self.pushButton_SHOWfromPath = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_SHOWfromPath.setGeometry(QtCore.QRect(110, 20, 91, 41))
        self.pushButton_SHOWfromPath.setObjectName(_fromUtf8("pushButton_SHOWfromPath"))
        self.pushButton_SHOWnir = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_SHOWnir.setGeometry(QtCore.QRect(10, 70, 91, 41))
        self.pushButton_SHOWnir.setObjectName(_fromUtf8("pushButton_SHOWnir"))
        self.pushButton_SHOWndvi = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_SHOWndvi.setGeometry(QtCore.QRect(10, 120, 91, 41))
        self.pushButton_SHOWndvi.setObjectName(_fromUtf8("pushButton_SHOWndvi"))
        self.radio_COLOUR = QtGui.QRadioButton(self.groupBox_2)
        self.radio_COLOUR.setGeometry(QtCore.QRect(130, 340, 91, 20))
        self.radio_COLOUR.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radio_COLOUR.setObjectName(_fromUtf8("radio_COLOUR"))
        self.radio_MOISTURE = QtGui.QRadioButton(self.groupBox_2)
        self.radio_MOISTURE.setGeometry(QtCore.QRect(10, 310, 72, 17))
        self.radio_MOISTURE.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radio_MOISTURE.setObjectName(_fromUtf8("radio_MOISTURE"))
        self.radio_LEAF = QtGui.QRadioButton(self.groupBox_2)
        self.radio_LEAF.setGeometry(QtCore.QRect(10, 340, 81, 20))
        self.radio_LEAF.setObjectName(_fromUtf8("radio_LEAF"))
        self.radio_PHVALUE = QtGui.QRadioButton(self.groupBox_2)
        self.radio_PHVALUE.setGeometry(QtCore.QRect(10, 280, 41, 17))
        self.radio_PHVALUE.setObjectName(_fromUtf8("radio_PHVALUE"))
        self.radio_MOISTUREindicator = QtGui.QRadioButton(self.groupBox_2)
        self.radio_MOISTUREindicator.setGeometry(QtCore.QRect(90, 310, 131, 20))
        self.radio_MOISTUREindicator.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radio_MOISTUREindicator.setObjectName(_fromUtf8("radio_MOISTUREindicator"))
        self.radio_PHVALUEindicator = QtGui.QRadioButton(self.groupBox_2)
        self.radio_PHVALUEindicator.setGeometry(QtCore.QRect(90, 280, 131, 20))
        self.radio_PHVALUEindicator.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radio_PHVALUEindicator.setObjectName(_fromUtf8("radio_PHVALUEindicator"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 400, 731, 51))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.lineEdit_FILEpath = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_FILEpath.setGeometry(QtCore.QRect(120, 10, 601, 31))
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
        self.groupBox_6 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(9, 450, 731, 41))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.label = QtGui.QLabel(self.groupBox_6)
        self.label.setGeometry(QtCore.QRect(10, 20, 691, 16))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow_CAMERA.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_CAMERA)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_CAMERA)

    def retranslateUi(self, MainWindow_CAMERA):
        MainWindow_CAMERA.setWindowTitle(_translate("MainWindow_CAMERA", "CAMERA ", None))
        self.groupBox_2.setTitle(_translate("MainWindow_CAMERA", "Controls", None))
        self.pushButton_CAPTURE.setText(_translate("MainWindow_CAMERA", "CAPTURE", None))
        self.radio_NGB.setText(_translate("MainWindow_CAMERA", "NGB Mode", None))
        self.radio_RGB.setText(_translate("MainWindow_CAMERA", "RGB Mode", None))
        self.groupBox_7.setTitle(_translate("MainWindow_CAMERA", "Show", None))
        self.pushButton_SHOWfromStream.setText(_translate("MainWindow_CAMERA", "STREAM", None))
        self.pushButton_SHOWdvi.setText(_translate("MainWindow_CAMERA", "DVI", None))
        self.pushButton_SHOWlab.setText(_translate("MainWindow_CAMERA", "LAB", None))
        self.pushButton_SHOWfromPath.setText(_translate("MainWindow_CAMERA", "PATH", None))
        self.pushButton_SHOWnir.setText(_translate("MainWindow_CAMERA", "NIR", None))
        self.pushButton_SHOWndvi.setText(_translate("MainWindow_CAMERA", "NDVI", None))
        self.radio_COLOUR.setText(_translate("MainWindow_CAMERA", "LEAF COLOUR", None))
        self.radio_MOISTURE.setText(_translate("MainWindow_CAMERA", "MOISTURE", None))
        self.radio_LEAF.setText(_translate("MainWindow_CAMERA", "LEAF AREA", None))
        self.radio_PHVALUE.setText(_translate("MainWindow_CAMERA", "PH", None))
        self.radio_MOISTUREindicator.setText(_translate("MainWindow_CAMERA", "MOISTURE INDICATOR", None))
        self.radio_PHVALUEindicator.setText(_translate("MainWindow_CAMERA", "PH INDICATOR", None))
        self.pushButton_SELECT.setText(_translate("MainWindow_CAMERA", "SELECT FILE", None))
        self.groupBox.setTitle(_translate("MainWindow_CAMERA", "Display", None))
        self.label_FEEDLABEL.setText(_translate("MainWindow_CAMERA", "Feed Label", None))
        self.groupBox_6.setTitle(_translate("MainWindow_CAMERA", "STATUS", None))
        self.label.setText(_translate("MainWindow_CAMERA", "TextLabel", None))

