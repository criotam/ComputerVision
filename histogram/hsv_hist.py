import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/rgukt/Desktop/criotam/friut/arti/arti1.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

arr = np.asarray(hsv)

img1 = cv2.imread('/home/rgukt/Desktop/criotam/friut/natu/2.jpg')
hsv1 = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)

arr11 = np.asarray(hsv1)

#### for artificail
arr1 = arr[:,:,0].flatten()
arr1=(arr1.astype(float))/255.0
plt.subplot(2,3,1)
plt.hist(arr1*360,bins=360,range=(0.0,360.0),histtype='stepfilled', color='r', label='Hue')
plt.subplot(2,3,2)

arr2 = arr[:,:,1].flatten()
arr2=(arr2.astype(float))/255.0

plt.hist(arr2,bins=360,range=(0.0,1.0),histtype='stepfilled', color='b', label='saturation')

plt.subplot(2,3,3)

arr3 = arr[:,:,2].flatten()
arr3=(arr3.astype(float))/255.0

plt.hist(arr3,bins=360,range=(0.0,1.0),histtype='stepfilled', color='g', label='value')


## for natural one

arr1 = arr11[:,:,0].flatten()
arr1=(arr1.astype(float))/255.0
plt.subplot(2,3,4)
plt.hist(arr1*360,bins=360,range=(0.0,360.0),histtype='stepfilled', color='r', label='Hue')
plt.subplot(2,3,5)

arr2 = arr11[:,:,1].flatten()
arr2=(arr2.astype(float))/255.0

plt.hist(arr2,bins=360,range=(0.0,1.0),histtype='stepfilled', color='b', label='saturation')

plt.subplot(2,3,6)

arr3 = arr11[:,:,2].flatten()
arr3=(arr3.astype(float))/255.0

plt.hist(arr3,bins=360,range=(0.0,1.0),histtype='stepfilled', color='g', label='value')

plt.show()