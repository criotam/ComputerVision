import cv2
from matplotlib import pyplot as plt
import numpy as np
import math
from time import sleep

#path = "/home/rgukt/Desktop/criotam/friut/dataset/new.jpg"


path= "/home/rgukt/Desktop/criotam/friut/shape/shape/4.jpg"
im = cv2.imread(path)
img = cv2.imread(path,0)

#img = cv2.GaussianBlur(img,(9,9),10)


h,w,c = im.shape
print(im.shape)
thresh,bin = cv2.threshold(img,0,255,cv2.THRESH_OTSU)

bin = bin-255
kernel = np.ones((5,5))

#opening = cv2.erode(bin,kernel,iterations=3)

im2,cnts,her = cv2.findContours(bin,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

#cnts = sorted(cnts, key = cv2.contourArea, reverse = False)

def mid_point(x,y):

	cx = ((x[0]+y[0])*0.5)
	cy = ((x[1]+y[1])*0.5)
max_area = 0
max_index = 0
cn_area = []

for i in range(0,len(cnts)):
	area=cv2.contourArea(cnts[i])
	cn_area.append(area)            ### contour area
	#print(area,i)
	if area > max_area:
		max_area=area                  ## finding the large contour
		max_index = i



im1 = cv2.drawContours(im,cnts[max_index],-1,(0,255,0),7)

shape = []

M = cv2.moments(cnts[max_index])

cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])


max_distance = 0
max_dis_index = 0



for i in range(0,len(cnts[max_index])):
	
	dist = ((cnts[max_index][i][0][0]-cX)**2+(cnts[max_index][i][0][1]-cY)**2)
	shape.append(dist)
	if dist > max_distance :
		max_distance=dist
		max_dis_index=i


new_shape = []

cv2.circle(im,(cX,cY),3,(0,0,0),3)
print(max_distance)
print(max_dis_index,len(cnts[max_index]))
print(abs(max_dis_index-len(cnts[max_index])))

for i in range(max_dis_index,len(cnts[max_index])):
	new_shape.append(shape[i])

print(len(new_shape))

for i in range(0,max_dis_index-1):
	new_shape.append(shape[i])

print(len(new_shape))

plt.subplot(2,1,1)
plt.plot(new_shape)
plt.subplot(2,1,2)	
plt.imshow(im1,cmap='Greys_r')
plt.show()