import cv2
import math
from time import time
import numpy as np

def getLineCordinates(imageFile):
	boxes = []
	def on_mouse(event, x, y, flags, params):
	    # global img
		t = time()
		if event == cv2.EVENT_LBUTTONDOWN:
			print 'Start Mouse Position: '+str(x)+', '+str(y)
			sbox = [x, y]
			boxes.append(sbox) 
		elif event == cv2.EVENT_LBUTTONUP:
			print 'End Mouse Position: '+str(x)+', '+str(y)
			ebox = [x, y]
			boxes.append(ebox)
			cv2.line(img,(boxes[0][0],boxes[0][-1]),(boxes[1][0],boxes[1][-1]),(0,0,0),2)
			cv2.imshow('Draw Reference Distance', img)
			print boxes	
	#img = cv2.imread(imageFile)
	img=imageFile
	cv2.namedWindow('Draw Reference Distance')
	cv2.setMouseCallback('Draw Reference Distance', on_mouse, 0)
	cv2.imshow('Draw Reference Distance', img)
	if cv2.waitKey(0) == 27:
		cv2.destroyAllWindows()       
	return boxes
	
def getPixelCount(imageFile):
	#im_gray = cv2.cvtColor(imageFile, cv2.COLOR_BGR2GRAY)
	#thresh = 1
	#im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
	im_bw = 255*(cv2.cvtColor(imageFile, cv2.COLOR_BGR2GRAY) > 5).astype('uint8')
	se1 = cv2.getStructuringElement(cv2.MORPH_RECT, (10,10))
	se2 = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
	mask = cv2.morphologyEx(im_bw, cv2.MORPH_CLOSE, se1)
	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, se2)
	mask = mask/255
	im_bw = mask * im_bw
	cv2.imshow('Leaf Area region ...',im_bw)
	if cv2.waitKey(0) == 27:
		cv2.destroyAllWindows()  
	pixelCount = cv2.countNonZero(im_bw)
	return pixelCount

def getArea(imageFile, length, units):
	pixelCount=getPixelCount(imageFile)
	print 'pixel count of extracted  region is : '+str(pixelCount)
	boxes = getLineCordinates(imageFile)
	print 'distance in Real World is : '+str(length)
	units = units+' squared'
	distanceInPixel = math.sqrt(((boxes[0][0]-boxes[1][0])**2)+((boxes[0][-1]-boxes[1][-1])**2))
	print 'distance in pixel is : '+str(distanceInPixel)
	distancePerPixel = length/distanceInPixel
	print 'distance per pixelis : '+str(distancePerPixel)
	# experimental coefficient
	pixelCountRatio = 1.447
	a=raw_input( ' are disconitnuities large enough?: (y/n) ' )
	bias=0
	if a == 'y':
		bias=5.6
	else:
		bias=-6.2
	realArea=((pixelCount/pixelCountRatio)*(distancePerPixel)/length)-bias
	#realArea=(pixelCount*(distancePerPixel)/length)/pixelCountRatio
	return realArea, units