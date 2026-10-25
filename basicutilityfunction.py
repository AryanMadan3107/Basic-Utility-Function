import cv2
import numpy as np

image1=cv2.imread("Lesson 2/images/excavator.jpg")
image2=cv2.imread("Lesson 2/images/truck.jpg")

sum=cv2.addWeighted(image1,0.5,image2,0.5,0)
cv2.imshow("addition",sum)

sub=cv2.subtract(image2,image1)
cv2.imshow("subtraction",sub)

multiply=cv2.multiply(image2,2)
cv2.imshow("multiplication",multiply)

divide=cv2.divide(image1,image2)
cv2.imshow("division",divide)

resize1=cv2.resize(image1,(500,300))
cv2.imshow("resize1",resize1)

kernel=np.ones((9,9),np.uint8) 
erosion=cv2.erode(image1,kernel)
cv2.imshow("erosion",erosion)

gblur=cv2.GaussianBlur(image2,(7,7),0)
cv2.imshow("gaussianblur",gblur)

mblur=cv2.medianBlur(image2,5)
cv2.imshow("medianblur",mblur)

bfilter=cv2.bilateralFilter(image2,9,75,75)
cv2.imshow("bilateralfilter",bfilter)

cv2.waitKey(0)

cv2.destroyAllWindows()