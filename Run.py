import os
import time
import cv2


from PIL import Image
import openpyxl

from functions import classify_face1
a = []

def xlsheet(D):
    import pandas as pd



    df = pd.DataFrame(data=D, index=[0])

    df = (df.T)

    print(df)

    df.to_excel('attendance.xlsx')


# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)
# attendance via video file as input
# cap = cv2.VideoCapture('video.mp4')
i =0



while True:
    # Read the frame
    _, img = cap.read()


    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        im = Image.fromarray(img)
        im.save("your_file {}.jpeg".format(i))
        time.sleep(2)

        a = classify_face1("your_file {}.jpeg".format(i))
        if a != None:
            print(a[0])
            b = a[1]



        time.sleep(2)
        os.remove("your_file {}.jpeg".format(i))
        i = i + 1
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff

    if k==27:
        break

# Release the VideoCapture object
cap.release()
xlsheet(b)
