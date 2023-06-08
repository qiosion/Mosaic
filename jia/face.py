import cv2

# Haar 측면 얼굴 인식
# Haar Cascade 이용하기 haarcascade_profileface
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
profile_face_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')

# 이미지 업로드
img = cv2.imread('fam.jpg')

# 이미지를 그레이스케일로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 얼굴 검출// 파란색: 정면 얼굴 초록색: 측면 얼굴
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
profile_faces = profile_face_cascade.detectMultiScale(gray, 1.3, 5)

# 검출된 얼굴 주변에 사각형 그리기
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

for (x, y, w, h) in profile_faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 결과 이미지 출력
cv2.imshow('img', img)
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