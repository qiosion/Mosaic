import os
import cv2
import numpy as np
from django.shortcuts import render, redirect

from config import settings
from mosaicImg.models import MosaicImg

import random

from PIL import Image
import os


def mosaic_download(request, mos_no):
    mos = MosaicImg.objects.get(mos_no=mos_no)
    path = os.path.split(mos.mos_up.name)[1]
    print("다운로드시 경로 뭐냐 path : ", path)
    mosaic_path = os.path.join(settings.MEDIA_ROOT, 'mosaic', f'mosaic_{path}')
    mosaic_url = settings.MEDIA_URL + 'mosaic/' + f'mosaic_{path}'

    return redirect(mosaic_url)



def get_mosaic_haar(request, mos_no):
    mos = MosaicImg.objects.get(mos_no=mos_no)
    path = os.path.split(mos.mos_up.name)[1]
    file_name, extension = os.path.splitext(path)
    input_path = os.path.join(settings.MEDIA_ROOT, 'uploads', f'{path}')
    print("input_path : ", input_path)

    # haarcascade 불러오기
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    sideface_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    # 이미지 불러오기
    if extension.lower() == '.png':
        img = cv2.imread(input_path, cv2.IMREAD_COLOR)
        print("img : ", img)
    else:
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
    output_path = os.path.join(settings.MEDIA_ROOT, 'mosaic', f'mosaic_{path}')
    os.makedirs(os.path.dirname(output_path), exist_ok=True) # 저장 디렉터리 확인
    cv2.imwrite(output_path, img)
    print('이미지 저장 완료:', output_path)

    # DB에 저장
    mos.mos_down = f"mosaic/mosaic_{path}"
    mos.save()



def get_mosaic_zoom(request, mos_no):
    mos = MosaicImg.objects.get(mos_no=mos_no)
    path = os.path.split(mos.mos_up.name)[1]
    file_name, extension = os.path.splitext(path)
    input_path = os.path.join(settings.MEDIA_ROOT, 'uploads', f'{path}')
    print("input_path : ", input_path)

    # haarcascade 불러오기
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    sideface_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    # 이미지 불러오기
    if extension.lower() == '.png':
        img = cv2.imread(input_path, cv2.IMREAD_COLOR)
        print("img : ", img)
    else:
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
    output_path = os.path.join(settings.MEDIA_ROOT, 'mosaic', f'mosaic_{path}')
    os.makedirs(os.path.dirname(output_path), exist_ok=True) # 저장 디렉터리 확인
    cv2.imwrite(output_path, img)
    print('이미지 저장 완료:', output_path)

    # DB에 저장
    mos.mos_down = f"mosaic/mosaic_{path}"
    mos.save()


def zoom_image(image_path):
    img = cv2.imread(image_path)
    img_result = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    cv2.imshow("x2", img_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def upscale_image(output_path):
    # 모델 로드하기
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel('ESPCN_x3.pb')
    sr.setModel('espcn', 3)

    # 이미지 로드하기
    img = cv2.imread(output_path)

    # 이미지 추론하기(해당 함수는 전처리와 후처리를 한꺼번에 해줍니다.)
    result = sr.upsample(img)

    # 결과 이미지 비교하기
    resized_img = cv2.resize(img, dsize=None, fx=3, fy=3)

    cv2.imshow('Original Image', img)   # 원본
    cv2.imshow('Resized Image', resized_img)  # 크기를 3배로 변경한 이미지
    cv2.imshow('Upscaled Image', result)   # 해상도 올린 이미지
    cv2.waitKey(0)
    cv2.destroyAllWindows()




# 전체 이미지 셔플
def get_shuffle_img(request, mos_no):
    mos = MosaicImg.objects.get(mos_no=mos_no)
    path = os.path.split(mos.mos_up.name)[1]

    input_path = os.path.join(settings.MEDIA_ROOT, 'uploads', f'{path}')
    print("input_path : ", input_path)

    pieces = split_image(input_path)
    shuffled_pieces = shuffle_pieces(pieces)
    combined_image = combine_pieces(shuffled_pieces)

    output_path = os.path.join(settings.MEDIA_ROOT, 'mosaic', f'mosaic_{path}')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 저장 디렉터리 확인

    combined_image.save(output_path)
    # DB에 저장
    mos.mos_down = f"mosaic/mosaic_{path}"
    mos.save()

def split_image(input_path):
    image = Image.open(input_path)

    width, height = image.size

    piece_width = width // 20
    piece_height = height // 20

    pieces = []
    for y in range(0, height, piece_height):
        for x in range(0, width, piece_width):
            # 조각이미지 생성
            piece = image.crop((x, y, x + piece_width, y + piece_height))
            pieces.append(piece)
    return pieces

def shuffle_pieces(pieces):
    random.shuffle(pieces)
    return pieces

# def combine_pieces(pieces, piece_size):
    # width, height = piece_size
def combine_pieces(pieces):
    width = pieces[0].width
    height = pieces[0].height
    combined_img = Image.new('RGB', (width * 20, height * 20))

    for i, piece in enumerate(pieces):
        x = (i % 20) * width
        y = (i // 20) * height
        combined_img.paste(piece, (x, y))
    # combined_img = combined_img.resize((517, 517))

    return combined_img

# 얼굴만 셔플
def get_face_shuffle(request, mos_no):
    mos = MosaicImg.objects.get(mos_no=mos_no)
    path = os.path.split(mos.mos_up.name)[1]

    input_path = os.path.join(settings.MEDIA_ROOT, 'uploads', f'{path}')
    print("input_path : ", input_path)

    # haarcascade 불러오기
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 이미지 불러오기
    img = cv2.imread(input_path)
    print("img : ", img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 얼굴 찾기
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)

    # 얼굴 객체만 추출하여 셔플
    face_images = []
    for (x, y, w, h) in faces:
        roi_gray = gray[y: y + h, x: x + w]
        roi_color = img[y: y + h, x: x + w]
        face_images.append(roi_color)

    # 얼굴 이미지 셔플
    # shuffled_face_img = shuffle_face_obj(face_images)
    pieces = split_face_obj(face_images)
    shuffled_pieces = shuffle_face_obj(pieces)
    combined_image = combine_pieces(shuffled_pieces)
    # combined_image = combine_pieces(shuffled_pieces, (w, h))

    # PIL Image를 NumPy 배열로 변환
    combined_image_np = np.array(combined_image)

    """
    # 원본에 셔플 이미지 덮어쓰기 -> 구현중
    result = img.copy()

    for i, (x, y, w, h) in enumerate(faces):
        result[y: y + h, x: x + w] = combined_image_np[i]
    """
    # 이미지 저장
    output_path = os.path.join(settings.MEDIA_ROOT, 'mosaic', f'mosaic_{path}')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    # cv2.imwrite(output_path, result)
    cv2.imwrite(output_path, combined_image_np)
    print('이미지 저장 완료:', output_path)

    # DB에 저장
    mos.mos_down = f"mosaic/mosaic_{path}"
    mos.save()

def split_face_obj(face_images):
    pieces = []
    for image in face_images:
        image = Image.fromarray(image)
        width, height = image.size
        # width, height, _ = image.shape

        piece_width = width // 20
        piece_height = height // 20

        for y in range(0, height, piece_height):
            for x in range(0, width, piece_width):
                # 조각이미지 생성
                piece = image.crop((x, y, x + piece_width, y + piece_height))
                pieces.append(piece)
    return pieces

def shuffle_face_obj(pieces):
    np.random.shuffle(pieces)
    return pieces

# def combine_images(images):
#     num_images = len(images)
#     if num_images == 0:
#         return None
#
#     image_height, image_width, _ = images[0].shape
#     combined_width = image_width * num_images
#     combined_image = np.zeros((image_height, combined_width, 3), dtype=np.uint8)
#
#     for i, image in enumerate(images):
#         x_start = i * image_width
#         x_end = (i + 1) * image_width
#         combined_image[:, x_start:x_end, :] = image
#
#     return combined_image


# # 2배 Zoom
# def zoom_image(image_path):
#     img = cv2.imread(image_path)
#     img_result = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
#     cv2.imshow("x2", img_result)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
# image_path = 'faces0.png'
# zoom_image(image_path)
#
#
# # 해상도 3배로 올리는 함수
# # 파일도 같이 올렸지만 혹시 돌아가지 않는 다면 pip install opencv-contrib-python 설치하기
# def upscale_image(output_path):
#     # 모델 로드하기
#     sr = cv2.dnn_superres.DnnSuperResImpl_create()
#     sr.readModel('ESPCN_x3.pb')
#     sr.setModel('espcn', 3)
#
#     # 이미지 로드하기
#     img = cv2.imread(output_path)
#
#     # 이미지 추론하기(해당 함수는 전처리와 후처리를 한꺼번에 해줍니다.)
#     result = sr.upsample(img)
#
#     # 결과 이미지 비교하기
#     resized_img = cv2.resize(img, dsize=None, fx=3, fy=3)
#
#     cv2.imshow('Original Image', img)   # 원본
#     cv2.imshow('Resized Image', resized_img)  # 크기를 3배로 변경한 이미지
#     cv2.imshow('Upscaled Image', result)   # 해상도 올린 이미지
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
# image_path = 'zoom_pp0.jpg'
# upscale_image(image_path)