import cv2
import numpy as np
import array
import math
from scipy import ndimage

img = cv2.imread('test_sample8.jpg', 0)# 331, 328 Search for an image full of circles
img = cv2.resize(img,(481,680))
cv2.imshow("aaa", img)
#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_edges = cv2.Canny(img, 100, 100, apertureSize=3)
lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=50, maxLineGap=5)

angles = []

for x1, y1, x2, y2 in lines[0]:
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    angles.append(angle)

median_angle = np.median(angles)
img = ndimage.rotate(img, median_angle)

print("Angle is {}".format(median_angle))
cv2.imshow('Rotated', img)
# scale_percent = 30 # percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)
# img = cv2.resize(img, dim)
# cv2.imshow('Resized', img)
# ret, thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV)
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
# kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
# cv2.imshow('Thresh 2', thresh)
# answers = cv2.connectedComponentsWithStats(thresh, 4, cv2.CV_32S)
# answers = answers[2]
# answers = answers[1:23]
# print("Number Of Circles", len(answers))
# print("Array", answers)
#
# def Answer (Question_no, x_axis,y_axis):
#     if (i[0] >= 292) & (i[0] <= 302) & (i[1] >= 236):
#         print('Question: %5.1f Strongly Agree'%(Question_no))
#     if (i[0] >= 318) & (i[0] <= 328) & (i[1] >= 236):
#         print('Question: %5.1f Agree' % (Question_no))
#     if (i[0] >= 345) & (i[0] <= 355) & (i[1] >= 236):
#         print('Question: %5.1f Neutral' % (Question_no))
#     if (i[0] >= 371) & (i[0] <= 381) & (i[1] >= 236):
#         print('Question: %5.1f Disagree' % (Question_no))
#     if (i[0] >= 398) & (i[0] <= 408) & (i[1] >= 236):
#         print('Question: %5.1f Strongly Disagree' % (Question_no))
# value = 255
# count = 1.1
# count2 = 1.0
# j = 0
# while j != 19:
#     for i in circles[0]:
#         if (i[1] >= value) & (i[1] <= (value+11)):
#             print(i[1])
#             print(value)
#             Answer(count,0,0)
#             if (count == 4.2):
#                 value = value - 20
#             else:
#                 value = value + 10
#             count = round(count + 0.1,1)
#             j += 1
#             print(i[1])
#             print (value)
#             if ((round(count-count2,1)) == 0.6) & (count2 == 1.0):
#                 count = 2.1
#                 count2 += 1.0
#                 value += 25
#             if (round(count-count2,1) == 0.7) & (count2 == 2.0):
#                 count = 3.1
#                 count2 += 1.0
#                 value += 25
#             if (round(count-count2,1) == 0.4) & (count2 >= 3.0):
#                 if count2 == 3.0:
#                     count = 4.1
#                     count2 += 1.0
#                     value += 25
#                 else:
#                     count = 5.1

cv2.waitKey(0)
cv2.destroyAllWindows()
