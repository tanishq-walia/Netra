import numpy as np
from skimage import color
import scipy 
import cv2 

#-------------------------------------------
#----------------NDVI Function--------------
#-------------------------------------------
#NDVI Calculation
#Input: an RGB image frame from infrablue source (blue is blue, red is pretty much infrared)
#Output: an RGB frame with equivalent NDVI of the input frame
def NDVICalc(original):
    "This function performs the NDVI calculation and returns an RGB frame)"
    lowerLimit = 5 #this is to avoid divide by zero and other weird stuff when color is near black
    #First, make containers
    oldHeight,oldWidth = original[:,:,0].shape 
    ndviImage = np.zeros((oldHeight,oldWidth,3),np.uint8) #make a blank RGB image
    ndvi = np.zeros((oldHeight,oldWidth),np.int) #make a blank b/w image for storing NDVI value
    red = np.zeros((oldHeight,oldWidth),np.int) #make a blank array for red
    blue = np.zeros((oldHeight,oldWidth),np.int) #make a blank array for blue
    #Now get the specific channels. Remember: (B , G , R)
    red = (original[:,:,2]).astype('float')
    blue = (original[:,:,0]).astype('float')
    #Perform NDVI calculation
    summ = red+blue
    summ[summ<lowerLimit] = lowerLimit #do some saturation to prevent low intensity noise
    ndvi = (((red-blue)/(summ)+1)*127).astype('uint8')  #the index
    redSat = (ndvi-128)*2  #red channel
    bluSat = ((255-ndvi)-128)*2 #blue channel
    redSat[ndvi<128] = 0 #if the NDVI is negative, no red info
    bluSat[ndvi>=128] = 0 #if the NDVI is positive, no blue info
    #And finally output the image. Remember: (B , G , R)
    #Red Channel
    ndviImage[:,:,2] = redSat
    #Blue Channel
    ndviImage[:,:,0] = bluSat
    #Green Channel
    ndviImage[:,:,1] = 255-(bluSat+redSat)
    return ndviImage

#-------------------------------------------
#----------------DVI Function---------------
#-------------------------------------------
#DVI Calculation
#Input: an RGB image frame from infrablue source (blue is blue, red is pretty much infrared)
#Output: an RGB frame with equivalent DVI of the input frame
def DVICalc(original):
    "This function performs the DVI calculation and returns an RGB frame)"
    #First, make containers
    oldHeight,oldWidth = original[:,:,0].shape 
    dviImage = np.zeros((oldHeight,oldWidth,3),np.uint8) #make a blank RGB image
    dvi = np.zeros((oldHeight,oldWidth),np.int) #make a blank b/w image for storing DVI value
    red = np.zeros((oldHeight,oldWidth),np.int) #make a blank array for red
    blue = np.zeros((oldHeight,oldWidth),np.int) #make a blank array for blue
    #Now get the specific channels. Remember: (B , G , R)
    red = (original[:,:,2]).astype('float')
    blue = (original[:,:,0]).astype('float')
    #Perform DVI calculation
    dvi = (((red-blue)+255)/2).astype('uint8')  #the index
    redSat = (dvi-128)*2  #red channel
    bluSat = ((255-dvi)-128)*2 #blue channel
    redSat[dvi<128] = 0; #if the NDVI is negative, no red info
    bluSat[dvi>=128] = 0; #if the NDVI is positive, no blue info
    #And finally output the image. Remember: (B , G , R)
    #Red Channel
    dviImage[:,:,2] = redSat
    #Blue Channel
    dviImage[:,:,0] = bluSat
    #Green Channel
    dviImage[:,:,1] = 255-(bluSat+redSat)
    return dviImage
    

#-------------------------------------------
#----------LAB Averaging Function-----------
#-------------------------------------------
#LAB Averaging Calculation
#Input: an RGB image frame  as BGR
#Output: an RGB frame with equivalent LAB of the input frame with colour blurred in 250 by 250    
def LABAverage(bgr_img, k):
	# Convert it into rgb
	rgb_img = bgr2rgb(bgr_img)
	# Resizing image
	resized_image = cv2.resize(rgb_img, (250, 250)) 
	# Averaging the pixel data
	kernelStd=k
	kernelRadius = int(5 * kernelStd)
	kernelLength = (2 * kernelRadius ) + 1
	blur=cv2.GaussianBlur(resized_image,(kernelLength,kernelLength),kernelRadius)
	# sample image
	sample_img = blur[25:200, 25:200] 
	# Converting to LAB
	lab_img = rgb2lab(rgb_img)
	return lab_img
    
#-------------------------------------------
#----------------NIR Function--------------
#-------------------------------------------
#NIR Calculation
#Input: an RGB image frame from infrablue source (blue is blue, red is pretty much infrared)
#Output: an NIR frame from the input frame
def NIRCalc(original):
    "This function performs the NIR calculation and returns an NIR frame"
    #First, make containers
    oldHeight,oldWidth = original[:,:,0].shape 
    red = np.zeros((oldHeight,oldWidth),np.int) #make a blank array for nir
    #Now get the specific channels. Remember: (B , G , R)
    nir = (original[:,:,2]).astype('float')
    return nir

#-------------------------------------------
#--------------Helper Function--------------
#-------------------------------------------
  
def mean_components(img_array):
	x,y,z = cv2.split(img_array)
	return x.mean(), y.mean(), z.mean()
    
def rgb2gray(rgbImage):
    return color.rgb2gray(rgbImage)
    
def bgr2gray(bgrImage):
    return cv2.cvtColor(bgrImage, cv2.COLOR_BGR2GRAY)
    
def rgb2lab(rgbImage):
    return color.rgb2lab(rgbImage)
    
def lab2rgb(labImage):
    return color.lab2rgb(labImage)
    
def bgr2rgb(bgrImage):
    # Loading b g r components
	b,g,r = cv2.split(bgrImage)
	# Converting to RGB
	return cv2.merge([r,g,b])

def rgb2bgr(rgbImage):
    # Loading r g b components
	r, g, b = cv2.split(rgbImage)
	# Converting to BGR
	return cv2.merge([b, g, r])
    
def bgr2hsv(bgrImage):
    return cv2.cvtColor(bgrImage, cv2.COLOR_BGR2HSV)

def smallestBoundingRectangularSegment(segImage):
	gray=bgr2gray(segImage)
	_, contours, hierarchy = cv2.findContours(gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	# Find the index of the largest contour
	areas = [cv2.contourArea(c) for c in contours]
	max_index = np.argmax(areas)
	cnt=contours[max_index]
	x,y,w,h = cv2.boundingRect(cnt)
	#cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
	outputImge = segImage[y:y+h, x:x+w]
	return outputImge
    
    
