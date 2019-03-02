import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('/home/rgukt/Desktop/criotam/friut/arti/6AFMAN-AC-2.jpg',0)      ## reading the images
img1 = cv2.imread('/home/rgukt/Desktop/criotam/friut/arti/6AFMAN-AC-2.jpg')


ret,thresh = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)               ## applying threshod

plt.imshow(thresh,cmap='Greys_r')
plt.show()
