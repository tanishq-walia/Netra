import sys
import os
import cv2
import numpy as np
from PyQt4 import QtGui, QtCore, Qt
import coreLib.imFormat as imFormat
from CAMERA_ui import Ui_MainWindow_CAMERA
import coreLib.SessionManager as SessionManager
from coreLib.utility import Video
			
class Gui(QtGui.QMainWindow):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_MainWindow_CAMERA()
		self.ui.setupUi(self)
		self.video = Video(cv2.VideoCapture(0))
		self._timer = QtCore.QTimer(self)
		self._timer.timeout.connect(self.play)
		self._timer.start(27)
		self.session = SessionManager.configuration()
		self.imageName = self.session.DATA_PREFIX+"default.jpg"
		self.recent = self.session.DATA_PREFIX+"default.jpg"
		self.filename = ""
		self.extension = ""
		self.colour = "RGB"
		self.captureMode = "MOISTURE"
		self.behaviour()
		self.statusString = "Initialized camera . . . "
		self.ui.label.setText(self.statusString)

		
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
		self.connect(self.ui.pushButton_SHOWfromStream, Qt.SIGNAL("clicked()"), self.showFromStream)
		self.connect(self.ui.pushButton_SHOWfromPath, Qt.SIGNAL("clicked()"), self.showFromPath)
		self.connect(self.ui.pushButton_SELECT, Qt.SIGNAL("clicked()"), self.select)
		self.connect(self.ui.pushButton_SHOWndvi, Qt.SIGNAL("clicked()"), self.showNdvi)
		self.connect(self.ui.pushButton_SHOWdvi, Qt.SIGNAL("clicked()"), self.showDvi)
		self.connect(self.ui.pushButton_SHOWnir, Qt.SIGNAL("clicked()"), self.showNir)
		self.connect(self.ui.pushButton_SHOWlab, Qt.SIGNAL("clicked()"), self.showLab)
		self.connect(self.ui.radio_COLOUR, Qt.SIGNAL("clicked()"), self.radioSignal)
		self.connect(self.ui.radio_LEAF, Qt.SIGNAL("clicked()"), self.radioSignal)
		self.connect(self.ui.radio_MOISTURE, Qt.SIGNAL("clicked()"), self.radioSignal)
		self.connect(self.ui.radio_PHVALUE, Qt.SIGNAL("clicked()"), self.radioSignal)
		self.connect(self.ui.radio_PHVALUEindicator, Qt.SIGNAL("clicked()"), self.radioSignal)
		self.connect(self.ui.radio_MOISTUREindicator, Qt.SIGNAL("clicked()"), self.radioSignal)
		self.connect(self.ui.radio_NGB, Qt.SIGNAL("clicked()"), self.radioSignal)
		self.connect(self.ui.radio_RGB, Qt.SIGNAL("clicked()"), self.radioSignal)

	def updateStatus(self, parameter):
		self.statusString = parameter
		self.ui.label.setText(self.statusString)

	def radioSignal(self):
		if self.ui.radio_RGB.isChecked():
			self.colour = "RGB"
		elif self.ui.radio_NGB.isChecked():
			self.colour = "NGB"
		if self.ui.radio_COLOUR.isChecked():
			self.captureMode = "COLOUR"
		elif self.ui.radio_LEAF.isChecked():
			self.captureMode = "LEAF"
		elif self.ui.radio_MOISTURE.isChecked():
			self.captureMode = "MOISTURE"
		elif self.ui.radio_PHVALUE.isChecked():
			self.captureMode = "PH"
		elif self.ui.radio_MOISTUREindicator.isChecked():
			self.captureMode = "MOISTURE_INDICATOR"
		elif self.ui.radio_PHVALUEindicator.isChecked():
			self.captureMode = "PH_INDICATOR"

	def capture(self):
		self.video.captureNextFrame()
		print("Equalizing luminence")
		image = imFormat.bgr2rgb(imFormat.equalize(self.video.currentFrame))
		self.session.refresh(self.captureMode)
		self.recent = self.session.imageFilename(self.captureMode, self.colour)
		cv2.imwrite(self.recent, image)
		self.updateStatus("captured : "+ self.recent)

	def select(self):
		filename = QtGui.QFileDialog.getOpenFileName(self, "Select File", self.session.getDirectory(self.captureMode))
		self.ui.lineEdit_FILEpath.setText(str(filename))
		self.recent = filename

	def showFromStream(self):
		cv2.imshow("Captured Image", imFormat.imread(self.recent))
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	def showFromPath(self):
		cv2.imshow("Selected Image", imFormat.imread(self.recent))
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	def showNdvi(self):
		cv2.imshow("NDVI Image", imFormat.NDVICalc(imFormat.imread(self.recent)))
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	def showDvi(self):
		cv2.imshow("DVI Image", imFormat.DVICalc(imFormat.imread(self.recent)))
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	def showNir(self):
		cv2.imshow("NIR Image", imFormat.NIRCalc(imFormat.imread(self.recent)))
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	def showLab(self):
		cv2.imshow("LAB Image", imFormat.rgb2lab(imFormat.imread(self.recent)))
		cv2.waitKey(0)
		cv2.destroyAllWindows()

def main():
	app = QtGui.QApplication(sys.argv)
	ex = Gui()
	ex.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()