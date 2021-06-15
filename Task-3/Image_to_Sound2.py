import numpy as np
import cv2
from scipy.io.wavfile import write
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img=cv2.imread('C:/Users/admin/Downloads/treasure_mp3.png',0)
n,m=img.shape
k=0
data=np.empty(n*m,np.int16)
for i in range(n):
    for j in range (m):
        data[k]=int(img[i][j])
        k=k+1;

#scaled=np.int16(data/np.max(np.abs(data))*32767)
write('test.wav', n*m, data)
cv2.imshow('image',img.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()

