import tkinter as tk
from functions import *

window = tk.Tk()
# title
window.title("Smart Attendance System")
window.configure(background="white")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.geometry("500x500")
window.resizable(0, 0)
message = tk.Label(
    window, text='''Smart-Face-Recognition
                 -Attendance-System''',
    bg="blue", fg="white", width=37,
    height=3, font=('times', 20, 'bold'))

message.place(x=10, y=10)


def tranning():
    os.system("python trainning.py")


def attend():
    os.system("python attendance.py")
    




trainImg = tk.Button(window, text="Training"
                     , fg="white", bg="blue", command=tranning,
                     width=20, height=3, activebackground="green",
                     font=('times', 15, ' bold ')).place(x=130, y=120)
attendance = tk.Button(window, text="Attendance"
                       , fg="white", bg="blue",command = attend,
                       width=20, height=3, activebackground="green",
                       font=('times', 15, ' bold ')).place(x=130, y=220)
quitwindow = tk.Button(window, text="Exit"
                       , fg="white", bg="blue", command=window.destroy,

                       width=20, height=3, activebackground="Red",
                       font=('times', 15, ' bold ')).place(x=130, y=320)

window.mainloop()
