import cv2
from matplotlib import pyplot as plt
import numpy as np
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import imutils


path = "/home/rgukt/Desktop/criotam/friut/shape/WhatsApp Image 2019-03-23 at 2.40.01 PM.jpeg"
original = cv2.imread(path)

gray = cv2.imread(path,0)

pixels_per_inch = None

 
def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)



h,w = gray.shape

thresh,bin_image = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
kernel = np.ones((5,5))

bin_image = bin_image-255
erotion = cv2.erode(bin_image,kernel)

dilation = cv2.dilate(erotion,kernel)



_,cnts,_= cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

#cnts = imutils.grab_contours(cnts)

(cnts, _) = contours.sort_contours(cnts)

width = 2.2    ## in inches

print(len(cnts))
for c in cnts:
	if cv2.contourArea(c)<20000:
		continue

	box = cv2.minAreaRect(c)       ## will get the center,width,height,angle of rotations
	box = cv2.boxPoints(box)     ## will get the corners
	box = np.array(box, dtype="int")
	box = perspective.order_points(box)


	cv2.drawContours(original,[box.astype("int")],-1,(0,255,0),10)
	for (x, y) in box:
		cv2.circle(original, (int(x), int(y)), 5, (0, 0, 255), -1)         ## draw the corners
	(topleft, topright, bottomright, bottomleft) = box                ## Top right ,top right , bottom right , bottom left
	
	(topleft_toprightX, topleft_toprightY) = midpoint(topleft, topright)            ## midpoint of top row of rectangele
	(bottomleft_bottomrightX, bottomleft_bottomrightY) = midpoint(bottomleft, bottomright)              ## midpoint of bottom row of rectangle

	(topleft_bottomleftX, topleft_bottomleftY) = midpoint(topleft, bottomleft)          ##  mid point of left column of rectangle
	(topright_bottomrightX, topright_bottomrightY) = midpoint(topright, bottomright)          ##  mid point of right column of rectangle

	cv2.line(original, (int(topleft_toprightX), int(topleft_toprightY)), (int(bottomleft_bottomrightX), int(bottomleft_bottomrightY)),      ## line ffrom top mid to bottom mid
		(255, 0, 255), 2)
	cv2.line(original, (int(topleft_bottomleftX), int(topleft_bottomleftY)), (int(topright_bottomrightX), int(topright_bottomrightY)),       ## line from left mid to right mid
		(255, 0, 255), 2)
	dA = dist.euclidean((topleft_toprightX, topleft_toprightY), (bottomleft_bottomrightX, bottomleft_bottomrightY))         ## height of the rectangle
	dB = dist.euclidean((topleft_bottomleftX, topleft_bottomleftY), (topright_bottomrightX, topright_bottomrightY))         ## width of the rectangle

	if pixels_per_inch is None:
		pixels_per_inch = dB / width               ## reference size

	dimA = dA / pixels_per_inch             ## height
	dimB = dB / pixels_per_inch            ## width

	cv2.putText(original, "{:.1f}in".format(dimA),
		(int(topleft_toprightX - 15), int(topleft_toprightY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
		0.65, (255, 255, 255), 3)
	cv2.putText(original, "{:.1f}in".format(dimB),
		(int(topright_bottomrightX ), int(topright_bottomrightY)), cv2.FONT_HERSHEY_SIMPLEX,
		0.65, (255, 0, 0), 3)

plt.imshow(original)
plt.show()




