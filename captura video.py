import cv2 as cv

capture= cv.VideoCapture(0,cv.CAP_DSHOW) #INt 0:webcam / oruta al video entre comillas

while True: #loop de lectura de video
    isTrue, frame = capture.read() #captura video cuadro por cuadro y devuelve true si lo pudo hacer
    cv.imshow('Video',frame) #muestra la captura obtenida del video,
        
    if cv.waitKey(20) & 0xFF==ord('d'): # si presionamos "d" salimos del loop
        break

capture.release()
cv.destroyAllWindows()