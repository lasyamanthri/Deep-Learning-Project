import numpy as np
import cv2
import time

#import the cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def TakeSnapshotAndSave():
    video = cv2.VideoCapture(0)
    width = 1500
    height = 1080
    dim = (width, height)
    num = 0
    f = []

    while True:
        _, frame = video.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)




        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2, cv2.FILLED)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            #cropped_frame = frame[(x, y), (x + w + w, y + h + h )]
            #cv2.imwrite("some_name.jpg", cropped_frame)


        x = 0
        y = 20
        text_color = (0, 255, 0)
        if type(faces).__module__ == np.__name__:
            f.append(faces)

        if len(f) == 100:
            cv2.imwrite('opencv' + str(num) + '.jpg', frame)

            break
        num = num + 1

        frame = cv2.resize(frame, (315, 315))
        cv2.imshow("Lodhran Camera", frame)
        k = cv2.waitKey(1)

        if k == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    TakeSnapshotAndSave()