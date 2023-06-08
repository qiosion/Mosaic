import cv2

# haarcascade 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
sideface_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
# eye_detect = False
#haarcascade_eye_tree_eyeglasses.xml

# 얼굴 인식의 경우 크기가 480x360 픽셀 이상인 이미지를 사용
# 얼굴이 권장 각도 범위 이내인 이미지를 사용 피치는 아래로 30도 미만 위로 45도 미만
# 요는 양쪽 방향으로 45도 미만 롤에는 제한이 없다

# 이미지 불러오기
img = cv2.imread('./dd.png')
print(img.shape)
# cv2.imshow('image', img)  # img 쓰면 얼굴 검출  img_w_mosaic 쓰면 블러처리 됨
# cv2.waitKey(0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# exit()
# 얼굴 찾기
faces = face_cascade.detectMultiScale(gray, 1.2, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y: y+h, x: x+w]
    roi_color = img[y: y+h, x: x+w]

    # 모자이크 처리
    # roi_color = cv2.blur(roi_color, (50, 50))
    # img_w_mosaic = img
    # img_w_mosaic[y: y+h, x: x+w] = roi_color

    # 눈 찾기
    eye = eye_cascade.detectMultiScale(roi_gray, 1.03, 6)
    for (ex, ey, ew, eh) in eye:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)

sideface = sideface_cascade.detectMultiScale(gray, 1.2, 3)
for (x, y, w, h) in sideface:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
# exit()

# 영상 출력
cv2.imshow('image', img)  # img 쓰면 얼굴 검출  img_w_mosaic 쓰면 블러처리 됨
cv2.waitKey(0)
cv2.destroyAllWindows()

def opencv_img_save(img, save_img_path, save_img_name):
    """
    ### 처리 이미지 저장 기능
    :param img: 저장할 이미지
    :param save_img_path: 이미지 저장 경로
    :param save_img_name: 저장할 이미지 명
    """
    cv2.imwrite(save_img_path + save_img_name, img)



# 샘플 이미지 경로
origin_image_path ='five.png'
# 처리된 이미지 저장 경로
save_image_path = 'D:\TeamProject\FirstWebSite\Test'

# 샘플 이미지 opencv에서 읽기
origin_image_src = cv2.imread(origin_image_path)
