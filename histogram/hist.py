import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/rgukt/Desktop/criotam/friut/art_mango.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)



img1 = cv2.imread('/home/rgukt/Desktop/criotam/friut/natural_mango.png')
hsv1 = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)



hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

hist1 = cv2.calcHist([hsv1],[0,1], None, [180, 256], [0, 180, 0, 256])

plt.subplot(2,2,1)
plt.plot(hist)
plt.subplot(2,2,2)
plt.plot(hist1)
plt.show()