import sys
import os
import numpy as np
from PyQt4 import QtGui, QtCore, Qt
from TRAIN_ui import Ui_MainWindow_TRAINphNmoisture
import coreLib.SessionManager as session
import coreLib.multlin as multi
import coreLib.grabCut as grabCut
import coreLib.imFormat as imFormat
import coreLib.imProcess as imProcess

class Gui(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow_TRAINphNmoisture()
		self.ui.setupUi(self)
		self.supressVisualtizaion = False
		self.mode = "MOISTURE"
		self.imageMode = "RGB"
		self.imageList = list()
		self.coeflist = None
		self.database = session.database(self.mode)
		self.session = session.configuration()
		self.DATA = None
		self.dimensions = None
		self.LAB = False
		self.behaviour()

	def behaviour(self):
		self.connect(self.ui.radio_MOISTURE, Qt.SIGNAL("clicked()"), self.radioSignal)
		self.connect(self.ui.radio_PHVALUE, Qt.SIGNAL("clicked()"), self.radioSignal)
		self.connect(self.ui.checkBox_LAB, Qt.SIGNAL("clicked()"), self.options)
		self.connect(self.ui.radioButton_HSV, Qt.SIGNAL("clicked()"), self.imageModeFeatures)
		self.connect(self.ui.radioButton_RGB, Qt.SIGNAL("clicked()"), self.imageModeFeatures)
		self.connect(self.ui.radioButton_NDVI, Qt.SIGNAL("clicked()"), self.imageModeFeatures)
		self.connect(self.ui.pushButton_SELECT, Qt.SIGNAL("clicked()"), self.selectImageFiles)
		self.connect(self.ui.pushButton_EXTRACT, Qt.SIGNAL("clicked()"), self.extract)
		self.connect(self.ui.checkBox_SUPRESSvisualization, Qt.SIGNAL("clicked()"), self.options)
		self.connect(self.ui.pushButton_EDIT, Qt.SIGNAL("clicked()"), self.edit)

	def radioSignal(self):
		if self.ui.radio_MOISTURE.isChecked():
			self.mode = "MOISTURE"
		elif self.ui.radio_PHVALUE.isChecked():
			self.mode = "PH"
		self.database = session.database(self.mode)
		
	def options(self):
		self.supressVisualtizaion = self.ui.checkBox_SUPRESSvisualization.isChecked()
		self.LAB = self.ui.checkBox_LAB.isChecked()

	def imageModeFeatures(self):
		if self.ui.radioButton_RGB.isChecked():
			self.imageMode = "RGB"
		if self.ui.radioButton_RGBHSV.isChecked():
			self.imageMode = "HSV"
		if self.ui.radioButton_RGBNDVI.isChecked():
			self.imageMode = "NDVI"

	def selectFiles(self, parameter):
		imlist = list()
		for path in QtGui.QFileDialog.getOpenFileNames(self, parameter, self.session.getDirectory(self.mode)):
			imlist.append(str(path))
		filelist = sorted(imlist, key=lambda x: int(x.split(self.session.delimiter)[-1].split('_')[0]))
		self.dimensions = len(filelist)
		return filelist

	def selectImageFiles(self):
		self.imageList = self.selectFiles("Select Files")
		data = None
		if self.imageList == list():
			data = "WARNING! No files have been selected. Image list is empty!"
		else:
			data = "All files in the list to be processed are :\n"
			for item in self.imageList:
				data +=item.split(self.session.delimiter)[-1] + "\n"
		self.showdialog(data)

	def train(self):
		l = multi.similarityRanking( self.mode, self.dimensions, self.supressDATAGraph)
		l.train(visualize=self.supressVisualtizaion)
		self.showdialog("Training complete !")

	def showdialog(self, parameter):
		msg = QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Information)
		msg.setText(parameter)
		msg.setWindowTitle("Notice")
		msg.setStandardButtons(QtGui.QMessageBox.Ok)
		return msg.exec_()

	def getInput(self, parameter):
		text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', parameter)
		if ok:
		   return str(text)
		return None

	def imSegment(self, filelist, imageMode):
		mlist = list()
		if imageMode == "RGB":
			for path in filelist:
				print("\n"+path+"\r")
				image1 = grabCut.getGrabCutImage(imFormat.imread(path))
				m1, m2, m3 = imProcess.getMeanComponents(imProcess.sampleImage(image1, LAB=self.LAB))
				mlist.append([m1, m2, m3])
		elif imageMode == "HSV":
			for path in filelist:
				print("\n"+path+"\r")
				image1 = grabCut.getGrabCutImage(imFormat.rgb2hsv(imFormat.imread(path)))
				m1, m2, m3 = imProcess.getMeanComponents(imProcess.sampleImage(image1, LAB=self.LAB))
				mlist.append([m1, m2, m3])
		elif imageMode == "NDVI":
			for path in filelist:
				print("\n"+path+"\r")
				image1 = grabCut.getGrabCutImage(imFormat.NDVICalc(imFormat.imread(path)))
				m1, m2, m3 = imProcess.getMeanComponents(imProcess.sampleImage(image1, LAB=self.LAB))
				mlist.append([m1, m2, m3])
		print(mlist)
		return mlist

	def getDeltaEValues(self, filelist, imageMode):
		deltalist = list()
		deltaVector = list()
		self.coeflist = self.imSegment(filelist, imageMode)
		for v1 in self.coeflist:
			for v2 in self.coeflist:
				delta = imProcess.getDelta(v1[0], v1[1], v1[2], v2[0], v2[1], v1[2])
				print delta
				deltaVector.append(delta)
			deltalist.append(deltaVector)
			deltaVector = list()
		self.coeflist = np.array(self.coeflist)
		return np.array(deltalist)

	def updateDATA(self):
		print("Validation check and raw data extraction complete")
		print("Parsing Data...")
		self.DATA = self.getDeltaEValues(self.imageList, self.imageMode)

	def saveToFile(self):
		print("Saving the data to data file ...")
		np.savetxt(self.database.dataFile, self.DATA, delimiter = self.database.dataDelimiter)
		print("Saving the coefficients to output file ...")
		np.savetxt(self.database.outputFile, self.coeflist, delimiter = self.database.dataDelimiter)
		print("Finished!")

	def extract(self):
		self.updateDATA()
		self.saveToFile()
		self.showdialog("Extraction of features completed !")

	def edit(self):
		data = np.loadtxt(self.database.dataFile, delimiter = self.database.dataDelimiter).tolist()
		newData = list()
		i = 1
		for item in data:
			vector=list()
			for element in item:
				vector.append(element)
			val = None
			while val == None :
				val = float(self.getInput("Enter reference "+str(i)+" :"))
			vector.append(val)
			print vector
			newData.append(vector)
			i += 1
		newData = np.array(newData)
		print("Saving the data to data file ...")
		np.savetxt(self.database.dataFile, newData, delimiter = self.database.dataDelimiter)
		if self.showdialog("Would you like to view the raw file ?") == 1024:
			os.startfile(self.database.dataFile)

def main():
	app = QtGui.QApplication(sys.argv)
	ex = Gui()
	ex.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
