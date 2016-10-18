import sys
import coreLib.linregr as linear
from PyQt4 import QtGui, QtCore, Qt
from PREDICTORgypsum_ui import Ui_MainWindow_Gypsum 
from decimal import *

class Gui(QtGui.QMainWindow):

	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow_Gypsum()
		self.ui.setupUi(self)
		self.output = ""
		self.application = ""
		self.behaviour()

	def reset(self):
		self.ui.lineEdit_pHValue.clear()
		self.ui.textBrowser_GYPSUMestimate.clear()

	def updateOutput(self, output):
		self.ui.textBrowser_GYPSUMestimate.setText(output)
		print("Finished")

	def radioSignal(self):
		if self.ui.radioButton_HEAVY.isChecked():
			self.application = "GYPSUM_H"
		if self.ui.radioButton_LIGHT.isChecked():
			self.application = "GYPSUM_L"
		if self.ui.radioButton_MEDIUM.isChecked():
			self.application = "GYPSUM_M"
		print("application mode is: "+self.application)

	def poly(self, a, b, c, d, x):
		getcontext().prec = 40
		a = Decimal(a)
		b = Decimal(b)
		c = Decimal(c)
		d = Decimal(d)
		x = Decimal(x)
		y = ( a + ( b * x ) ) / ( 1 + ( c * x ) + ( d * x * x ) )
		return float(y)

	def calculate(self):
		def value(parameter):
			return format(parameter, '.25g')
		supress = False
		val = 0.0
		if self.ui.checkBox_Polyfit.isChecked():
			self.ui.checkBox_SUPRESS.setCheckState(False)
			if self.application == "GYPSUM_H":
				val = self.poly(-3.9558679, 0.45971327, -0.21049008, 0.011477248, float(str(self.ui.lineEdit_pHValue.text())))
				self.output = str(val)
				print self.output
			if self.application == "GYPSUM_L":
				val = self.poly(-6.306401,  0.71471308, -0.18657624, 0.0086433375, float(str(self.ui.lineEdit_pHValue.text())))
				self.output = str(val)
				print self.output
			if self.application == "GYPSUM_M":
				val = self.poly(-18.570644, 2.1295611, -0.20118166, 0.012205188, float(str(self.ui.lineEdit_pHValue.text())))
				self.output = str(val) 
				print self.output
		else:
			if self.ui.checkBox_SUPRESS.isChecked():
				supress = True
			l = linear.linearRegression(self.application, supress, XLABEL="pH", YLABEL="Gypsum requirement", TITLE="GYPSUM ESTIMATION")
			self.output = str(l.predict(float(self.ui.lineEdit_pHValue.text())))
		self.updateOutput(self.output)
	
	def behaviour(self):
		self.connect(self.ui.pushButton_ESTIMATEvalue , Qt.SIGNAL("clicked()"), self.calculate)
		self.connect(self.ui.radioButton_HEAVY , Qt.SIGNAL("clicked()"), self.radioSignal)
		self.connect(self.ui.pushButton_RESET, Qt.SIGNAL("clicked()"), self.reset)
		self.connect(self.ui.radioButton_LIGHT , Qt.SIGNAL("clicked()"), self.radioSignal)
		self.connect(self.ui.radioButton_MEDIUM , Qt.SIGNAL("clicked()"), self.radioSignal)

def main():
	app = QtGui.QApplication(sys.argv)
	ex = Gui()
	ex.show()
	sys.exit(app.exec_())
 
if __name__ == '__main__':
	main()