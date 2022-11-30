#prueba https://www.youtube.com/watch?v=oXlwWbU8l2o

import cv2 as cv

def rescaleFrame(frame,scale=0.5):
    """Cambiar tamaño sirve para imagenes, video y captura de video en vivo"""
    width=int (frame.shape[1] * scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
 
def changeRes(width,height): 
    """Solo sirve para captura de video en vivo"""    
    capture.set(3,width)
    capture.set(4,height)

#Reading img

img =cv.imread('fotos/Perro01.jpeg')    #Leer imagen original
cv.imshow('perro',img)                  #Muestra la imagen

resized_image=rescaleFrame(img,0.2)     #Ajusta la imagen
cv.imshow('Resized',resized_image)      #Muestra la imagen


# Reading Videos

capture= cv.VideoCapture(0,cv.CAP_DSHOW)

while True:
    isTrue, frame = capture.read()
    frame_resized=rescaleFrame(frame,0.2)
    cv.imshow('Video',frame)
    cv.imshow('Video_Resized',frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()