import cv2
import numpy as np
import imutils

img = cv2.imread('img/20210612_080853488_iOS.jpg')

img = cv2.resize(img, (500,500))  # 將大小修改成250*250

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range = np.array([23,34,15])
upper_range = np.array([42,49,30])

mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow('image', img)
cv2.imshow('mask', mask)

while(True):
 k = cv2.waitKey(5) & 0xFF
 if k == 27:
   break

cv2.destroyAllWindows()