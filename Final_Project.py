import cv2
import numpy as np
import math

x = input("Enter image path : ")
def rotateImage(image, angle): # image rotation function by calculating the center of the image and then rotate it
    image_center = tuple(np.array(image.shape[1::-1]) / 2) # calculating the center of image
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0) # calculating the suitable rotation matrix
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR) # Getting the final image as a result
    return result


file = open("Output.txt","w+") # Opening the output file to use it
img = cv2.imread(x, 0) # Reading the input image
img = cv2.resize(img,(481,680)) # Resizing the image
img = cv2.bitwise_not(img) # Inverting the image to be ready for applying some operations

img_edges = cv2.Canny(img, 100, 100, apertureSize=3) # Edge detection
lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=50, maxLineGap=5) # Line detection
angles = []
for x1, y1, x2, y2 in lines[0]:

    angle = math.degrees(math.atan2(y2 - y1, x2 - x1)) # Calculating the angle of rotation by calculating slope
    angles.append(angle)

median_angle = np.median(angles) # Getting the angle value to rotate the image

img = rotateImage(img,median_angle) # Image rotation function by passing the image and the angle calculated before
img = cv2.resize(img,(481,680)) # Resizing again after rotation

ret, thresh = cv2.threshold(img,235,255,cv2.THRESH_BINARY) # Applying thresholding on the image to get the needed information only
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
eroded = cv2.erode(thresh,kernel)
eroded = cv2.dilate(eroded,kernel) # erosion to make sure there is no noise

answers = cv2.connectedComponentsWithStats(eroded, 4, cv2.CV_32S) # Function to detect the components in the image after thresholding
answers = answers[2]
answers = answers[1:23]
j = 0
Question_no = "1.1","1.2","1.3","1.4","1.5","2.1","2.2","2.3","2.4","2.5","2.6","3.1","3.2","3.3","4.1","4.2","4.3",\
              "5.1","5.2"
for i in answers: # printing the answers detected from the image
    if i[1] == answers[0][1]:
        if (i[0] >= 353) & (i[0] <= 391):
            file.write("Gender: Male \r\n")
        elif (i[0] >= 392) & (i[0] <= 446):
            file.write("Gender: Female \r\n")
    if i[1] == answers[1][1]:
        # Continue semester values
        if (i[0] >= 145) & (i[0] <= 185):
            file.write("Semester: Fall \r\n")
        if (i[0] >= 190) & (i[0] <= 260):
            file.write("Semester: Spring \r\n")
        if (i[0] >= 290) & (i[0] <= 350):
            file.write("Semester: Summer \r\n")
    if i[1] == answers[2][1]:
        # Program value
        if (i[0] >= 120) & (i[0] <= 150) & ~(i[1] >= 140):
            file.write("Program: MCTA \r\n====================================================================== \r\n"
                       "====================================================================== \r\n")  # done
        if (i[0] >= 159) & (i[0] <= 189) & ~(i[1] >= 140):
            file.write("Program: ENVER \r\n====================================================================== \r\n"
                       "====================================================================== \r\n")  # done
        if (i[0] >= 198) & (i[0] <= 228) & ~(i[1] >= 140):
            file.write("Program: BLDG \r\n====================================================================== \r\n"
                       "====================================================================== \r\n")  # done
        if (i[0] >= 237) & (i[0] <= 277) & ~(i[1] >= 140):
            file.write("Program: CESS \r\n====================================================================== \r\n"
                       "====================================================================== \r\n")  # done
        if (i[0] >= 275) & (i[0] <= 305) & ~(i[1] >= 140):
            file.write("Program: ERGY \r\n====================================================================== \r\n"
                       "====================================================================== \r\n")  # done
        if (i[0] >= 307) & (i[0] <= 337) & ~(i[1] >= 140):
            file.write("Program: COMM \r\n====================================================================== \r\n"
                       "====================================================================== \r\n")  # done
        if (i[0] >= 354) & (i[0] <= 384) & ~(i[1] >= 140):
            file.write("Program: MANF \r\n====================================================================== \r\n"
                       "====================================================================== \r\n")  # done
        if (i[0] >= 120) & (i[0] <= 150) & (i[1] >= 140):
            file.write("Program: LAAR \r\n====================================================================== \r\n"
                       "====================================================================== \r\n")  # done
        if (i[0] >= 159) & (i[0] <= 189) & (i[1] >= 140):
            file.write("Program: MATL \r\n====================================================================== \r\n"
                       "====================================================================== \r\n")  # done
        if (i[0] >= 198) & (i[0] <= 228) & (i[1] >= 140):
            file.write("Program: CISE \r\n====================================================================== \r\n"
                       "====================================================================== \r\n")  # done
        if (i[0] >= 237) & (i[0] <= 277) & (i[1] >= 140):
            file.write("Program: HAUD \r\n====================================================================== \r\n"
                       "====================================================================== \r\n")  # done

    while (j != 19) & (i[1] >= answers[3][1]):
        if i[1] == answers[j+3][1]:
            # Questions
            if (i[0] >= 310) & (i[0] <= 340):
                file.write("Question"+Question_no[j] + " : Strongly Agree \r\n====================================================================== \r\n")
                j += 1
                break
            if (i[0] >= 341) & (i[0] <= 371):
                file.write("Question"+Question_no[j] + " : Agree \r\n====================================================================== \r\n")
                j += 1
                break
            if (i[0] >= 372) & (i[0] <= 402):
                file.write("Question"+Question_no[j] + " : Neutral \r\n====================================================================== \r\n")
                j += 1
                break
            if (i[0] >= 403) & (i[0] <= 433):
                file.write("Question"+Question_no[j] + " : Disagree \r\n====================================================================== \r\n")
                j += 1
                break
            if (i[0] >= 434) & (i[0] <= 474):
                file.write("Question"+Question_no[j] + " : Strongly Disagree \r\n====================================================================== \r\n")
                j += 1
                break
file.close()
print("Finisheed Successfuly")
cv2.waitKey(0)
#cv2.destroyAllWindows()
