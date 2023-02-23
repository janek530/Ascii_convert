import cv2 as cv
import numpy as np
import sys, random, argparse
import pandas as pd
import matplotlib.pylab as plt

gray = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def resize_image(image):
    file = open("ascci.txt", "w")
    ascii_tab = []
    img = cv.cvtColor(cv.imread(image), cv.COLOR_BGR2GRAY)
    scale_percent = 400
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    if img.shape[0] or img.shape[1] > 1000:
        img = cv.resize(img, dim,  interpolation = cv.INTER_AREA)

    img_pixeled = cv.resize(img, None, fx=0.50, fy=0.25)
    # fig, ax = plt.subplots(figsize=(8, 8))
    # plt.imshow(img_pixeled, cmap="Greys")
    # plt.show()
    for i in img_pixeled:
        ascii_line = []
        for pixel in i:
            for j in range(69, 0, -1):
                if int(pixel/3.657142857142857)==70-j:
                    ascii_line.append(gray[j])
        ascii_tab.append(ascii_line)

    for line in ascii_tab:
        for i in line:
            file.write(i)
        file.write("\n")
    print("Ready!")
    return img_pixeled