import os
import tkinter as tk
import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def attendance():
    os.system("python Run.py")






if __name__ == '__main__':
        window3 = tk.Tk()
        window3.title("Attendance")
        window3.configure(background="white")
        window3.grid_rowconfigure(0, weight=1)
        window3.grid_columnconfigure(0, weight=1)
        window3.geometry("500x200")
        window3.resizable(0, 0)
        capture = tk.Button(window3, text="Take Attendance"
                            , fg="white", bg="blue",command = attendance,
                            width=20, height=3, activebackground="green",
                            font=('times', 15, ' bold ')).place(x=130, y=0)

        exit = tk.Button(window3, text="Exit"
                         , fg="white", bg="blue", command=window3.destroy,
                         width=20, height=3, activebackground="green",
                         font=('times', 15, ' bold ')).place(x=130, y=100)
        window3.mainloop()
