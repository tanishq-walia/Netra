import numpy as np
import pylab as pl
from coreLib.SessionManager import database

class linearRegression():
	def __init__(self, application, supressGraph=False, XLABEL="input values", YLABEL="target values", TITLE="application",  alpha=0.001, iterations=50000):
		self.database = database(application)
		print("Loading dataset ...")
		self.data = np.loadtxt(self.database.dataFile, delimiter = self.database.dataDelimiter)
		print("Initializing parameters ...")
		self.X = self.data[:, 0]
		#self.X = np.multiply(self.X , 10000)
		self.y = self.data[:, 1]
		#self.y = np.multiply(self.y , 100)
		#number of training samples
		self.m = self.y.size
		#Add a column of ones to X (interception data)
		self.it = np.ones(shape=(self.m, 2))
		self.it[:, 1] = self.X
		#Initialize theta parameters
		self.theta = np.zeros(shape=(2, 1))
		#Some gradient descent settings
		self.iterations = iterations
		self.alpha = alpha
		self.supressGraph = supressGraph
		print("Data structured and parameters initialized !")
		if not self.supressGraph:
			print("Plotting dataset...")
			self.plotData(self.X, self.y, TITLE, XLABEL, YLABEL)

	def plotData(self, X, Y, TITLE, XLABEL, YLABEL):
		pl.figure()
		pl.scatter(X, Y, marker='o', c='b')
		pl.title(TITLE)
		pl.xlabel(XLABEL)
		pl.ylabel(YLABEL)
		pl.show()
					
	#Evaluate the linear regression 
	def compute_cost(self, X, y, theta):
		'''
		Comput cost for linear regression
		'''
		m = y.size
		predictions = X.dot(theta).flatten()
		sqErrors = (predictions - y) ** 2
		J = (1.0 / (2 * m)) * sqErrors.sum()
		return J

	def gradient_descent(self, X, y, theta, alpha, num_iters):
		'''
		Performs gradient descent to learn theta
		by taking num_items gradient steps with learning
		rate alpha
		'''
		m = y.size
		J_history = np.zeros(shape=(num_iters, 1))
		for i in range(num_iters):
			predictions = X.dot(theta).flatten()
			errors_x1 = (predictions - y) * X[:, 0]
			errors_x2 = (predictions - y) * X[:, 1]
			theta[0][0] = theta[0][0] - alpha * (1.0 / m) * errors_x1.sum()
			theta[1][0] = theta[1][0] - alpha * (1.0 / m) * errors_x2.sum()
			J_history[i, 0] = self.compute_cost(X, y, theta)
		return theta, J_history
	
	def predict(self, targetInput, fromFile=True):
		theta = self.theta
		if fromFile:
			theta = np.loadtxt(self.database.outputFile, delimiter = self.database.dataDelimiter)
		#Predict value for target input
		print "coefficient : ", theta
		targetOutput = np.array([1, targetInput]).dot(theta).flatten()[0]
		if not self.supressGraph:
			#Plot the results
			result = self.it.dot(theta).flatten()
			pl.plot(self.data[:, 0], result)
			pl.show()
		print "Predicted value : ", targetOutput
		return targetOutput

	def saveCoefficients(self):
		print("Saving the coefficients to output file ...")
		np.savetxt(self.database.outputFile, self.theta, delimiter = self.database.dataDelimiter)
		print("Finished!")

	def train(self, testVal = 3.5, visualize = False):
		#compute and display initial cost
		print "compute cost : ", self.compute_cost(self.it, self.y, self.theta)
		self.theta, J_history = self.gradient_descent(self.it, self.y, self.theta, self.alpha, self.iterations)
		self.saveCoefficients()
		ret = self.predict(testVal, self.supressGraph)

		def contour():
			#Grid over which we will calculate J
			theta0_vals = np.linspace(-10, 10, 100)
			theta1_vals = np.linspace(-1, 4, 100)
			#initialize J_vals to a matrix of 0's
			J_vals = np.zeros(shape=(theta0_vals.size, theta1_vals.size))
			#Fill out J_vals
			for t1, element in enumerate(theta0_vals):
				for t2, element2 in enumerate(theta1_vals):
					thetaT = np.zeros(shape=(2, 1))
					thetaT[0][0] = element
					thetaT[1][0] = element2
					J_vals[t1, t2] = self.compute_cost(self.it, self.y, thetaT)
			#Contour plot
			J_vals = J_vals.T
			#Plot J_vals as 15 contours spaced logarithmically between 0.01 and 100
			pl.figure()
			pl.contour(theta0_vals, theta1_vals, J_vals, np.logspace(-2, 3, 20))
			pl.xlabel('theta_0')
			pl.ylabel('theta_1')
			pl.scatter(self.theta[0][0], self.theta[1][0])
			pl.show()

		if not visualize:
			contour()
		#return ret



