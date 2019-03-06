import cv2
import numpy as np
from matplotlib import pyplot as plt
from time import sleep
import operator

img1 = cv2.imread('/home/rgukt/Desktop/criotam/friut/arti/arti1.jpg')
img = cv2.imread('/home/rgukt/Desktop/criotam/friut/arti/arti1.jpg',0)
temp = cv2.imread('/home/rgukt/Desktop/criotam/friut/arti/41eUrCvxq5L._SX450_.jpg',0)
temp = cv2.resize(temp,(200,200))

temp = cv2.Canny(temp,50,200)
b,g,r = cv2.split(img1)
img1 = cv2.merge((r,g,b))

ih,iw = img.shape
th,tw = temp.shape
#re, img = cv2.threshold(img,0,256,cv2.THRESH_OTSU)
#re,temp = cv2.threshold(temp,0,256,cv2.THRESH_OTSU)

val = []
loc = []
va=[]
for i in np.linspace(0.002,2,100):
	resiz = cv2.resize(img,(int(i*iw),ih))             ## this is for scale invariant
	h,w = resiz.shape
	
	if h>th and w>tw:

		canny = cv2.Canny(resiz,100,200)                   ## canny edge detection
		result = cv2.matchTemplate(canny, temp, cv2.TM_CCOEFF)          ## template matching 
		(_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)              
		val.append(maxVal)
		loc.append(maxLoc)

index, value = max(enumerate(val), key=operator.itemgetter(1))           ## max value and its index 



cv2.rectangle(img1,(loc[index][0],loc[index][1]),(loc[index][0]+th,loc[index][1]+tw),(0,127,127),5)      ## drawing rectangular box
plt.imshow(img1,cmap='Greys_r')
plt.show()
		
