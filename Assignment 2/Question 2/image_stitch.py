import numpy as np
import cv2

rialto = ["/Users/rakhi/Desktop/CV/Assignment 2/Question 2/set3/rialto_team6-1.jpeg", "/Users/rakhi/Desktop/CV/Assignment 2/Question 2/set3/rialto_team6-2.jpeg", "/Users/rakhi/Desktop/CV/Assignment 2/Question 2/set3/rialto_team6-3.jpeg"]
bookstore = ["bookstore1.jpg", "bookstore2.jpg", "bookstore3.jpg"]
library_north = ["LibraryNorth_team06_1.jpeg", "LibraryNorth_team06_2.jpeg", "LibraryNorth_team06_3.jpeg"]
arts = ["Art and humanities01_team6.jpg", "Art and humanities02_team6.jpg" , "Art and humanities03_team6.jpg"]
rec_center = ["rec_center1.jpg", "rec_center2.jpg", "rec_center3.jpg"]

images = []

for path in rialto:
	image = cv2.imread(path)
	images.append(image)

stitcher = cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

if status == 0:
	print("stiching is successful")
	cv2.imshow("Stitched", stitched)
	cv2.waitKey(0)
else:
	print("[INFO] image stitching failed ({})".format(status))