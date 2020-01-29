import face_recognition
import cv2
video_capture = cv2.VideoCapture(0)
face_locations = []
face_names = []
while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    name = "Person"
    face_names.append(name)
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.rectangle(frame, (left, top), (right, bottom), (60,60,60), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (60,60,60), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 0, 0), 2)
    cv2.imshow('Face Recognition', frame)
    if cv2.waitKey(1) == 27:
        break
video_capture.release()
cv2.destroyAllWindows()
