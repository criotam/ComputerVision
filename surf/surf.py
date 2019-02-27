import numpy as np
import cv2

from matplotlib import pyplot as plt
# Load the image
img = cv2.imread('//home/rgukt/Desktop/criotam/art_mango.jpg')


# Convert it to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                 ## gray converting

# Detect the SURF key points
surf = cv2.xfeatures2d.SURF_create(hessianThreshold=500, upright=True, extended=True)             ## definig the SURF 
keyPoints, descriptors = surf.detectAndCompute(gray, None)                    ## detecting keypoints
print(len(descriptors))
# Paint the key points over the original image
result = cv2.drawKeypoints(img, keyPoints,img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)    ## draw keypoints 
 
b,g,r = cv2.split(result)
img = cv2.merge((r,g,b))
cv2.imwrite("surf_natu.jpg",img)
plt.imshow(img)
plt.show()