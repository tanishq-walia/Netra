import math
import cv2
import imFormat

def getMeanComponents(img_array):
	x,y,z = cv2.split(img_array)
	return float(x.mean()), float(y.mean()), float(z.mean())

def getDelta(A1, A2, A3, B1, B2, B3):
	deltaE = math.sqrt(((A1-B1)**2)+((A2-B2)**2)+((A3-B3)**2))
	return deltaE

def getDeltaFromImage(image1, image2):
	A1 , A2 , A3 = getMeanComponents(image1)
	B1 , B2 , B3 = getMeanComponents(image2)
	return getDelta(A1, A2, A3, B1, B2, B3)

def getDeltaHybrid(image1, b1, b2, b3):
	A1 , A2 , A3 = getMeanComponents(image1)
	B1 , B2 , B3 = b1 , b2 , b3
	return getDelta(A1, A2, A3, B1, B2, B3)

def sampleImage(rgb_image, kernelStd=1, LAB=True):
	# Resizing image
	resized_image = cv2.resize(rgb_image, (200, 200))
	# Averaging the pixel data
	kernelRadius = int(5 * kernelStd);
	kernelLength = (2 * kernelRadius ) + 1;
	blur=cv2.GaussianBlur(resized_image,(kernelLength,kernelLength),kernelRadius)
	# sample image
	sample_img = blur[15:170, 15:170] 
	# Converting to LAB
	output = sample_img
	if LAB:
		output = imFormat.rgb2lab(sample_img)
	return output
