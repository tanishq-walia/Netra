import sys
from PyQt4 import QtGui, QtCore, Qt
from METER_ui import Ui_MainWindow_AnalogMETER
import coreLib.linregr as linear

class Gui(QtGui.QMainWindow):

	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow_AnalogMETER()
		self.ui.setupUi(self)
		self.output = ""
		self.mode = "METER"
		self.behaviour()

	def reset(self):
		self.ui.lineEdit_METERreading.clear()
		self.ui.textBrowser_ACTUALreading.clear()

	def updateOutput(self, output):
		self.ui.textBrowser_ACTUALreading.setText(output)

	def calculate(self):
		supress = False
		if self.ui.checkBox_SUPRESS.isChecked():
			supress = True
		l = linear.linearRegression( self.mode, supress, XLABEL="Meter Readings", YLABEL="Laboratory Reading", TITLE=self.mode)
		self.output = str(l.predict(float(self.ui.lineEdit_METERreading.text())))
		self.updateOutput(self.output)
	
	def behaviour(self):
		self.connect(self.ui.pushButton_RESET, Qt.SIGNAL("clicked()"), self.reset)
		self.connect(self.ui.pushButton_CALCULATE, Qt.SIGNAL("clicked()"), self.calculate)

def main():
	app = QtGui.QApplication(sys.argv)
	ex = Gui()
	ex.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()