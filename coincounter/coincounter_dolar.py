import numpy as np
import cv2 as cv
import os

def _blob_detection(img):
    # creating parameters for filtering
    params = cv.SimpleBlobDetector_Params()
    params.filterByArea = True
    params.minArea = 1;
    params.maxArea = 100000;
    params.filterByColor = True
    params.blobColor = 0

    # creating a detector with the parameters
    detector = cv.SimpleBlobDetector_create(params)

    # getting blobs data
    return detector.detect(img)    
     
def _draw_coins(output, keypoints):
    for i in range(len(keypoints)):
        cv.circle(output, (int(keypoints[i].pt[0]), int(keypoints[i].pt[1])), 
                          int(keypoints[i].size/2), (0, 255, 0), 4)
        cv.circle(output, (int(keypoints[i].pt[0]), int(keypoints[i].pt[1])), 
                          1, (255, 0, 0), 5)
    return output

def _save_result(output):
    dirName = "..\\image_result"
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    cv.imwrite(dirName + "\\dolar_result.png", output)  
    
#-----------------------------------------------------------------------------
# MAIN LOOP 
#-----------------------------------------------------------------------------
# reading original image
input_dolar = cv.imread("..\\assets\\dolar_original.png")

# converting to grayscale
input_dolar_gray = cv.cvtColor(input_dolar, cv.COLOR_BGR2GRAY)

# converting image to binary pattern expected of part 3
input_dolar_bin = cv.threshold(input_dolar_gray,50,255,cv.THRESH_BINARY_INV)[1]

# creating kernels to be used as structuring elements in morpholog. operations
kernel = np.ones((1,2), np.uint8) 
kernel2 = cv.getStructuringElement(cv.MORPH_ELLIPSE,(20,20))

# eroding initial gray img to get rid of noise in the interior region of coins
erosion = cv.erode(input_dolar_bin,kernel,iterations = 3)

# dilating result to homogenize bkgrd w/ circular kernel to smooth coins edges
dilation = cv.dilate(erosion,kernel2,iterations = 2)

# eroding previous result to get blobs back to original coin size
erosion2 = cv.erode(dilation,kernel2,iterations = 2)

# getting blobs data
keypoints = _blob_detection(erosion2)

# number of coins (blobs) detected
print('Number of coins detected: ', len(keypoints))

# drawing coins (blobs) borders
borders = cv.drawKeypoints(erosion2, keypoints, np.array([]), (0,0,255), 
			   cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# drawing circles on original image using data from blob detection
output = input_dolar.copy()
output = _draw_coins(output, keypoints)

# saving result as a file
_save_result(output) 

# showing results
cv.imshow('input image', input_dolar)
cv.imshow('input image in grayscale', input_dolar_gray)
cv.imshow('input image binarized', input_dolar_bin)
cv.imshow('bin image with morphological filtering', erosion2)
cv.imshow("bin image with borders detection", borders)
cv.imshow('output image with detected coins', output)

cv.waitKey(0)
cv.destroyAllWindows()
