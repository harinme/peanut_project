import cv2
from ultralytics import YOLO
import time
import pygame.mixer
import numpy as np

# YOLO 모델 로드
model = YOLO("best_low.pt")

# 웹캠 초기화
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while webcam.isOpened():
    status, frame = webcam.read()
    
    if status:
        result = model.predict(frame, save=True, conf=0.8)
        time.sleep(1)
        print(result[0].boxes)

        # unpeeled 클래스(클래스 인덱스 1) 개수 세기
        bad = list(result[0].boxes.cls).count(1)
        print('검출된 불량의 개수: ', bad)

        # 프레임 복사본 생성 (마스크를 그리기 위해)
        frame_with_masks = frame.copy()

        # unpeeled 항목만 마스크와 라벨을 그림
        for i, box in enumerate(result[0].boxes):
            if int(box.cls[0]) == 1:  # 클래스 인덱스 1이 unpeeled 항목이라고 가정
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # 좌표 가져오기
                label = result[0].names[int(box.cls[0])]  # 클래스 라벨 가져오기
                confidence = box.conf[0]  # 신뢰도 가져오기

                # 바운딩 박스 그리기
                cv2.rectangle(frame_with_masks, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame_with_masks, f'{label} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                # 세그멘테이션 마스크가 있으면 그리기
                if hasattr(result[0], 'masks') and result[0].masks is not None:
                    mask = result[0].masks.data[i].cpu().numpy()  # 마스크를 numpy 배열로 변환
                    mask = (mask * 255).astype(np.uint8)  # 마스크를 uint8로 변환
                    mask = np.stack((mask,)*3, axis=-1)  # 마스크를 3채널 이미지로 변환
                    colored_mask = np.zeros_like(frame_with_masks)
                    colored_mask[mask[:,:,0] > 0] = [0, 255, 0]  # 마스크에 색상 적용
                    frame_with_masks = cv2.addWeighted(frame_with_masks, 1, colored_mask, 0.5, 0)

        # 마스크와 함께 프레임 표시
        cv2.imshow("Detection", frame_with_masks)

        # 불량 항목 개수에 따라 다른 음성 파일 재생
        if bad == 1:
            pygame.mixer.init()
            pygame.mixer.music.load("voice1.mp3")
            pygame.mixer.music.play()
            time.sleep(1.5)
            pygame.mixer.music.load("voicestop.mp3")
            pygame.mixer.music.play()
        elif bad == 2:
            pygame.mixer.init()
            pygame.mixer.music.load("voice2.mp3")
            pygame.mixer.music.play()
            time.sleep(1.5)
            pygame.mixer.music.load("voicestop.mp3")
            pygame.mixer.music.play()
        elif bad == 3:
            pygame.mixer.init()
            pygame.mixer.music.load("voice3.mp3")
            pygame.mixer.music.play()
            time.sleep(1.5)
            pygame.mixer.music.load("voicestop.mp3")
            pygame.mixer.music.play()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(2)

# 웹캠 릴리즈 및 창 닫기
webcam.release()
cv2.destroyAllWindows()
