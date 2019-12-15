import cv2
import numpy as np
import sys

img = cv2.imread('test_sample12.jpg', 0)  # 331, 328 Search for an image full of circles
cv2.imshow('before', img)
edges = cv2.Canny(img,127,255)
cv2.imshow('after', edges)
# Circles will be detected using Contours and hit&miss algorithm


cv2.waitKey()