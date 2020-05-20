
import tkinter as tk
import pickle

from tkinter import messagebox

import  os
import face_recognition as fr
def sucess():
    messagebox.showinfo("Success", "DataBase Updated")

def update():
    encoded = {}
    attendancesheet = {}

    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".jpeg"):
                face = fr.load_image_file("faces/" + f)
                try:
                    encoding = fr.face_encodings(face)[0]
                    encoded[f[:5].split(".")[0]] = encoding

                except:
                    pass


    with open('data.pickle', 'wb') as handle:
        pickle.dump(encoded, handle, protocol=pickle.HIGHEST_PROTOCOL)



    sucess()




if __name__ == '__main__':
        window1 = tk.Tk()
        window1.title("Training")
        window1.configure(background="white")
        window1.grid_rowconfigure(0, weight=1)
        window1.grid_columnconfigure(0, weight=1)
        window1.geometry("500x500")
        window1.resizable(0, 0)

        lbl1 = tk.Label(window1, text='''     For Tranning copy 
         photos of students with clear
          face to faces directory
          and then click Update below''',
                       width=30, fg="blue", bg="white",
                       height=5, font=('times', 20, ' bold ')).place(x=0, y=40)
        lbl2 = tk.Label(window1,text = "Updating Database May take 2-5 mins \n Depends on Number of students added",
                        width =45,height = 3,fg = "red",bg = "white",font=('times', 15, ' bold ') ).place(x=0,y=220)


        capture = tk.Button(window1, text="Update"
                             , fg="white", bg="blue",command = update,
                             width=20, height=3, activebackground="green",
                             font=('times', 15, ' bold ')).place(x=130, y=310)
        exit = tk.Button(window1, text="Exit"
                            , fg="white", bg="blue", command=window1.destroy,
                            width=20, height=3, activebackground="green",
                            font=('times', 15, ' bold ')).place(x=130, y=410)


        window1.mainloop()
