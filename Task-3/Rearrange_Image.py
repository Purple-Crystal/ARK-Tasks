import cv2
import numpy as np

image=cv2.imread("C:/Research Group/Level1.png", cv2.IMREAD_COLOR)
img=np.zeros((200,150,3),dtype="uint8")
cv2.imshow("Black",img)
x = 0
y = 0
for i in range(94,177):
   
    img[y,x,0]=image[6,i,0]
    img[y,x,1]=image[6,i,1]
    img[y,x,2]=image[6,i,2]
    x=x+1



for j in range(7,176):
    for i in range(0,177):
        
        img[y,x,0]=image[j,i,0]
        img[y,x,1]=image[j,i,1]
        img[y,x,2]=image[j,i,2]
        x=x+1
        if(x>149):   
          y=y+1
          x=0
    


    
cv2.imshow("New",img)


cv2.waitKey(0)
k = cv2.waitKey(0)
if k == ord('q'):
    cv2.destroyAllWindows()
