import numpy as np
import cv2 as cv
import os

def _draw_circles(output, circles):
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv.circle(output, (x, y), r, (0, 255, 0), 4)
            cv.circle(output, (x, y), 1, (0, 0, 255), 5)  
    return output   

def _save_result(output):
    dirName = "..\\image_result"
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    cv.imwrite(dirName + "\\real_result.jpg", output)  

#------------------------------------------------------------
# MAIN LOOP 
#------------------------------------------------------------
# reading original image
input_real = cv.imread("..\\assets\\real_original.jpg")

# converting to grayscale
input_real_gray = cv.cvtColor(input_real, cv.COLOR_BGR2GRAY)

# applying GaussianBlur filter
input_real_blur = cv.GaussianBlur(input_real_gray,(11,11),cv.BORDER_DEFAULT)

# detecting circles using HoughCircles
circles = cv.HoughCircles(input_real_blur,cv.HOUGH_GRADIENT,1.2,100)

# printing number of coins (circles) detected
print('Number of coins detected: ', len(circles[0,:]))

# drawing detected circles on original image
output = input_real.copy()
output = _draw_circles(output, circles)  

# saving result as a file
_save_result(output) 

# showing results
cv.imshow('input image', input_real)
cv.imshow('input image in grayscale', input_real_gray)
cv.imshow('input image in grayscale and blurred', input_real_blur)
cv.imshow('output image with detected coins', output)

cv.waitKey(0)
cv.destroyAllWindows()