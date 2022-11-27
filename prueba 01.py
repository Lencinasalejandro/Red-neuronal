#prueba https://www.youtube.com/watch?v=oXlwWbU8l2o

import cv2 as cv
import numpy as np

#Reading img

img =cv.imread('fotos/Perro01.jpeg')
cv.imshow('perro',img)

def rescaleFrame(frame,scale=0.5):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

cv.waitKey(0)

resized_image=rescaleFrame('Perro2.jpeg',0.2)

cv.imshow('Resized',resized_image)

cv.wait(0)


