import cv2
from ultralytics import YOLO
import time

model=YOLO("best_low.pt")
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

while webcam.isOpened():
    status, frame = webcam.read()
    if status:

        result=model.predict(frame, save=True)
        time.sleep(1)        


webcam.release()
cv2.destroyAllWindows()