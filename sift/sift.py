import numpy as np
import cv2
from matplotlib import pyplot as plt
# Load the image

img = cv2.imread('/home/rgukt/Desktop/criotam/natural_mango.png')
#img1 = cv2.imread("/home/rgukt/Desktop/criotam/art_mango.jpg")

# Convert it to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)            ## rgb to gray
#gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
(kps, descs) = sift.detectAndCompute(gray, None)                ## detecting keypoints
print(len(descs))
w,h = descs.shape
n=np.zeros((w,h)) 
x=np.zeros((w,h))
img1=cv2.drawKeypoints(img,kps,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)           ## draw keypoints
cv2.imwrite("sdf.jpg",img)

for i in range(w):
        for j in range(h):
                x[i,j] = n[i,j]
                
            
np.savetxt("foo.csv", x, delimiter=",")

b,g,r = cv2.split(img)
img = cv2.merge((r,g,b))
plt.imshow(img)
plt.show()
