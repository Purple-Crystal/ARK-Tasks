import numpy as np
from scipy.io.wavfile import write
from PIL import Image
from numpy import asarray, uint16
import cv2
img = Image.open('C:/Users/admin/Downloads/treasure_mp3.png')   
#img=cv2.imread("C:/Users/admin/Downloads/treasure_mp3.png")
WIDTH, HEIGHT = img.size
#data = [[0 for i in range(390)] for j in range(390)]
#WIDTH=390
#HEIGHT=390
print(WIDTH,HEIGHT)
#for i in range (WIDTH):
    #for j in range (WIDTH):
        #data[i][j]=img[i][j]

data = list(img.getdata())
data = ([data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)])
print(data)
arr = np.array(data)
scaled = np.int16(arr/np.max(np.abs(arr)) * 32767)
write('test_new.wav', 44100, scaled)