import cv2
import numpy as np

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
img = cv2.imread('test_sample12.jpg', 0)  # 331, 328 Search for an image full of circles
ret, thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('before', thresh)
edges = cv2.Canny(thresh,0,255)
cv2.imshow('after', edges)
contours,hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(edges, contours, -1, (255,255,255), 1)
cv2.imshow('Contour',edges)
# Update upper part
circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:

    cv2.circle(edges,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',edges)
print(circles)

cv2.waitKey(0)
cv2.destroyAllWindows()
