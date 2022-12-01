# Importamos librerias
import cv2 as cv  #python3 -m pip install opencv-contrib-python
import numpy as np
import torch

# Leemos el modelo entrenado
model = torch.hub.load('ultralytics/yolov5', 'custom',
    path = 'E:/0-code/DATA SET/Dataset 01-ok- frutilla.v1i.yolov5pytorch/model/frutilla.pt')

# Realizo Videocaptura int:0 es la webcam de la notebook
cap = cv.VideoCapture(0)

# Empezamos
while True:
    # Realizamos lectura de frames y las guarda
    ret, frame = cap.read()

    # Correccion de color
    #frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # Realizamos las detecciones
    detect = model(frame)

    info = detect.pandas().xyxy[0]  # im1 predictions
    print(info)

    # Mostramos FPS
    cv.imshow('Frutillas', np.squeeze(detect.render()))

    # Leemos el teclado
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cap.release()
cv.destroyAllWindows()
