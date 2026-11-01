import cv2
import numpy as np

pikachu=cv2.imread("Lesson 3/images/pikachu.png")
pikachu1=cv2.cvtColor(pikachu,cv2.COLOR_BGR2GRAY)

img=pikachu.astype(np.int32)

(row,col)=img.shape[0:2]

for i in range (row):
    for j in range (col):
        average=int(sum(img[i,j])/3)
        img[i,j]=[average,average,average]

img=img.astype(np.uint8)

cv2.imshow("Grayscale",img)

cv2.waitKey(0)

