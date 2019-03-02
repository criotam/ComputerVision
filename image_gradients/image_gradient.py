import numpy as np
import cv2
import math
from time import sleep
from matplotlib import pyplot as plt

img = cv2.imread("/home/rgukt/Desktop/criotam/friut/natu/mango.jpg",0)

kernel = np.ones((10,10),np.float32)/100
img = cv2.filter2D(img,-1,kernel)
print(kernel)
plt.imshow(img)
plt.show()
h,w = img.shape
print(h*w)
sleep(1)

grad_x = np.array([-1,0,1])
grad_y = np.array([[-1],
					[0],
					[1]])

new_image = np.zeros((h,w),dtype ='int64')
"""
t = grad_x.size


new_image = np.zeros((h+(t-1),w+(t-1)))

new_image[np.uint16((t-1)/2.0):h+np.uint16((t-1)/2.0),
			np.uint16((t-1)/2.0):w+np.uint16((t-1)/2.0)] = img

result = new_image.shape


for i in range(1,result[0]):
	for j in range(1,result[1]):
		cur_reg = new_image[i-np.uint16((t-1)/2):i+(np.uint16((t-1)/2)+1),j-np.uint16((t-1)/2):j+(np.uint16((t-1)/2)+1)]
		cur_res = cur_reg*grad_x
		print(cur_reg,cur_res)
"""		
"""
ts = grad_x.size		
import numpy as numpy
for r in numpy.uint16(numpy.arange((ts-1)/2.0, img.shape[0]+(ts-1)/2.0)):
    for c in numpy.uint16(numpy.arange((ts-1)/2.0, 
                          img.shape[1]+(ts-1)/2.0)):
        curr_region = new_image[r-numpy.uint16((ts-1)/2.0):r+numpy.uint16((ts-1)/2.0)+1, 
                              c-numpy.uint16((ts-1)/2.0):c+numpy.uint16((ts-1)/2.0)+1]
        curr_result = curr_region * grad_x
        score = numpy.sum(curr_result)
        print(curr_region,curr_result,score,grad_x)
        sleep(1)
"""
c=0
for i in range(3,h-3):
	for j in range(3,w-3):
		c+=1
		x = img[i][j+3]-img[i][j-3]
		y = img[i+3][j]-img[i-3][j]
		z = x**2+y**2

		val = math.sqrt(z)
		
		new_image[i][j] = np.round(val)/255
	print(c)

cv2.imwrite("natural_mango.jpg",new_image)
plt.imshow(new_image,cmap='Greys_r')
plt.hist(new_image,bins=256)
plt.show()
