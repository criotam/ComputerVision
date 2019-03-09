import cv2
from matplotlib import pyplot as plt
import numpy as np
from time import sleep


def noise(img):

	h,w = img.shape
	c=0
	print(h,w)
	for i in range(1,h-1):
		for j in range(1,w-1):
			#print(i,j)
			
			sum = (img[i-1,j-1]+img[i-1,j]+img[i-1,j+1]+img[i+1,j-1]+img[i+1,j]+img[i+1,j+1]+img[i,j-1]+img[i,j+1])
			mean=sum/8
			if img[i,j]>mean:
				c+=1
				
				

	signal = ((h*w)-c)
	print(signal,c)
	if signal and c !=0:
		return signal/c



img = cv2.imread('/home/rgukt/Desktop/criotam/friut/natu/mango.jpg',0)
before = noise(img)

row,col= img.shape
mean = 0
var = 10
sigma = var**1
gauss = np.random.normal(mean,sigma,(row,col))
gauss = gauss.reshape(row,col)
noisy = img + gauss

after = noise(noisy)

print("before adding noise is",before)
print('after adding noise is',after)

plt.subplot(2,2,1)
plt.title('Natural_normal_image')
plt.imshow(img,cmap='Greys_r')
plt.subplot(2,2,2)
plt.imshow(noisy,cmap='Greys_r')
plt.title('Natural_noisy_image')
plt.show()