import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("/home/rgukt/Desktop/criotam/friut/art_mango.jpg",0)
img1 = cv2.imread("/home/rgukt/Desktop/criotam/friut/arti/da.jpg",0)

img2 = cv2.imread("/home/rgukt/Desktop/criotam/friut/natu/4568_mango.jpg",0)
img3 = cv2.imread("/home/rgukt/Desktop/criotam/friut/natu/mango.jpg",0)

u = np.mean(img)
print(u)


img = np.asarray(img)
img = img.flatten()

img1 = np.asarray(img1)
img1 = img1.flatten()

img2 = np.asarray(img2)
img2 = img2.flatten()

img3 = np.asarray(img3)
img3 = img3.flatten()

plt.subplot(2,2,1)
plt.hist(img,bins=100,color = 'black')
plt.subplot(2,2,2)
plt.hist(img1,bins=100,color ='black')

plt.subplot(2,2,3)
plt.hist(img2,bins=100,color = 'black')
plt.subplot(2,2,4)
plt.hist(img3,bins=100,color ='black')

plt.show()

