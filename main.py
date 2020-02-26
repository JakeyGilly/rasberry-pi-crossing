import tkinter
import face_recognition
import cv2
import _thread
import time
from PIL import Image, ImageTk
video_capture = cv2.VideoCapture(0)
face_locations = []
frame_counter = 0
root = tkinter.Tk()
root.configure(background='green')
root.update()
while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    print(face_locations)
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (60,60,60), 2)
        if len(face_locations) != 0:
            frame_counter += 1
            if frame_counter == 15:
                print("Face Detected and waiting")
                frame_counter = 0
                time.sleep(3)
                ret, frame = video_capture.read()
                rgb_frame = frame[:, :, ::-1]
                face_locations = face_recognition.face_locations(rgb_frame)
                if len(face_locations) != 0:
                    root.configure(background='yellow')
                    root.update()
                    time.sleep(1)
                    root.configure(background='red')
                    root.update()
                    while len(face_locations) != 0:
                        video_capture = cv2.VideoCapture(0)
                        ret, frame = video_capture.read()
                        rgb_frame = frame[:, :, ::-1]
                        face_locations = face_recognition.face_locations(rgb_frame)
                        print(face_locations)
                    time.sleep(5)
                    root.configure(background='yellow')
                    root.update()
                    time.sleep(2)
                    root.configure(background='green')
                    root.update()
                    
                    
                    
    cv2.imshow('Face Recognition', frame)
    if cv2.waitKey(1) == 27:
        break
video_capture.release()
cv2.destroyAllWindows


# SMART CROSSING
# 1. Detect if phone is near the rasberry pi (or with face recognition for abled people)

# 2. send a signal to phone to alert the crossing is near

# 3. if in range while green man send notification to phone/watch (2 buzzes)

# 4. cross