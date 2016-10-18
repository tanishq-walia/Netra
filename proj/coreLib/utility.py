import cv2
import numpy as np
from PyQt4 import QtGui, QtCore, Qt

class Video():
	def __init__(self,capture):
		self.capture = capture
		self.currentFrame=np.array([])

	def captureNextFrame(self):
		"""                           
		capture frame and reverse RBG BGR and return opencv image                                      
		"""
		ret, readFrame=self.capture.read()
		if(ret==True):
			#self.currentFrame = readFrame
			self.currentFrame=cv2.cvtColor(readFrame,cv2.COLOR_BGR2RGB)

	def convertFrame(self):
		"""     converts frame to format suitable for QtGui            """
		try:
			height,width=self.currentFrame.shape[:2]
			img=QtGui.QImage(self.currentFrame,
							  width,
							  height,
							  QtGui.QImage.Format_RGB888)
			img=QtGui.QPixmap.fromImage(img)
			self.previousFrame = self.currentFrame
			return img
		except:
			return None