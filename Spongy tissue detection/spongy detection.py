import cv2
import numpy as np
import matplotlib.pyplot as plt



spongy = cv2.imread('spongymango_gray.jpg')


##converting to grayscale
spongy_gray = cv2.cvtColor(spongy,cv2.COLOR_BGR2GRAY)


##sharpening
kernel = np.array([[-1,-1,-1],
                  [-1,9,-1],
                  [-1,-1,-1]])
sharp = cv2.filter2D(spongy_gray,-1,kernel)

##Gaussianblur
g_blur = cv2.GaussianBlur(sharp,(9,9),0)

##medianblur
m_blur = cv2.medianBlur(g_blur,5)

##averaging
avg = cv2.blur(m_blur,(3,3))

##adaptive thresholding
thresh = cv2.adaptiveThreshold(avg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,17,8)


#external contour
_,cntr,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

bg = np.zeros(spongy.shape,np.uint8)

for i,cntr in enumerate(cntr):
    if hierarchy[0][i][3] == -1:
        epsilon = 0.0001*cv2.arcLength(cntr,True)
        approx = cv2.approxPolyDP(cntr,epsilon,True)
    
        img = cv2.drawContours(bg,[approx],0,(255,0,0),1)
    
_,cntr,hier = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
bg = np.zeros(spongy.shape,np.uint8)

for i,cnt in enumerate(cntr):
    if hier[0][i][3] == -1:
    
        
    
        img = cv2.drawContours(bg,[approx],0,(255,255,255),-1)
    
plt.imshow(img,cmap='gray')
img = img[:,:,0]
res = cv2.subtract(thresh,img)
plt.imshow(res,cmap='gray')
plt.show()



#getting total fruit size
_,thresh = cv2.threshold(g_blur,0,255,cv2.THRESH_TRIANGLE)
plt.imshow(thresh,cmap='gray')
plt.title('Total fruit size')
plt.show()


total = cv2.countNonZero(thresh)
spongy = cv2.countNonZero(res)

percentage = spongy/total*100
plt.imshow(res,cmap='gray')
plt.title(f"Lightly infested : {percentage:.3}%")
plt.show()