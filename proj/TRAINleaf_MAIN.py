import sys
import os
from PyQt4 import QtGui, QtCore, Qt
from TRAIN_ui import Ui_MainWindow_TRAIN
import coreLib.SessionManager as session


class Gui(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow_TRAIN()
		self.ui.setupUi(self)
		self.behaviour()
		self.supressRegression = False
		self.supressVisualtizaion = False
		self.mode = "GYPSUM_H"
		self.database = session.database(self.mode)

	def behaviour(self):
		self.connect(self.ui.pushButton_EDIT, Qt.SIGNAL("clicked()"), self.edit)
		self.connect(self.ui.pushButton_TRAIN, Qt.SIGNAL("clicked()"), self.train)
		self.connect(self.ui.checkBox_SUPRESSregression, Qt.SIGNAL("clicked()"), self.options)
		self.connect(self.ui.checkBox_SUPRESSvisualization, Qt.SIGNAL("clicked()"), self.options)
		self.connect(self.ui.radioButton_HEAVY, Qt.SIGNAL("clicked()"), self.radioSignal)
		self.connect(self.ui.radioButton_LIGHT, Qt.SIGNAL("clicked()"), self.radioSignal)
		self.connect(self.ui.radioButton_MEDIUM, Qt.SIGNAL("clicked()"), self.radioSignal)

	def radioSignal(self):
		if self.ui.radioButton_HEAVY.isChecked():
			self.mode = "GYPSUM_H"
		elif self.ui.radioButton_LIGHT.isChecked():
			self.mode = "GYPSUM_L"
		elif self.ui.radioButton_MEDIUM.isChecked():
			self.mode = "GYPSUM_M"
		self.database = session.database(self.mode)
	
	def edit(self):
		os.startfile(self.database.dataFile)

	def train(self):
		ALPHA = 0
		ITERATIONS = 0
		try:
			ALPHA = float(str(self.ui.lineEdit_ALPHA.text()))
			ITERATIONS = int(str(self.ui.lineEdit_ITERATION.text()))
		except:
			ALPHA = 0.001
			ITERATIONS = 40000
		l = linear.linearRegression( self.mode, self.supressRegression, XLABEL="pH Readings", YLABEL="Gypsum Requirement", TITLE=self.mode, alpha=ALPHA, iterations=ITERATIONS)
		print self.supressVisualtizaion
		l.train(visualize=self.supressVisualtizaion)
		self.showdialog()

	def showdialog(self):
		msg = QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Information)
		msg.setText("Training complete !")
		msg.setWindowTitle("Notice")
		msg.setStandardButtons(QtGui.QMessageBox.Ok)
		return msg.exec_()

	def options(self):
		self.supressRegression = self.ui.checkBox_SUPRESSregression.isChecked()
		self.supressVisualtizaion = self.ui.checkBox_SUPRESSvisualization.isChecked()

def main():
	app = QtGui.QApplication(sys.argv)
	ex = Gui()
	ex.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

