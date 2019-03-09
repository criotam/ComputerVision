import cv2
from matplotlib import pyplot as plt
import numpy as np
from time import sleep


img = cv2.imread('/home/rgukt/Desktop/criotam/friut/natural_mango.png',0)

noise  = cv2.medianBlur(img,5)

sub = cv2.subtract(img,noise)

plt.subplot(2,2,1)
plt.imshow(noise,cmap='Greys_r')
plt.subplot(2,2,2)
plt.imshow(img,cmap='Greys_r')
plt.subplot(2,2,3)
plt.imshow(sub,cmap='Greys_r')
plt.show()

