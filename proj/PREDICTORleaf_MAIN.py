import sys
import numpy as np
import cv2
import coreLib.calibrate as calibrate
import coreLib.grabCut as grabCut
import coreLib.SessionManager as SessionManager
import coreLib.imFormat as imFormat 
from PyQt4 import QtGui, QtCore, Qt
from PREDICTORleaf_ui import Ui_MainWindow_PREDICRTORleaf
from coreLib.utility import Video

class Gui(QtGui.QMainWindow):

	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.session = SessionManager.configuration()
		self.ui = Ui_MainWindow_PREDICRTORleaf()
		self.ui.setupUi(self)
		self.video = Video(cv2.VideoCapture(0))
		self._timer = QtCore.QTimer(self)
		self._timer.timeout.connect(self.play)
		self._timer.start(27)
		self.behaviour()
		self.imageName = self.session.DATA_PREFIX+"default.jpg"
		self.recent = self.session.DATA_PREFIX+"default.jpg"
		self.filename = ""
		self.extension = ""
		self.cameraMode = "RGB"
		self.resizeFactor = 1.0
		self.length = 0.0
		self.units = "centimeters"
		self.mode = "LEAF"

	def play(self):
		try:
			self.video.captureNextFrame()
			self.ui.label_FEEDLABEL.setPixmap(
				self.video.convertFrame())
			self.ui.label_FEEDLABEL.setScaledContents(True)
		except TypeError:
			print("No frame")


	def behaviour(self):
		self.connect(self.ui.pushButton_CAPTURE, Qt.SIGNAL("clicked()"), self.capture)
		self.ui.radio_NGB.toggled.connect(self.radioSignal)
		self.connect(self.ui.pushButton_CALCULATEfromPath, Qt.SIGNAL("clicked()"), self.calculateFromPath)
		self.connect(self.ui.pushButton_CALCULATEfromStream, Qt.SIGNAL("clicked()"), self.calculateFromStream)
		self.connect(self.ui.pushButton_SELECT, Qt.SIGNAL("clicked()"), self.select)
		self.connect(self.ui.pushButton_SET, Qt.SIGNAL("clicked()"), self.set)
		self.connect(self.ui.pushButton_SAVE, Qt.SIGNAL("clicked()"), self.save)
		self.connect(self.ui.pushButton_RESET, Qt.SIGNAL("clicked()"), self.reset)
		
	def radioSignal(self):
		if self.ui.radio_RGB.isChecked():
			self.cameraMode = "RGB"
		if self.ui.radio_NGB.isChecked():
			self.cameraMode = "NGB"

	def select(self):
		filename = QtGui.QFileDialog.getOpenFileName(self, "Select File", self.session.getDirectory(self.mode))
		self.ui.lineEdit_FILEpath.setText(str(filename))

	def capture(self):
		self.video.captureNextFrame()
		print("Equalizing luminence")
		image = imFormat.bgr2rgb(imFormat.equalize(self.video.currentFrame))
		self.session.refresh(self.mode)
		self.recent = self.session.imageFilename(self.mode, self.cameraMode)
		print("captured : "+self.recent)
		cv2.imwrite(self.recent, image)

	def save(self):
		pass

	def reset(self):
		self.ui.lineEdit_FILEpath.clear()
		self.ui.lineEdit_RESIZEfactor.clear()
		self.ui.lineEdit_CALIBRATIONvalue.clear()
		self.ui.lineEdit_CALIBRATIONunit.clear()
		self.ui.textBrowser_OUTPUT.clear()

	def set(self):
		self.imageName = str(self.ui.lineEdit_FILEpath.text())
		print self.imageName
		self.filename = self.imageName.split('.')[0]
		self.extension = self.imageName.split('.')[-1]
		self.resizeFactor = float(self.ui.lineEdit_RESIZEfactor.text())
		print self.resizeFactor

	def calculateFromStream(self):
		self.resizeFactor = float(self.ui.lineEdit_RESIZEfactor.text())
		self.imageName = self.recent
		print self.imageName
		print self.resizeFactor
		self.filename = self.imageName.split('.')[0]
		self.extension = self.imageName.split('.')[-1]
		self.calculateFromPath(True)
		
	def calculateFromPath(self , subcall=False):
		if not subcall:
			self.set()
		self.length = float(self.ui.lineEdit_CALIBRATIONvalue.text())
		self.units = str(self.ui.lineEdit_CALIBRATIONunit.text())
		while True:
			print 'Segmentation starting for '+ self.imageName+' ...'
			imageFile = grabCut.loadFile(self.filename, self.extension, self.resizeFactor)
			print '\nSegmentation Successfull!\n'
			realArea , units = calibrate.getArea(imageFile, self.length, self.units)
			print 'As per your reference calibration...\n'
			self.ui.textBrowser_OUTPUT.setText(str(realArea)+' '+units)
			if not self.showdialog() == 1024:
				break

	def showdialog(self):
		msg = QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Information)
		msg.setText("Would you like to extract the area again ?")
		msg.setInformativeText("Press Ok if YES and Cancel if NO")
		msg.setWindowTitle("Please answer")
		#msg.setDetailedText("The details are as follows:")
		msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
		return msg.exec_()


def main():
	app = QtGui.QApplication(sys.argv)
	ex = Gui()
	ex.show()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
