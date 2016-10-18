import sys
import numpy as np
import cv2
import coreLib.SessionManager as session
import coreLib.multlin as multi
import coreLib.grabCut as grabCut
import coreLib.imFormat as imFormat
import coreLib.imProcess as imProcess
from PyQt4 import QtGui, QtCore, Qt
from PREDICTOR_ui import Ui_MainWindow_PREDICTOR
from coreLib.utility import Video

class Gui(QtGui.QMainWindow):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.session = session.configuration()
		self.ui = Ui_MainWindow_PREDICTOR()
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
		self.imageMode = "RGB"
		self.LAB = False
		self.mode = "MOISTURE"
		self.imageList = list()
		

	def play(self):
		try:
			self.video.captureNextFrame()
			self.ui.label_FEEDLABEL.setPixmap(
				self.video.convertFrame())
			self.ui.label_FEEDLABEL.setScaledContents(True)
		except TypeError:
			print("No frame")

	def imageModeFeatures(self):
		if self.ui.radioButton_RGB.isChecked():
			self.imageMode = "RGB"
		if self.ui.radioButton_HSV.isChecked():
			self.imageMode = "HSV"
		if self.ui.radioButton_NDVI.isChecked():
			self.imageMode = "NDVI"

	def behaviour(self):
		self.connect(self.ui.pushButton_CAPTURE, Qt.SIGNAL("clicked()"), self.capture)
		self.connect(self.ui.radioButton_HSV, Qt.SIGNAL("clicked()"), self.imageModeFeatures)
		self.connect(self.ui.radioButton_RGB, Qt.SIGNAL("clicked()"), self.imageModeFeatures)
		self.connect(self.ui.radioButton_NDVI, Qt.SIGNAL("clicked()"), self.imageModeFeatures)
		self.connect(self.ui.radio_RGB, Qt.SIGNAL("clicked()"), self.radioSignal)
		self.connect(self.ui.radio_NGB, Qt.SIGNAL("clicked()"), self.radioSignal)
		self.connect(self.ui.radio_PHVALUE, Qt.SIGNAL("clicked()"), self.radioSignal)
		self.connect(self.ui.radio_MOISTURE, Qt.SIGNAL("clicked()"), self.radioSignal)
		self.connect(self.ui.checkBox_LAB, Qt.SIGNAL("clicked()"), self.radioSignal)
		self.connect(self.ui.pushButton_SET, Qt.SIGNAL("clicked()"), self.set)
		self.connect(self.ui.pushButton_SELECT, Qt.SIGNAL("clicked()"), self.select)
		self.connect(self.ui.pushButton_CALCULATEfromStream, Qt.SIGNAL("clicked()"), self.calculateFromStream)
		self.connect(self.ui.pushButton_CALCULATEfromPath, Qt.SIGNAL("clicked()"), self.calculateFromPath)		
		self.connect(self.ui.pushButton_SAVE, Qt.SIGNAL("clicked()"), self.save)
		self.connect(self.ui.pushButton_RESET, Qt.SIGNAL("clicked()"), self.reset)
		
	def select(self):
		filename = QtGui.QFileDialog.getOpenFileName(self, "Select File", self.session.getDirectory(self.mode))
		self.ui.lineEdit_FILEpath.setText(str(filename))
			
	def radioSignal(self):

		if self.ui.checkBox_LAB.isChecked():
			self.LAB = True
		else : self.LAB = False

		if self.ui.radio_MOISTURE.isChecked():
			self.mode = "MOISTURE"
		elif self.ui.radio_PHVALUE.isChecked():
			self.mode = "PH"

		if self.ui.radio_NGB.isChecked():
			self.cameraMode = "NGB"
		elif self.ui.radio_RGB.isChecked():
			self.cameraMode = "RGB"

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
		self.ui.textBrowser_OUTPUT.clear()

	def set(self):
		self.imageName = str(self.ui.lineEdit_FILEpath.text())
		print self.imageName
		self.filename = self.imageName.split('.')[0]
		self.extension = self.imageName.split('.')[-1]

	def calculateFromStream(self):
		self.imageName = self.recent
		print self.imageName
		self.filename = self.imageName.split('.')[0]
		self.extension = self.imageName.split('.')[-1]
		self.calculateFromPath(True)
		
	def calculateFromPath(self, subcall = False):
		if not subcall:
			self.set()
		while True:
			l = multi.similarityRanking(self.mode)
			targetVector = l.getTargetVector(self.imageName, self.imageMode, self.LAB)
			self.output = str(l.predict(targetVector))
			self.updateOutput(self.output)
			if not self.showdialog() == 1024:
				break

	def updateOutput(self, parameter):
		self.ui.textBrowser_OUTPUT.setText(str(parameter))
		print("Done!")

	def showdialog(self):
		msg = QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Information)
		msg.setText("Would you like to process the image again ?")
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
