import numpy as np
import matplotlib.pyplot as pyplot
from coreLib.SessionManager import database
import coreLib.grabCut as grabCut
import coreLib.imFormat as imFormat
import coreLib.imProcess as imProcess
from scipy import spatial

class similarityRanking():
	def __init__(self, application, dimension=1, supressGraph=False):
		self.database = database(application)
		print("Loading dataset ...")
		self.data = np.loadtxt(self.database.dataFile, delimiter = self.database.dataDelimiter)
		print("Initializing parameters ...")
		self.X = None
		self.Y = None
		self.m = None
		self.dimensions = dimension
		self.similarityMeasure = None
		self.supressGraph = supressGraph
		try:
			self.loadParameters()
		except:
			print("Dimensions mismatched, don't worry its all under control ;)")
	
	def loadParameters(self):
		self.X = self.data[:, 0:self.dimensions]
		self.Y = self.data[:, self.dimensions]
		self.m = self.Y.size
		self.similarityMeasure = list()
		print("Data structured and parameters initialized !")
		if not self.supressGraph:
			print("Plotting dataset...")
			#displaying as a raster
			pyplot.imshow(self.X, interpolation='nearest')
			pyplot.show()

	def normalize(self, numberList, sum):
		print numberList
		print('Normalizing the similarity vecotrs ...')
		temp = [float(i)/sum for i in numberList]
		maxVal = max(temp)
		norm = [float(i)/maxVal for i in temp]
		print('Done.')
		print norm
		return norm
		
	def getSimilarity(self, vector1, vector2):
		return (1 - spatial.distance.cosine(vector1, vector2))

	def getTargetVector(self, imagePath, imageMode, LAB):
		print("Loading coefecients ...")
		coeflist = np.loadtxt(self.database.outputFile, delimiter = self.database.dataDelimiter)
		deltaVector = list()
		self.dimensions = int(coeflist.shape[0])
		self.loadParameters()

		print("Extract for target image ...")
		if imageMode == "RGB":
			image = grabCut.getGrabCutImage(imFormat.imread(imagePath))
		elif imageMode == "HSV":
			image = grabCut.getGrabCutImage(imFormat.rgb2hsv(imFormat.imread(imagePath)))
		elif imageMode == "NDVI":
			image = grabCut.getGrabCutImage(imFormat.NDVICalc(imFormat.imread(imagePath)))

		for coef in coeflist:
			print(coef)
			delta = imProcess.getDeltaHybrid(imProcess.sampleImage(image, LAB=LAB), b1=coef[0], b2=coef[1], b3=coef[2])
			deltaVector.append(delta)
		deltaVector = np.array(deltaVector)
		return deltaVector
	
	def checkSimilarity(self, similarity, value):
		factor = (float(value-1))/value
		if similarity > value : 
			return True
		return False

	def predict(self, targetVector):
		#generate similarity ranking list
		sum = 0.0
		for item in self.X:
			similarity = self.getSimilarity(targetVector, item)
			sum += similarity
			self.similarityMeasure.append(similarity)
		self.similarityMeasure = self.normalize(self.similarityMeasure, sum)
		#now get vector corresponding to highest value
		max_val = max(self.similarityMeasure)
		index = self.similarityMeasure.index(max_val)
		nearestVector = self.X[index]
		print('calculating similarity index ...')
		#now get similarity of targetVector from this vector
		similarity = self.getSimilarity(targetVector, nearestVector)
		#validate authenticity by limiting curve
		if self.checkSimilarity(similarity, self.Y[index]):
			print("similarity estimate inside optimum range")
		#multiply this similarity index with actual value pertaining to this vector
		targetOutput = similarity*(float(self.Y[index]))
		print(targetOutput)
		return targetOutput
