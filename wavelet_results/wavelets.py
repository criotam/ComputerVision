
import pywt
import cv2
import numpy as np
import glob
from matplotlib import pyplot as plt


def  coeff(p_wavelet,I1):
	wavelet = p_wavelet#wavelets[0]#'db1'
	
	cooef1 = pywt.wavedec2(I1[:,:], wavelet)


	cooef2 = pywt.dwt2(I1[:,:], wavelet)
	cA, (cH, cV, cD) = cooef2
	max = np.abs(cooef2[0]).max()
	li = ['cA','cH','cV','cD','sd']
	k=0
	for i ,j in enumerate([cA,cH,cV,cD]):
		i=i+1
		a = li[k]
		k+=1
		print(len(cH))

		plt.subplot(2,2,i)
		plt.title(a)
		plt.imshow(j,cmap="Greys_r")
		
	plt.show()
	

img1 = cv2.imread("/home/rgukt/Pictures/0.jpeg",0)


funcaofeia("haar",img1)
		
