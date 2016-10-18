
import os
import sys

class configuration():
	def __init__(self):	
		self.DATA_DIR = self.getPath2DATA()
		self.delimiter = "\\"
		self.DATA_PREFIX = self.DATA_DIR + self.delimiter
		
		self.LEAF_DIR = self.DATA_PREFIX + "LEAF"
		if not os.path.exists(self.LEAF_DIR):
			os.mkdir(self.LEAF_DIR)
		self.LEAF_PREFIX = self.LEAF_DIR + self.delimiter
		self.LEAF_PTR = 0
		
		self.PH_DIR = self.DATA_PREFIX + "PH"
		if not os.path.exists(self.PH_DIR):
			os.mkdir(self.PH_DIR)
		self.PH_PREFIX = self.PH_DIR + self.delimiter
		self.PH_PTR = 0
		
		self.PH_INDICATOR_DIR = self.DATA_PREFIX + "PH_INDICATOR"
		if not os.path.exists(self.PH_INDICATOR_DIR):
			os.mkdir(self.PH_INDICATOR_DIR)
		self.PH_INDICATOR_PREFIX = self.PH_INDICATOR_DIR + self.delimiter
		self.PH_INDICATOR_PTR = 0

		self.MOISTURE_INDICATOR_DIR = self.DATA_PREFIX + "MOISTURE_INDICATOR"
		if not os.path.exists(self.MOISTURE_INDICATOR_DIR):
			os.mkdir(self.MOISTURE_INDICATOR_DIR)
		self.MOISTURE_INDICATOR_PREFIX = self.MOISTURE_INDICATOR_DIR + self.delimiter
		self.MOISTURE_INDICATOR_PTR = 0

		self.MOISTURE_DIR = self.DATA_PREFIX + "MOISTURE"
		if not os.path.exists(self.MOISTURE_DIR):
			os.mkdir(self.MOISTURE_DIR)
		self.MOISTURE_PREFIX = self.MOISTURE_DIR + self.delimiter
		self.MOISTURE_PTR = 0		
		
		self.COLOUR_DIR = self.DATA_PREFIX + "COLOUR"
		if not os.path.exists(self.COLOUR_DIR):
			os.mkdir(self.COLOUR_DIR)
		self.COLOUR_PREFIX = self.COLOUR_DIR + self.delimiter
		self.COLOUR_PTR = 0	
		
		self.NN_DATA_DIR = self.DATA_PREFIX + "NN_DATA"
		if not os.path.exists(self.NN_DATA_DIR):
			os.mkdir(self.NN_DATA_DIR)
		self.NN_DATA_PREFIX = self.NN_DATA_DIR + self.delimiter
		self.NN_DATA_PTR = 0
		
		self.EXTENSION = ".jpg"
		self.dataEXTENSION = ".txt"
		self.logEXTENSION = ".txt"

		self.MoistureIndicatorData = self.NN_DATA_PREFIX + "MoistureIndicatorData" + self.dataEXTENSION
		self.PhIndicatorData = self.NN_DATA_PREFIX + "PhIndicatorData" + self.dataEXTENSION		
		self.LeafData = self.NN_DATA_PREFIX + "LeafData" + self.dataEXTENSION
		self.PhData = self.NN_DATA_PREFIX + "PhData" + self.dataEXTENSION
		self.MoistureData = self.NN_DATA_PREFIX + "MoistureData" + self.dataEXTENSION
		self.MeterData = self.NN_DATA_PREFIX + "MeterData" + self.dataEXTENSION
		self.GypsumData_H = self.NN_DATA_PREFIX + "GypsumData_H" + self.dataEXTENSION
		self.GypsumData_M = self.NN_DATA_PREFIX + "GypsumData_M" + self.dataEXTENSION
		self.GypsumData_L = self.NN_DATA_PREFIX + "GypsumData_L" + self.dataEXTENSION
		self.ColourData = self.NN_DATA_PREFIX + "ColourData" + self.dataEXTENSION
		
		self.MoistureIndicatorCoefficients = self.NN_DATA_PREFIX + "MoistureIndicatorCoefficients" + self.dataEXTENSION
		self.PhIndicatorCoefficients = self.NN_DATA_PREFIX + "PhIndicatorCoefficients" + self.dataEXTENSION
		self.LeafCoefficients = self.NN_DATA_PREFIX + "LeafCoefficients" + self.dataEXTENSION
		self.PhCoefficients = self.NN_DATA_PREFIX + "PhCoefficients" + self.dataEXTENSION
		self.MoistureCoefficients = self.NN_DATA_PREFIX + "MoistureCoefficients" + self.dataEXTENSION
		self.MeterCoefficients = self.NN_DATA_PREFIX + "MeterCoefficients" + self.dataEXTENSION
		self.GypsumCoefficients_H = self.NN_DATA_PREFIX +  "GypsumCoefficeints_H" + self.dataEXTENSION
		self.GypsumCoefficients_M = self.NN_DATA_PREFIX +  "GypsumCoefficeints_M" + self.dataEXTENSION
		self.GypsumCoefficients_L = self.NN_DATA_PREFIX +  "GypsumCoefficeints_L" + self.dataEXTENSION
		self.ColourCoefficients = self.NN_DATA_PREFIX + "ColourCoefficients" + self.dataEXTENSION

		self.PhIndicatorLog = self.DATA_PREFIX + "PhIndicatorLog" + self.logEXTENSION
		self.MoistureIndicatorLog = self.DATA_PREFIX + "MoistureIndicatorLog" + self.logEXTENSION		
		self.PhLog = self.DATA_PREFIX + "PhLog" + self.logEXTENSION
		self.MoistureLog = self.DATA_PREFIX + "MoistureLog" + self.logEXTENSION
		self.MeterLog = self.DATA_PREFIX + "MeterLog" + self.logEXTENSION
		self.LeafLog = self.DATA_PREFIX + "LeafLog" + self.logEXTENSION
		self.GypsumLog = self.DATA_PREFIX + "GypsumLog" + self.logEXTENSION
		self.ColourLog = self.DATA_PREFIX + "ColourLog" + self.logEXTENSION

	def getPtr(self, capture, last = True):
		'''
		if last == True: then get last pointer in folder
		if last == False: then get next pointer
		'''
		dir = ""
		if capture == "LEAF":
			dir = self.LEAF_DIR
		elif capture == "PH":
			dir = self.PH_DIR
		elif capture == "MOISTURE":
			dir = self.MOISTURE_DIR
		elif capture == "COLOUR":
			dir = self.COLOUR_DIR
		elif capture == "NN_DATA":
			dir = self.NN_DATA_DIR
		elif capture == "PH_INDICATOR":
			dir = self.PH_INDICATOR_DIR
		elif capture == "MOISTURE_INDICATOR_DIR":
			dir = self.MOISTURE_INDICATOR_DIR
			
		fileList = list()
		for item in os.listdir(dir):
			if item.split('.')[-1] == self.EXTENSION.split(".")[-1]:
				fileList.append(int(item.split('.')[0].split('_')[0]))
		fileList = sorted(fileList)
		
		pointer = 0
		if (len(fileList)>0):
			pointer = (int)(fileList[-1])
		if last:
			return pointer
		return pointer+1

	def refresh(self, capture):
		'''
		sets to next pointer by default
		'''
		if capture == "LEAF":
			self.LEAF_PTR = self.getPtr(capture, False)
		elif capture == "PH":
			self.PH_PTR = self.getPtr(capture, False)
		elif capture == "MOISTURE":
			self.MOISTURE_PTR = self.getPtr(capture, False)
		elif capture == "COLOUR":
			self.COLOUR_PTR = self.getPtr(capture, False)
		elif capture == "NN_DATA":
			self.NN_DATA_PTR = self.getPtr(capture, False)
		elif capture == "MOISTURE_INDICATOR":
			self.MOISTURE_INDICATOR_PTR = self.getPtr(capture, False)
		elif capture == "PH_INDICATOR":
			self.PH_INDICATOR_PTR = self.getPtr(capture, False)

	def imageFilename(self, capture ,colour):
		'''
		colour = "RGB"/"NGB"/"NDVI"
		!WARNING --> defence mechanism not yet implemented
		'''
		first = ""
		mid = ""
		if capture == "LEAF":
			first = self.LEAF_PREFIX
			mid = str(self.LEAF_PTR)
		elif capture == "PH":
			first = self.PH_PREFIX
			mid = str(self.PH_PTR)
		elif capture == "MOISTURE":
			first = self.MOISTURE_PREFIX
			mid = str(self.MOISTURE_PTR)
		elif capture == "COLOUR":
			first = self.COLOUR_PREFIX
			mid = str(self.COLOUR_PTR)
		elif capture == "NN_DATA":
			first = self.NN_DATA_PREFIX
			mid = str(self.NN_DATA_PTR)
		elif capture == "PH_INDICATOR":
			first = self.PH_INDICATOR_PREFIX
			mid = str(self.PH_INDICATOR_PTR)
		elif capture == "MOISTURE_INDICATOR":
			first = self.MOISTURE_INDICATOR_PREFIX
			mid = str(self.MOISTURE_INDICATOR_PTR)
		
		return first + mid +"_"+ colour + self.EXTENSION

	def getPath2DATA(self):
		dir=str(os.getcwd()).split('\\')[:-1]
		Path2DATA = ""
		for node in dir:
			Path2DATA += node + "\\"
		Path2DATA += "DATA"
		return Path2DATA

	def getPath2Scripts(self):
		dir=str(os.getcwd()).split('\\')[:-1]
		Path2Scripts = ''
		for node in dir:
			Path2Scripts += node + '\\'
		Path2Scripts += 'Camera_App'
		return Path2Scripts

	def getDirectory(self, mode):
		if mode == "PH":
			return self.PH_DIR
		elif mode == "MOISTURE":
			return self.MOISTURE_DIR
		elif mode == "COLOUR":
			return self.COLOUR_DIR
		elif mode == "LEAF":
			return self.LEAF_DIR
		elif mode == "PH_INDICATOR":
			return self.PH_INDICATOR_DIR
		elif mode == "MOISTURE_INDICATOR":
			return self.MOISTURE_INDICATOR_DIR
		elif mode == "NN_DATA":
			return self.NN_DATA_DIR
		
	def purgeAll(self):
		try:
			print("Purging LEAF_DIR :" + LEAF_DIR)
			for item in os.listdir(self.LEAF_DIR):
				os.remove(item)
			os.removedirs(self.LEAF_DIR)
			print("Purge successful")
		except:
			print("Error occoured!")
		
		try:
			print("Purging PH_DIR :" + PH_DIR)
			for item in os.listdir(self.PH_DIR):
				os.remove(item)
			os.removedirs(self.PH_DIR)
			print("Purge successful")
		except:
			print("Error occoured!")
		
		try:
			print("Purging MOISTURE_DIR :" + MOISTURE_DIR)
			for item in os.listdir(self.MOISTURE_DIR):
				os.remove(item)
			os.removedirs(self.MOISTURE_DIR)
			print("Purge successful")
		except:
			print("Error occoured!")
			
		try:
			print("Purging COLOUR_DIR :" + XOLOUR_DIR)
			for item in os.listdir(self.COLOUR_DIR):
				os.remove(item)
			os.removedirs(self.COLOUR_DIR)
			print("Purge successful")
		except:
			print("Error occoured!")
		
		try:
			print("Purging NN_DATA_DIR :" + NN_DATA_DIR)
			for item in os.listdir(self.NN_DATA_DIR):
				os.remove(item)
			os.removedirs(self.NN_DATA_DIR)
			print("Purge successful")
		except:
			print("Error occoured!")

		try:
			print("Purging PH_INDICATOR_DIR :" + PH_INDICATOR_DIR)
			for item in os.listdir(self.PH_INDICATOR_DIR):
				os.remove(item)
			os.removedirs(self.PH_INDICATOR_DIR)
			print("Purge successful")
		except:
			print("Error occoured!")

		try:
			print("Purging MOISTURE_INDICATOR_DIR :" + MOISTURE_INDICATOR_DIR)
			for item in os.listdir(self.MOISTURE_INDICATOR_DIR):
				os.remove(item)
			os.removedirs(self.MOISTURE_INDICATOR_DIR)
			print("Purge successful")
		except:
			print("Error occoured!")
						
			
class database():
	def __init__(self, application):
		self.session = configuration()
		self.dataFile = ""
		self.outputFile = ""
		self.logFile = ""
		self.dataDelimiter = ','
		self.inputFeatures = 0
		if application == "METER":
			self.dataFile = self.session.MeterData
			self.outputFile = self.session.MeterCoefficients
			self.logFile = self.session.MeterLog
			self.inputFeatures = 1
		elif application == "GYPSUM_H":
			self.dataFile = self.session.GypsumData_H
			self.outputFile = self.session.GypsumCoefficients_H
			self.logFile = self.session.GypsumLog
			self.inputFeatures = 1
		elif application == "GYPSUM_M":
			self.dataFile = self.session.GypsumData_M
			self.outputFile = self.session.GypsumCoefficients_M
			self.logFile = self.session.GypsumLog
			self.inputFeatures = 1
		elif application == "GYPSUM_L":
			self.dataFile = self.session.GypsumData_L
			self.outputFile = self.session.GypsumCoefficients_L
			self.logFile = self.session.GypsumLog
			self.inputFeatures = 1
		elif application == "LEAF":
			self.dataFile = self.session.LeafData
			self.outputFile = self.session.LeafCoefficients
			self.logFile = self.session.LeafLog
		elif application == "PH":
			self.dataFile = self.session.PhData
			self.outputFile = self.session.PhCoefficients
			self.logFile = self.session.PhLog
		elif application == "MOISTURE":
			self.dataFile = self.session.MoistureData
			self.outputFile = self.session.MoistureCoefficients
			self.logFile = self.session.MoistureLog
		elif application == "COLOUR":
			self.dataFile = self.session.ColourData
			self.outputFile = self.session.ColourCoefficients
			self.logFile = self.session.ColourLog
		elif application == "PH_INDICATOR":
			self.dataFile = self.session.PhIndicatorData
			self.outputFile = self.session.PhIndicatorCoefficients
			self.logFile = self.session.PhIndicatorLog
		elif application == "MOISTURE_INDICATOR":
			self.dataFile = self.session.MoistureIndicatorData
			self.outputFile = self.session.MoistureIndicatorCoefficients
			self.logFile = self.session.MoistureIndicatorLog