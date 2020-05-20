import json
import tkinter as tk
import pickle
import shutil

from tkinter import messagebox,filedialog as fd
from tkinter.ttk import *
import os
import face_recognition as fr

import cv2

def fail():
    messagebox.showinfo("Fail", '''Image Quality is Low use HD camera''')

def update(new_encoded):



        pkl_file = open('data.pickle', 'rb')
        mydict = pickle.load(pkl_file)
        pkl_file.close()


        # update dict and write to the file again
        mydict.update(new_encoded)
        output = open('data.pickle', 'wb')
        pickle.dump(mydict, output)
        output.close()

        # read python dict back from the file
        # pkl_file = open('data.pickle', 'rb')
        # mydict = pickle.load(pkl_file)
        # pkl_file.close()
        attendancedict = {}
        for dirpath, dnames, fnames in os.walk("./faces"):
                for f in fnames:
                        attendancedict.update({f[:5]: "absent"})
        output = open('attend.pickle', 'wb')
        pickle.dump(attendancedict, output)
        output.close()



def encodingcheck(target,m = 1,a="a"):
    encoded = {}
    face = fr.load_image_file(target)
    face_bounding_boxes = fr.face_locations(face)

    if len(face_bounding_boxes)==1:


        try:


            encoding = fr.face_encodings(face)[0]
            encoded[a.split(".")[0]] = encoding

        except:
            pass
        print(encoded)
        if not bool(encoded):

            return False
        else:
            update(encoded)
            return True
    elif(m==2):
        return False
    else:
        messagebox.showinfo("Fail", '''Uploaded Photo contain no Faces''')
        return False



def copy():

    name = txt1.get()
    id = txt2.get()
    if name.isalpha() and len(id)==5 and id.isnumeric():
        original = fd.askopenfilename()

        target = "faces\{}-{}.jpg".format(id, name)
        if encodingcheck(original,1,id):
            shutil.copyfile(original, target)
            messagebox.showinfo("success", '''Uploaded Successfully''')

        else:
            fail()


    else:
        messagebox.showinfo("Error", '''Id should be in numbers with length 5\n Name should contain only letters ''')




encoder = {}

def capture():

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    cap = cv2.VideoCapture(0)
    i = 1

    while True:

        ret, img = cap.read()


        photo = img
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            # photo = Image.fromarray(photo)


            name = txt1.get()
            id = txt2.get()
            print(name + ' '+ id)
            a = "{}-{}.jpg".format(id, name)



            cv2.imwrite("faces//" + a,photo)
            face = fr.load_image_file("faces//" + a)


            try:
                encoding = fr.face_encodings(face)[0]
                encoder[a[:5].split(".")[0]] = encoding
            except:
                print("passed")
                pass
            cv2.imshow('img', img)
            


            i = i + 1
            if encodingcheck("faces//" + a,2,id):

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Success", "Face Captured Succesfully")

                i=50
                break
        if i ==50:
            break




    cv2.destroyAllWindows()

if __name__ == '__main__':
        window1 = tk.Tk()
        window1.title("Training")
        window1.configure(background="white")
        window1.grid_rowconfigure(0, weight=1)
        window1.grid_columnconfigure(0, weight=1)
        window1.geometry("700x600")
        window1.resizable(0, 0)
        lbl1 = tk.Label(window1, text="Name",
                        width=15, fg="blue", bg="white",
                        height=1, font=('times', 25, ' bold ')).place(x=215, y=20)
        txt1 = tk.Entry(window1, width=40,
                       bg="white", fg="black",
                       font=('times', 15, ' bold '))
        txt1.place(x=155, y=80)
        lbl2 = tk.Label(window1, text="ID(5 Digit)",
                        width=15, fg="blue", bg="white",
                        height=1, font=('times', 25, ' bold ')).place(x=215, y=130)
        txt2 = tk.Entry(window1, width=40,
                        bg="white", fg="black",
                        font=('times', 15, ' bold '))
        txt2.place(x=155, y=190)


        capture = tk.Button(window1, text="Capture"
                             , fg="white", bg="blue",command = capture,
                             width=20, height=3, activebackground="green",
                             font=('times', 15, ' bold ')).place(x=230, y=310)
        importfile = tk.Button(window1, text="Upload Photo"
                         , fg="white", bg="blue", command=copy,
                         width=20, height=3, activebackground="green",
                         font=('times', 15, ' bold ')).place(x=230, y=410)
        exit = tk.Button(window1, text="Exit"
                            , fg="white", bg="blue", command=window1.destroy,
                            width=20, height=3, activebackground="green",
                            font=('times', 15, ' bold ')).place(x=230, y=510)

        window1.mainloop()
# print(encoder)

# get_encoded_faces()