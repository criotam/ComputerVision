import cv2
import numpy as np
from matplotlib import pyplot as plt
from time import sleep

img = cv2.imread('/home/rgukt/Desktop/criotam/friut/natural_mango.png')          ## read the image

b,g,r = cv2.split(img)        ## split the image
img = cv2.merge((r,g,b))     ## mereg the  bgr to rgb

img = img/255                  ## scale image to range between 0 to 1

print(img[100,100,:	])

plt.imshow(img,cmap="Greys_r")
plt.show()

h,w,c = img.shape
img = img.astype('float32')               ## convert this image to float
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)     ## rgb to lab
lab = np.asarray(lab)

print (f'{lab[:,:,0].min()}, {lab[:,:,0].max()}')
            
cv2.imwrite("B_natural.jpg",lab[:,:,1])

print(lab[100,100,:])

print(np.mean(lab[:,:,0]))

print(np.mean(lab[:,:,1]))             ## mean values
print(np.mean(lab[:,:,2]))

