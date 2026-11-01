import cv2

excavator=cv2.imread("Lesson 2/images/excavator.jpg")

excavator=cv2.resize(excavator,(250,250))

borderimage=cv2.copyMakeBorder(excavator,10,10,10,10,cv2.BORDER_CONSTANT,value=(200,200,200))

cv2.imshow("exborder",borderimage)

cv2.waitKey(0)

borderimages=cv2.copyMakeBorder(excavator,100,100,100,100,cv2.BORDER_REFLECT)

cv2.imshow("reflectborder",borderimages)

cv2.waitKey(0)