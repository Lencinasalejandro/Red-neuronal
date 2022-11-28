#prueba https://www.youtube.com/watch?v=oXlwWbU8l2o

import cv2 as cv
import numpy as np

#Reading img

img =cv.imread('fotos/Perro01.jpeg') #leer imagen
cv.imshow('perro',img) #muestra la imagen

def rescaleFrame(frame,scale=0.5):
    """Cambiar tamaño"""
    width=int (frame.shape[1] * scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
 
"""def changeRes(width,height): #ver captura de video en vivo
    capture.set(3,width)
    capture.set(4,height)
"""

resized_image=rescaleFrame(img,0.2)

cv.imshow('Resized',resized_image)

cv.waitKey(0)


