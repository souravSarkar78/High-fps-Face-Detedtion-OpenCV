import cv2
import mediapipe as mp
import time


mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
face_detection = mpFaceDetection.FaceDetection()

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_detection.process(imgRGB)

    for detections in results.detections:
        mpDraw.draw_detection(frame, detections)
        print(detections)


    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()