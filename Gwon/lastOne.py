import cv2

# haarcascade 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
sideface_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')

# 이미지 불러오기
img = cv2.imread('original.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 얼굴 찾기
faces = face_cascade.detectMultiScale(gray, 1.2, 4)
for (x, y, w, h) in faces:
    # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi_gray = gray[y: y + h, x: x + w]
    roi_color = img[y: y + h, x: x + w]

# 옆으로 돌아간 얼굴 찾기 ==> 완전한 측면은 인식 불가
sideface = sideface_cascade.detectMultiScale(gray, 1.2, 3)
for (x, y, w, h) in sideface:
    # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y: y + h, x: x + w]
    roi_color = img[y: y + h, x: x + w]

    # 해상도 3배 올리기
    # 모델 로드하기
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel('ESPCN_x3.pb')
    sr.setModel('espcn', 3)
    upscaled_img = cv2.resize(roi_color, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

     # 이미지 축소하기
    downscaled_img = cv2.resize(upscaled_img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # 모자이크 처리
    mosaic_img = cv2.resize(downscaled_img, (w, h), interpolation=cv2.INTER_NEAREST)
    roi_color = cv2.blur(roi_color, (50, 50))
    mosaic = img
    mosaic[y: y + h, x: x + w] = roi_color

    # 원본에 모자이크처리 된 부분 합성
    img = mosaic

# # 합성된 이미지 저장
cv2.imwrite('./array_imges/blended_original2.png', img)

# 이미지 출력
cv2.imshow('blended_img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
