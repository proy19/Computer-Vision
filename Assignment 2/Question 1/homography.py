#!/usr/bin/env python
 
import cv2
import numpy as np
 
if __name__ == '__main__' :
 
    # Read source image.
    im_src = cv2.imread('image2.jpeg')
    # Coordinates of the source image
    pts_src = np.array([[447, 142], [585, 118], [450, 438],[584, 432]])
 
    # Read destination image.
    im_dst = cv2.imread('image.jpeg')
    # Coordinates of destination image.
    pts_dst = np.array([[83, 138],[213, 125],[107, 444],[236, 444]])
 
    # Calculate Homography
    h, status = cv2.findHomography(pts_src, pts_dst)
 
    # Warp source image to destination based on homography
    im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))

    print(h)

    #Homography Matrix 
    # [[ 1.02517117e+00  6.91576115e-02 -3.81221505e+02]
   # [ 1.01643800e-01  1.05874101e+00 -5.13741482e+01]
   #  [ 1.19886476e-04 -5.06972385e-05  1.00000000e+00]]
 
    # Display images
    cv2.imshow("Source Image", im_src)
    cv2.imshow("Destination Image", im_dst)
    cv2.imshow("Warped Source Image", im_out)
 
    cv2.waitKey(0)
