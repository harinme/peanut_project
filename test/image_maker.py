import cv2
from ultralytics import YOLO
import time
import os

model = YOLO("best_add.pt")
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

image_count = 21
last_save_time = time.time()

while webcam.isOpened():
    status, frame = webcam.read()
    if status:
        current_time = time.time()
        if current_time - last_save_time >= 3:  # 3초마다 저장
            image_filename = f"image{image_count}.jpg"
            cv2.imwrite(image_filename, frame)
            image_count += 1
            last_save_time = current_time
            print(f"Saved {image_filename}")

        result = model.predict(frame, save=True)
        time.sleep(1)  # 모델 예측 시간 조정

webcam.release()
cv2.destroyAllWindows()
