import cv2
import numpy as np
from matplotlib import pyplot as plt
from time import sleep

img = cv2.imread('/home/rgukt/Desktop/criotam/friut/arti/da.jpg')          ## read the image

b,g,r = cv2.split(img)        ## split the image
img = cv2.merge((r,g,b))     ## mereg the  bgr to rgb

#img = img/255                  ## scale image to range between 0 to 1



#plt.imshow(img,cmap="Greys_r")
#plt.show()



lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB) 
for i ,j in enumerate(['__L__','__A__','__B__']):

	#plt.imshow(lab[:,:,2],cmap="Greys_r")
	cv2.imwrite('{type}artificial3{ind}.jpg'.format(ind = i ,type = j),lab[:,:,i])
plt.show()
