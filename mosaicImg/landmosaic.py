import dlib
import cv2
import numpy as np
from imutils import face_utils

def land_mosaic(image_path):
    # 이미지 로드
    frame = cv2.imread(image_path)

    # 얼굴 감지 및 랜드마크 예측 모델 설정
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('../shape_predictor_68_face_landmarks.dat/shape_predictor_68_face_landmarks.dat')

    # 회색 이미지로 변환
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴 감지
    faces = detector(img_gray)

    for face in faces:
        # 얼굴 랜드마크 예측
        landmarks = predictor(img_gray, face)
        points = face_utils.shape_to_np(landmarks)
        rect = cv2.boundingRect(points)
        x, y, w, h = rect

        # 모자이크 처리할 영역 추출
        mosaic = frame[y:y + h, x:x + w].copy()

        # 모자이크 적용
        mosaic = cv2.blur(mosaic, (25, 25))  # 흐림 효과 적용
        mosaic = cv2.resize(mosaic, dsize=(w, h), interpolation=cv2.INTER_NEAREST)
        frame[y:y + h, x:x + w] = mosaic

    # 모자이크 처리된 이미지 출력
    cv2.imshow('Mosaic Image', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()