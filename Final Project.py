import cv2
import numpy as np
import array

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
img = cv2.imread('test_sample13.jpg', 0)  # 331, 328 Search for an image full of circles
cv2.imshow('Original',img)
ret, thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('before', thresh)
#edges = cv2.Canny(thresh,0,255)
#cv2.imshow('after', edges)
#contours,hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(edges, contours, -1, (255,255,255), 1)
#cv2.imshow('Contour',edges)
ret, thresh2 = cv2.threshold(img,0,0,cv2.THRESH_BINARY_INV)

# Update upper part
circles = cv2.HoughCircles(thresh,cv2.HOUGH_GRADIENT,1,20,param1=80,param2=10,minRadius=2,maxRadius=2)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(thresh2,(i[0],i[1]),1,(255,255,255))
    cv2.imshow('circles',thresh2)
    print(circles)
    print(len(circles[0]))
print (circles[0][0][0])

def Answer (Question_no, x_axis,y_axis):
    if (i[0] >= 292) & (i[0] <= 302) & (i[1] >= 236):
        print('Question: %5.1f Strongly Agree'%(Question_no))
    if (i[0] >= 318) & (i[0] <= 328) & (i[1] >= 236):
        print('Question: %5.1f Agree' % (Question_no))
    if (i[0] >= 345) & (i[0] <= 355) & (i[1] >= 236):
        print('Question: %5.1f Neutral' % (Question_no))
    if (i[0] >= 371) & (i[0] <= 381) & (i[1] >= 236):
        print('Question: %5.1f Disagree' % (Question_no))
    if (i[0] >= 398) & (i[0] <= 408) & (i[1] >= 236):
        print('Question: %5.1f Strongly Disagree' % (Question_no))
value = 255
count = 1.1
count2 = 1.0
j = 0
while j != 19:
    for i in circles[0]:
        if (i[1] >= value) & (i[1] <= (value+11)):
            print(i[1])
            print(value)
            Answer(count,0,0)
            if (count == 4.2):
                value = value - 20
            else:
                value = value + 10
            count = round(count + 0.1,1)
            j += 1
            print(i[1])
            print (value)
            if ((round(count-count2,1)) == 0.6) & (count2 == 1.0):
                count = 2.1
                count2 += 1.0
                value += 25
            if (round(count-count2,1) == 0.7) & (count2 == 2.0):
                count = 3.1
                count2 += 1.0
                value += 25
            if (round(count-count2,1) == 0.4) & (count2 >= 3.0):
                if count2 == 3.0:
                    count = 4.1
                    count2 += 1.0
                    value += 25
                else:
                    count = 5.1

cv2.waitKey(0)
cv2.destroyAllWindows()
