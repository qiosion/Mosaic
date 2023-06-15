import os
import cv2
from django.shortcuts import render, redirect

from config import settings
from mosaicImg.models import MosaicImg


def mosaic_download(request, mos_no):
    mos = MosaicImg.objects.get(mos_no=mos_no)

    board_no = str(mos.board_no.board_no).zfill(8)
    mosaic_path = os.path.join(settings.MEDIA_ROOT, 'mosaic', f'mosaic_{board_no}.jpg')
    mosaic_url = settings.MEDIA_URL + 'mosaic/' + f'mosaic_{board_no}.jpg'

    return redirect(mosaic_url)


def get_mosaic_haar(request, mos_no):
    mos = MosaicImg.objects.get(mos_no=mos_no)
    board_no = str(mos.board_no.board_no).zfill(8)

    input_path = os.path.join(settings.MEDIA_ROOT, 'uploads', f'{board_no}.jpg')
    print("input_path : ", input_path)

    # haarcascade 불러오기
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    sideface_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    # 이미지 불러오기
    img = cv2.imread(input_path)
    print("img : ", img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 얼굴 찾기
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)
    for (x, y, w, h) in faces:
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y: y+h, x: x+w]
        roi_color = img[y: y+h, x: x+w]

        # 모자이크 처리
        roi_color = cv2.blur(roi_color, (50, 50))
        img_w_mosaic = img
        img_w_mosaic[y: y+h, x: x+w] = roi_color

        # 눈 찾기
        eye = eye_cascade.detectMultiScale(roi_gray, 2, 2)
        for (ex, ey, ew, eh) in eye:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

    sideface = sideface_cascade.detectMultiScale(gray, 1.2, 3)
    for (x, y, w, h) in sideface:
        # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)

        # 영상 출력
        cv2.imshow('img_w_mosaic', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # 이미지 저장
    output_path = os.path.join(settings.MEDIA_ROOT, 'mosaic', f'mosaic_{board_no}.jpg')
    os.makedirs(os.path.dirname(output_path), exist_ok=True) # 저장 디렉터리 확인
    cv2.imwrite(output_path, img)
    print('이미지 저장 완료:', output_path)

    # DB에 저장
    mos.mos_down = f"mosaic/mosaic_{board_no}.jpg"
    mos.save()