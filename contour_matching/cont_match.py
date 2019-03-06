import cv2
import numpy as np
from matplotlib import pyplot as plt
from time import sleep
import operator
import collections

img1 = cv2.imread('/home/rgukt/Desktop/criotam/friut/natu/mango.jpg')

b,g,r = cv2.split(img1)
img1 = cv2.merge((r,g,b))
img = cv2.imread('/home/rgukt/Desktop/criotam/friut/natu/mango.jpg',0)
img = cv2.resize(img,(500,500))

ret,thresh = cv2.threshold(img,0,256,cv2.THRESH_OTSU)
im1,cnt1,her = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


temp = cv2.imread('/home/rgukt/Desktop/Mintm/Coffe_cup/2.jpg',0)
temp = cv2.resize(temp,(100,100))
re,thr = cv2.threshold(temp,0,256,cv2.THRESH_OTSU)


im2,cnt2,her1 = cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)



dist = []

c=0
corre = 100
cor_in = 0

max_area = 0
max_index = 0
dict = {}

for k in range(0,len(cnt2)):
	area = cv2.contourArea(cnt2[k])
	

	dict.update({area:k})


cd = sorted(dict.items(),key=operator.itemgetter(0),reverse=True)


inn = []
n=2

for i in range(0,n):
	
	inn.append(cd[0:n][i][1])
print(inn)
for i in inn:
	for j in range(0,len(cnt1)):
		
		ret = cv2.matchShapes(cnt1[j],cnt2[i],1,0.0)            ## comparing every contour of template image with Main image
		dist.append(ret)
		print(ret)
		c+=1
			
		if (ret)<(corre) and ret!=0 :
			print(i)	
			#print("enter",ret,corre)
			
			corre = ret
			cor_in = j

print(cor_in)			

			
index, value = max(enumerate(dist), key=operator.itemgetter(1))



im = cv2.drawContours(img1,cnt1,-1,(0,255,0),5)

plt.imshow(im,cmap='Greys_r')
plt.show()