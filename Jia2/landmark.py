
import dlib
import cv2 as cv
import numpy as np

face_det = dlib.get_frontal_face_detector()
landmark_model = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# range는 끝값이 포함안됨
ALL = list(range(0, 68))
RIGHT_EYEBROW = list(range(17, 22))
LEFT_EYEBROW = list(range(22, 27))
RIGHT_EYE = list(range(36, 42))
LEFT_EYE = list(range(42, 48))
NOSE = list(range(27, 36))
MOUTH_OUTLINE = list(range(48, 61))
MOUTH_INNER = list(range(61, 68))
JAWLINE = list(range(0, 17))
index = ALL


if __name__ == "__main__":
    src = cv.imread("Bin.jpg")
    grey = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

	# 얼굴검출.
    faces = face_det(grey)

    for face in faces:
        # 랜드마크 검출
        lm = landmark_model(src, face)

        lm_point = []
        for p in lm.parts():
            lm_point.append([p.x, p.y])
        lm_point = np.array(lm_point)

        for p in lm_point:
            cv.circle(src, (p[0], p[1]), radius=2, color=(255,0,0), thickness=2)


    cv.imshow("lsh", src)
    cv.waitKey()

