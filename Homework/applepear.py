import cv2
import numpy as np

apple=cv2.imread("Lesson 2/Homework/images/apple.jpg")
pear=cv2.imread("Lesson 2/Homework/images/pear.jfif")

apple=cv2.resize(apple,(1000,1000))
pear=cv2.resize(pear,(1000,1000))

addition=cv2.addWeighted(apple,0.3,pear,0.7,0)
cv2.imshow("addition",addition)

substract=cv2.subtract(pear,apple)
cv2.imshow("subtraction",substract)

kernel=np.ones((9,9),np.uint8) 
erosion=cv2.erode(apple,kernel)
cv2.imshow("erosion",erosion)

bfilter=cv2.bilateralFilter(pear,9,75,75)
cv2.imshow("bilateralfilter",bfilter)

mblur=cv2.medianBlur(pear,5)
cv2.imshow("medianblur",mblur)

gblur=cv2.GaussianBlur(pear,(7,7),0)
cv2.imshow("gaussianblur",gblur)


cv2.waitKey(0)

cv2.destroyAllWindows()