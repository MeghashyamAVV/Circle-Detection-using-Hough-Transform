import cv2
import numpy as np
image = cv2.imread('img.JPG')
output = image.copy()
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,  1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 70)
if circles is not None:
   circles = np.round(circles[0, :]).astype("int" )
   print(circles)
   for (x, y, r) in circles:
      cv2.circle(output, (x, y), r, (0, 255, 0), 2)
cv2.imshow("detected",output)
cv2.waitKey(0)