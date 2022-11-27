import numpy as np
from scipy import signal
import cv2
import matplotlib.pyplot as plt

def motion_constraints(Iref, Inext):
    kernel_x = np.array([[-1., 1.], [-1., 1.]])*.25
    kernel_y = np.array([[-1., -1.], [1., 1.]])*.25
    kernel_t = np.array([[1., 1.], [1., 1.]])*.25
    Iref = Iref / 255. 
    Inext = Inext / 255.
    mode = 'same'

    Ix = signal.convolve2d(Iref, kernel_x, boundary='symm', mode=mode)
    Iy = signal.convolve2d(Iref, kernel_y, boundary='symm', mode=mode)
    It = signal.convolve2d(Inext, kernel_t, boundary='symm', mode=mode) + signal.convolve2d(Iref, -kernel_t, boundary='symm', mode=mode)
    return Ix, Iy, It

frame1 = cv2.imread("frame1.jpeg")
frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame1 = cv2.resize(frame1, (70,70))

frame2 = cv2.imread("frame2.jpg")
frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
frame2 = cv2.resize(frame2, (70,70))

Ix, Iy, It = motion_constraints(frame1, frame2)
print(Ix, Iy, It)
