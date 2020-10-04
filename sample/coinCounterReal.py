import numpy as np
import cv2 as cv
import os

# reading original image
input_real = cv.imread("..\\assets\\real_original.jpg")

# converting to grayscale
input_real_gray = cv.cvtColor(input_real, cv.COLOR_BGR2GRAY)

# applying GaussianBlur filter
input_real_blur = cv.GaussianBlur(input_real_gray,(11,11),cv.BORDER_DEFAULT)

# detecting circles using HoughCircles
circles = cv.HoughCircles(input_real_blur,cv.HOUGH_GRADIENT,1.2,100)

# drawing detected circles in original image
output = input_real.copy()
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv.circle(output, (x, y), r, (0, 255, 0), 4)
        cv.circle(output, (x, y), 1, (0, 0, 255), 5)  

# printing number of coins (circles) detected
print('Number of coins detected: ', len(circles))

# creating folder to save result
dirName = "..\\image_result"
if not os.path.exists(dirName):
    os.mkdir(dirName)

# saving result as a file
cv.imwrite(dirName + "\\real_result.jpg", output) 

# showing results
cv.imshow('input image', input_real)
cv.imshow('input image in grayscale', input_real_gray)
cv.imshow('input image in grayscale and blurred', input_real_blur)
cv.imshow('output image with detected coins', output)

cv.waitKey(0)
cv.destroyAllWindows()