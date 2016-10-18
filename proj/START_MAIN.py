import sys
import os
from PyQt4 import QtGui, QtCore, Qt
from START_ui import Ui_MainWindow_START
import coreLib.SessionManager as session
import subprocess

class Gui(QtGui.QMainWindow):

	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow_START()
		self.ui.setupUi(self)
		self.pathPrefix = session.configuration().getPath2Scripts()+'\\'
		self.behaviour()

	def executeScript(self, parameter):
		print("intiating the process ... please wait")
		batch_filename = self.pathPrefix + parameter
		print("starting...")
		os.startfile(batch_filename)
		print("done")

	def behaviour(self):
		self.connect(self.ui.pushButton_PH_Moisture, Qt.SIGNAL("clicked()"), self.pHnMoisture)
		self.connect(self.ui.pushButton_ANALOGmeter, Qt.SIGNAL("clicked()"), self.analogMeter)
		self.connect(self.ui.pushButton_LEAFAREAMETER, Qt.SIGNAL("clicked()"), self.leafAreaMeter)
		self.connect(self.ui.pushButton_GYPSUM, Qt.SIGNAL("clicked()"), self.gypsum)
		self.connect(self.ui.pushButton_LEAFCOLOURurea, Qt.SIGNAL("clicked()"), self.urea)
		self.connect(self.ui.pushButton_ACQUIREimages, Qt.SIGNAL("clicked()"), self.acquireImages)
		self.connect(self.ui.pushButton_HELP, Qt.SIGNAL("clicked()"), self.help)
		self.connect(self.ui.pushButton_LOG, Qt.SIGNAL("clicked()"), self.log)
		self.connect(self.ui.pushButton_TRAINanalogMeter, Qt.SIGNAL("clicked()"), self.trainAnalogMeter)
		self.connect(self.ui.pushButton_TRAINgypsum, Qt.SIGNAL("clicked()"), self.trainGypsum)
		self.connect(self.ui.pushButton_TRAINleaf, Qt.SIGNAL("clicked()"), self.trainLeaf)
		self.connect(self.ui.pushButton_TRAINurea, Qt.SIGNAL("clicked()"), self.trainUrea)
		self.connect(self.ui.pushButton_TRAINphNmoisture, Qt.SIGNAL("clicked()"), self.trainPhNMoisture)
		self.connect(self.ui.pushButton_PREDICTORindicator, Qt.SIGNAL("clicked()"), self.indicator)
		self.connect(self.ui.pushButton_TRAINindicator, Qt.SIGNAL("clicked()"), self.trainIndicator)
		self.connect(self.ui.pushButton_SYSTEM, Qt.SIGNAL("clicked()"), self.system)

	def system(self):
		pass
		
	def indicator(self):
		self.executeScript("PREDICTORindicator.bat")

	def trainIndicator(self):
		self.executeScript("TRAINindicator.bat")

	def urea(self):
		self.executeScript("PREDICTORcolour.bat")

	def acquireImages(self):
		self.executeScript("CAMERA.bat")

	def help(self):
		self.executeScript("HELP.bat")

	def log(self):
		self.executeScript("LOG.bat")

	def trainAnalogMeter(self):
		self.executeScript("TRAINmeter.bat")

	def trainGypsum(self):
		self.executeScript("TRAINgypsum.bat")

	def trainLeaf(self):
		self.executeScript("TRAINleaf.bat")

	def trainUrea(self):
		self.executeScript("TRAINcolour.bat")

	def trainPhNMoisture(self):
		self.executeScript("TRAIN.bat")

	def pHnMoisture(self):
		self.executeScript("PREDICTOR.bat")

	def analogMeter(self):
		self.executeScript("METER.bat")
				
	def gypsum(self):
		self.executeScript("PREDICTORgypsum.bat")

	def leafAreaMeter(self):
		self.executeScript("PREDICTORleaf.bat")

def main():
	app = QtGui.QApplication(sys.argv)
	ex = Gui()
	ex.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	if os.getcwd() not in sys.path:
			sys.path.append(os.getcwd())
	main()
